from django.conf import settings
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

from core.models import BaseModel
from core.managers import BaseManager


# Create your models here.
class UserManager(BaseManager, BaseUserManager):

    def create_user(self, username, email, password=None, **kwargs):
        if username is None:
            raise TypeError("Username must be provided")
        if not email:
            raise TypeError("email must be provided")
        if not password:
            raise TypeError("Password cannot be blank")
        user = self.model(
            username=username, email=self.normalize_email(email), **kwargs
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password, **kwargs):
        if not username:
            raise TypeError("Username must be provided")
        if not email:
            raise TypeError("email must be provided")
        if not password:
            raise TypeError("Password cannot be blank")
        user = self.create_user(username, email, password, **kwargs)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user

class Profile(BaseModel):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='profile')
    date_of_birth = models.DateTimeField(blank=True,null=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d',blank=True)

    def __str__(self):
        return f"Profile {self.user.name if self.user.name else self.user.get_email()}"
class User(BaseModel, AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    username = models.CharField(db_index=True, max_length=128, unique=True, null=False)
    email = models.EmailField(db_index=True, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    #profile = models.OneToOneField(to=Profile,related_name='profile',on_delete=models.CASCADE)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]
    #profile = models.OneToOneField(to=P)
    objects = UserManager()

    def __str__(self):
        return self.name if self.name else self.email

    @property
    def name(self):
        return self.first_name + " " + self.last_name

    def get_email(self):
        return self.email

