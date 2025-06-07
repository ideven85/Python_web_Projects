import hashlib
import hmac
import logging
import os
import random

import boto3
from django.contrib.auth.models import User
from django.shortcuts import render
from django.utils.translation import gettext_lazy as _
from django.views.generic import DetailView, CreateView
from django.views.generic.base import View
from rest_framework import permissions, status, authentication
from rest_framework.response import Response
from rest_framework.views import APIView

# from camiyaqui.settings.aws_credentials import (
#     AWS_ACCESS_KEY_ID,
#     AWS_BUCKET_NAME,
#     AWS_BUCKET_REGION,
#     AWS_SECRET_ACCESS_KEY,
# )
from ourwedding.mixins import GuestMixin
from .models import FileItem, Album

logger = logging.getLogger(__name__)


class FilePolicyAPI(APIView):
    """
    This view is to get the AWS Upload Policy for our s3 bucket.
    What we do here is first create a FileItem object instance in our
    Django backend. This is to include the FileItem instance in the path
    we will use within our bucket as you'll see below.
    """

    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.SessionAuthentication]

    def post(self, request, *args, **kwargs):
        """
        The initial post request includes the filename
        and auth credientails. In our case, we'll use
        Session Authentication but any auth should work.
        """
        filename_req = request.data.get("filename")
        album_pk = request.data.get("album_pk", None)
        if album_pk:
            try:
                album = Album.objects.get(id=album_pk)
            except Album.DoesNotExist:
                album = None

        # s3 = boto3.client('s3',
        #                   region_name=AWS_BUCKET_REGION,
        #                   aws_access_key_id=AWS_ACCESS_KEY_ID,
        #                   aws_secret_access_key=AWS_SECRET_ACCESS_KEY)

        if not filename_req:
            return Response(
                {"message": "A filename is required"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        user = request.user
        username_str = str(request.user.username)

        file_obj = FileItem.objects.create(user=user, name=filename_req, album=album)
        file_obj_id = file_obj.id
        upload_start_path = f"{username_str}/{file_obj_id}/"

        _, file_extension = os.path.splitext(filename_req)
        filename_final = f"{file_obj_id}{file_extension}"

        final_upload_path = f"{upload_start_path}{filename_final}"

        file_obj.path = final_upload_path
        file_obj.extension = file_extension[1:]
        file_obj.save()

        # presigned_post = s3.generate_presigned_post(
        #     Bucket=AWS_BUCKET_NAME,
        #     Key=final_upload_path,
        #     Fields={"acl": "private", "Content-Type": ""},
        #     Conditions=[
        #         {"acl": "private"},
        #         {"Content-Type": ""}
        #     ],
        #     ExpiresIn=3600
        # )

        # data = {'policy': presigned_post,
        #         'file_id': file_obj_id
        #         }

        return Response(None, status=status.HTTP_200_OK)


class FileUploadCompleteHandler(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.SessionAuthentication]

    def post(self, request, *args, **kwargs):
        file_id = request.POST.get("file")
        data = {}
        type_ = request.POST.get("fileType")
        if file_id:
            obj = FileItem.objects.get(id=int(file_id))
            obj.uploaded = True
            obj.type = type_
            obj.save()
            data["id"] = obj.id
            data["saved"] = True
        return Response(data, status=status.HTTP_200_OK)


def sign(key, msg):
    return hmac.new(key, msg.encode("utf-8"), hashlib.sha256).digest()


def getSignatureKey(key, date_stamp, regionName, serviceName):
    kDate = sign(("AWS4" + key).encode("utf-8"), date_stamp)
    kRegion = sign(kDate, regionName)
    kService = sign(kRegion, serviceName)
    kSigning = sign(kService, "aws4_request")
    return kSigning


class GalleryList(GuestMixin, View):
    def get(self, request):
        gallery_users = FileItem.objects.values("user").distinct()
        galleries = []
        for user_dict in gallery_users:
            user = User.objects.get(id=user_dict["user"])
            img_preview = random.choice(FileItem.objects.filter(user=user).all())
            preview = img_preview.gallery_thumbnail
            gallery = {"owner": user, "preview": preview}
            galleries.append(gallery)

        return render(request, "photos/galleries.html", {"galleries": galleries})


class GalleryView(GuestMixin, View):
    def get(self, request, pk):
        user = User.objects.get(pk=pk)
        images = FileItem.objects.filter(file_type="image", uploaded=True).filter(
            user=user
        )
        title = _("Image Gallery by {}").format(user.profile)
        gallery = {"title": title, "images": images, "preview": images.first()}
        return render(request, "photos/gallery.html", {"gallery": gallery})


class AlbumNew(GuestMixin, CreateView):
    model = Album
    fields = ("name", "description")
    template_name = "photos/album_create.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class AlbumAdd(GuestMixin, DetailView):
    template_name = "photos/album_add.html"
    model = Album
    context_object_name = "album"


class AlbumView(GuestMixin, DetailView):
    template_name = "photos/gallery.html"
    model = Album
    context_object_name = "gallery"
