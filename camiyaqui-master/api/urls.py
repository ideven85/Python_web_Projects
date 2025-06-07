from django.urls import include, path
from rest_framework import routers
from rest_framework.documentation import include_docs_urls
from api import views
from api.views import (
    VerifyToken,
    RegisterView,
    GuestRsvp,
    GroupView,
    GuestAdd,
    GuestView,
    MessageView,
    LoginView,
    PushTokenView,
    RequestAccessCode,
    PhotoUploadPolicy,
    PhotoUploadComplete,
    NewsView,
)

router = routers.DefaultRouter()
router.register(r"guests", views.GuestViewSet)


urlpatterns = [
    path("", include(router.urls)),
    path("login", LoginView.as_view(), name="verify_email"),
    path("access_code", RequestAccessCode.as_view(), name="access_code"),
    path("token", VerifyToken.as_view(), name="verify_token"),
    path("push-token", PushTokenView.as_view(), name="push-token"),
    path("register", RegisterView.as_view(), name="register"),
    path("guest-rsvp", GuestRsvp.as_view(), name="guest-rsvp"),
    path("guest-rsvp/<int:guest_id>", GuestRsvp.as_view(), name="other-guest-rsvp"),
    path("group", GroupView.as_view(), name="group"),
    path("new-guest", GuestAdd.as_view(), name="new-guest"),
    path("profile", GuestView.as_view(), name="profile"),
    path("message", MessageView.as_view(), name="new-message"),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    # path('docs/', include_docs_urls(title='Cami y Aqui Wedding API')),
    path("photos/policy", PhotoUploadPolicy.as_view(), name="photo-policy"),
    path("photos/complete", PhotoUploadComplete.as_view(), name="photo-uploaded"),
    path("news", NewsView.as_view(), name="news-list"),
]
