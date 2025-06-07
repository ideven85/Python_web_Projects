import base64
import json

from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _


class Album(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, null=False, on_delete=models.CASCADE
    )
    name = models.CharField(_("name"), max_length=50, null=False, blank=False)
    description = models.TextField(_("description"))
    creation_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now_add=False, null=True, default=None)

    def get_absolute_url(self):
        return f"/photos/album/{self.pk}"


class FileItem(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, default=1, on_delete=models.SET_NULL, null=True
    )
    album = models.ForeignKey(Album, null=True, default=None, on_delete=models.SET_NULL)
    name = models.CharField(max_length=120, null=True, blank=True)
    path = models.TextField(blank=True, null=True)
    size = models.BigIntegerField(default=0)
    extension = models.CharField(max_length=10, null=True, blank=True)
    file_type = models.CharField(max_length=120, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    uploaded = models.BooleanField(default=False)
    active = models.BooleanField(default=True)

    @property
    def title(self):
        return str(self.name)

    def save(self, **kwargs):
        if self.extension and not self.file_type:
            if self.extension in ("jpg", "jpeg", "png", "bmp", "gif"):
                self.file_type = "image"
            elif self.extension in ("mov", "mp4", "mpeg4", "avi"):
                self.file_type = "video"
            elif self.extension in ("mp3"):
                self.file_type = "audio"
            else:
                self.file_type = None
        super().save(**kwargs)

    @property
    def gallery_thumbnail(self):
        edits = {"resize": {"width": 300, "height": 300, "fit": "outside"}}
        data = {"bucket": settings.AWS_BUCKET_NAME, "key": self.path, "edits": edits}
        data_str = json.dumps(data)
        data_enc = base64.b64encode(data_str.encode("utf-8"))
        return settings.RESIZE_API_ENDPOINT + "/" + data_enc.decode()

    @property
    def thumbnail(self):
        edits = {"resize": {"width": 150, "height": 150, "fit": "outside"}}
        data = {"bucket": settings.AWS_BUCKET_NAME, "key": self.path, "edits": edits}
        data_str = json.dumps(data)
        data_enc = base64.b64encode(data_str.encode("utf-8"))
        return settings.RESIZE_API_ENDPOINT + "/" + data_enc.decode()

    @property
    def image(self):
        edits = {"resize": {"width": 1024, "height": 768, "fit": "outside"}}
        data = {"bucket": settings.AWS_BUCKET_NAME, "key": self.path, "edits": edits}
        data_str = json.dumps(data)
        data_enc = base64.b64encode(data_str.encode("utf-8"))
        return settings.RESIZE_API_ENDPOINT + "/" + data_enc.decode()


class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    comment = models.TextField()
    foto = models.ForeignKey(FileItem, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        get_latest_by = "-timestamp"
        ordering = [
            "-timestamp",
        ]


class Likes(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    foto = models.ForeignKey(FileItem, on_delete=models.CASCADE, related_name="likes")
    timestamp = models.DateTimeField(auto_now_add=True)
