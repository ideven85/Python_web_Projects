import uuid

from django.conf import settings

# from django.conf.global_settings import AUTH_USER_MODEL
# from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.core.exceptions import ObjectDoesNotExist
from django.db import models

# from django.db.models.functions import Now
from django.http import Http404
from django.urls import reverse
from django.utils import timezone


class BaseManager(models.Manager):
    def get_object_by_public_id(self, public_id):
        try:
            instance = self.get(public_id=public_id)
            return instance
        except (ObjectDoesNotExist, ValueError, TypeError):
            return Http404


# Create your models here.
class BaseModel(models.Model):
    public_id = models.UUIDField(db_index=True, unique=True, default=uuid.uuid4)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    objects = BaseManager()

    class Meta:
        abstract = True


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Post.Status.PUBLISHED)


class Post(BaseModel):

    class Status(models.TextChoices):
        DRAFT = "DF", "Draft"
        PUBLISHED = "PB", "Published"

    title = models.CharField(max_length=128)
    author = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="posts"
    )
    slug = models.SlugField(max_length=128)
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    status = models.CharField(choices=Status, max_length=2, default=Status.DRAFT)

    objects = models.Manager()
    published = PublishedManager()

    class Meta:
        ordering = ["-publish"]

    def get_absolute_url(self):
        return reverse("core:post_detail", args=[self.id])

    def __str__(self):
        return self.title


class Comment(BaseModel):
    post = models.ForeignKey(to=Post, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=128)
    email = models.EmailField()
    body = models.TextField()
    active = models.BooleanField()

    class Meta:
        ordering = ["created"]
        indexes = [models.Index(fields=["created"])]

    def __str__(self):
        return f"Commented by {self.name} on {self.post}"
