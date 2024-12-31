from django.contrib.auth.models import User
from django.utils.http import base36_to_int
from rest_framework import serializers
from rest_framework.authtoken.models import Token

from backend.models import PushTokens, News
from ourwedding.models import Profile, MessageFromGuest, Guest
from ourwedding.tokens import login_token_generator
from photos.models import FileItem


class GuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = (
            "first_name",
            "last_name",
            "nickname",
            "email",
            "phone",
            "is_attending",
            "is_child",
            "has_car",
            "needs_van",
            "dietary_restrictions",
            "comes_from",
            "invited_by",
            "pk",
        )


class UpdateGuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = (
            "nickname",
            "phone",
            "is_attending",
            "is_child",
            "has_car",
            "dietary_restrictions",
            "comes_from",
            "invited_by",
            "pk",
        )


class UserSerializer(serializers.ModelSerializer):
    profile = UpdateGuestSerializer()

    class Meta:
        model = User
        fields = ("first_name", "last_name", "email", "profile")

    def update(self, instance, validated_data):
        guest_data = validated_data.pop("profile")
        user = super(UserSerializer, self).update(instance, validated_data)
        serializer = UpdateGuestSerializer(instance.profile, data=guest_data)
        serializer.is_valid()
        serializer.save()
        return user


class NewGuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guest
        fields = ("first_name", "last_name", "email", "is_attending")


class RsvpSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = (
            "first_name",
            "last_name",
            "is_attending",
            "is_child",
            "has_car",
            "needs_van",
            "dietary_restrictions",
            "comes_from",
            "id",
        )
        read_only_fields = ("first_name", "last_name", "id")


class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = PushTokens
        fields = ("token",)


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = MessageFromGuest
        fields = ("message",)


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    phone = serializers.CharField(max_length=255, required=False)
    access_code = serializers.CharField(max_length=255, required=True)

    def validate_access_code(self, code):
        access_code = code.lower()
        if len(access_code.split("-")) != 3:
            raise serializers.ValidationError("Wrong access code format")
        a, b, user_pk = code.split("-")
        user_pk = base36_to_int(user_pk)
        try:
            user = User.objects.get(pk=user_pk)
        except User.DoesNotExist:
            raise serializers.ValidationError("Secret Code not Valid")

        if not login_token_generator.check_token(user, code):
            raise serializers.ValidationError("Access Code Expired. Require a New one.")
        return user_pk


class RegisterSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    first_name = serializers.CharField(max_length=255, required=True)
    last_name = serializers.CharField(max_length=255, required=True)
    phone = serializers.CharField(max_length=255, required=True)


class RequestAccessCodeSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)


class APITokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = ("key",)


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileItem
        fields = ("name",)


class PhotoConfirmSerializer(serializers.Serializer):
    file_id = serializers.IntegerField(required=True)


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ("title", "message", "published_on", "pk")
