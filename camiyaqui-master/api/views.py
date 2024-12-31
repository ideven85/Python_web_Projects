import logging
import os

import boto3
from django.contrib.auth.models import User
from rest_framework import viewsets, views, status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from api.serializers import (
    GuestSerializer,
    TokenSerializer,
    RsvpSerializer,
    NewGuestSerializer,
    MessageSerializer,
    LoginSerializer,
    APITokenSerializer,
    RegisterSerializer,
    UserSerializer,
    RequestAccessCodeSerializer,
    PhotoSerializer,
    PhotoConfirmSerializer,
    NewsSerializer,
)
from backend.models import News

# from camiyaqui.settings.aws_credentials import AWS_BUCKET_REGION, AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, \
#    AWS_BUCKET_NAME
from ourwedding.models import Profile, Group, MessageFromGuest, Guest
from photos.models import FileItem

logger = logging.getLogger(__name__)


class RequestAccessCode(views.APIView):
    """View to request a new access code."""

    permission_classes = ()

    def post(self, request):
        serializer = RequestAccessCodeSerializer(data=request.data)
        if serializer.is_valid():
            try:
                user = User.objects.get(email=serializer.validated_data.get("email"))
            except User.DoesNotExist:
                return Response(
                    {"error_message": "User does not exist"},
                    status=status.HTTP_401_UNAUTHORIZED,
                )
            user.profile.send_code()
            return Response({"message": "Check your e-mail"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(views.APIView):
    """View used for sending the email the first time and replying with the API token which is unique for
    every user. This and the registration endpoint should be the only public ones.
    All the rest should require authentication.
    """

    permission_classes = ()

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            try:
                user = User.objects.get(email=serializer.validated_data.get("email"))
            except User.DoesNotExist:
                return Response(
                    {"error_message": "Email not valid"},
                    status=status.HTTP_404_NOT_FOUND,
                )
            if user.pk != serializer.validated_data.get("access_code"):
                return Response(
                    {"error_message": "Access code and email don't match"},
                    status=status.HTTP_401_UNAUTHORIZED,
                )

            token, _ = Token.objects.get_or_create(user=user)
            token_serializer = APITokenSerializer(token)
            user.profile.phone = serializer.validated_data.get("phone")
            user.save()
            return Response(token_serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RegisterView(views.APIView):
    """This is the second public endpoint, used for registering new users who want to have access to the app but
    their email is not yet listed.
    """

    permission_classes = ()

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            if User.objects.filter(
                email=serializer.validated_data.get("email")
            ).exists():
                return Response(
                    {"error_message": "You are registered, try logging in"},
                    status=status.HTTP_406_NOT_ACCEPTABLE,
                )

            guest, created = Guest.objects.get_or_create(
                email=serializer.validated_data.get("email")
            )
            if created:
                guest.first_name = serializer.validated_data.get("first_name")
                guest.last_name = serializer.validated_data.get("last_name")
                guest.phone = serializer.validated_data.get("phone")
                guest.save()
                return Response(
                    {"message": "Profile waiting approval"}, status=status.HTTP_200_OK
                )

            return Response(
                {"message": "Profile waiting approval"}, status=status.HTTP_200_OK
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GuestViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = GuestSerializer


class PushTokenView(views.APIView):
    def post(self, request):
        serializer = TokenSerializer(data=request.data)
        if serializer.is_valid():
            token = serializer.save()
            token.user = request.user
            token.save()
            return Response({"message": "Token OK"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MessageView(views.APIView):
    """Allows the guests to communicate with us and to see their previous messages."""

    def get(self, request):
        messages = MessageFromGuest.objects.filter(guest=request.user)
        serializer = MessageSerializer(messages, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MessageSerializer(data=request.data)
        if serializer.is_valid():
            message = serializer.save()
            message.guest = request.user
            message.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GuestView(views.APIView):
    """View the details of the guest and allows him/her to update the information."""

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)

    def put(self, request, format=None):
        serializer = UserSerializer(request.user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VerifyToken(views.APIView):
    """Verifies whether the user has access to the app. This is in part kept for backwards compatibility, in part
    to give a clear endpoint where to check for the validity of the stored authentication token. If the response code
    is 200, then the token is OK, all other responses (especially 401) means the token is not valid.
    """

    def get(self, request):
        print(request.user)
        return Response({"message": "Token OK"})


class GuestRsvp(views.APIView):
    """Endpoint to update the RSVP status. It is very similar to the profile endpoint, but it only allows modifying
    some of the fields on the profile of the user and not on the user account itself.
    """

    def get(self, request):
        serializer = RsvpSerializer(request.user.profile)
        return Response(serializer.data)

    def put(self, request, guest_id=None):
        guest = request.user.profile
        if guest_id:
            guest = Profile.objects.get(id=guest_id)
        serializer = RsvpSerializer(guest, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        logger.info(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GroupView(views.APIView):
    def get(self, request):
        try:
            guests = request.user.profile.group.members.exclude(
                id=request.user.profile.id
            ).all()
        except:
            return Response(
                {"message": "This user has no group"}, status=status.HTTP_404_NOT_FOUND
            )
        serializer = RsvpSerializer(guests, many=True)
        logger.info("Got {} group members for {}".format(guests.count(), request.user))
        return Response(serializer.data)


class GuestAdd(views.APIView):
    def post(self, request):
        serializer = NewGuestSerializer(data=request.data)
        if serializer.is_valid():
            if not request.user.profile.group:
                group = Group.objects.create(
                    name="Group {}".format(request.user.profile)
                )
                request.user.profile.group = group
                request.user.profile.save()
            guest = serializer.save()
            guest.invited_by = request.user
            guest.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PhotoUploadPolicy(views.APIView):
    """
    This view is to get the AWS Upload Policy for our s3 bucket.
    What we do here is first create a FileItem object instance in our
    Django backend. This is to include the FileItem instance in the path
    we will use within our bucket as you'll see below.
    """

    def post(self, request, *args, **kwargs):
        """
        The initial post request includes the filename
        and auth credientails. In our case, we'll use
        Session Authentication but any auth should work.
        """
        serializer = PhotoSerializer(data=request.data)
        if serializer.is_valid():
            user = request.user
            file_obj = serializer.save()
            file_obj.user = user
            file_obj.save()
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        username_str = str(user.username)
        file_obj_id = file_obj.id
        upload_start_path = f"{username_str}/{file_obj_id}/"

        _, file_extension = os.path.splitext(serializer.validated_data.get("name"))

        filename_final = f"{file_obj_id}{file_extension}"

        final_upload_path = f"{upload_start_path}{filename_final}"

        file_obj.path = final_upload_path
        file_obj.extension = file_extension[1:]
        file_obj.save()

        return Response(data, status=status.HTTP_200_OK)


class PhotoUploadComplete(views.APIView):
    def post(self, request, *args, **kwargs):
        serializer = PhotoConfirmSerializer(data=request.data)
        if serializer.is_valid():
            file_id = serializer.validated_data.get("file_id")
            try:
                file = FileItem.objects.get(id=file_id)
            except FileItem.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
            file.uploaded = True
            file.save()
            data = PhotoSerializer(file)
            return Response(data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class NewsView(views.APIView):
    def get(self, request):
        queryset = News.objects.filter(language=request.user.profile.language)
        serializer = NewsSerializer(queryset, many=True)
        return Response(serializer.data)
