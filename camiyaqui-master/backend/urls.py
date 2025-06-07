from django.contrib.admin.views.decorators import staff_member_required
from django.urls import path

from backend.views import (
    GuestList,
    MessageList,
    MessageDetail,
    BackendLogin,
    ProfileDetails,
    ProfileEdit,
    MessagesFromGuestList,
    MessageCreate,
    MessageSend,
    GuestApprove,
    MessagePreview,
    MessageUpdate,
    UploadContactsView,
    MessageSendTest,
    GuestDetails,
    ExportGuests,
    ListNewsView,
    CreateNewsView,
)

urlpatterns = [
    path("", BackendLogin.as_view(), name="backend-login"),
    path(
        "guest-list",
        staff_member_required(GuestList.as_view()),
        name="bcknd-guest-list",
    ),
    path(
        "guest-list/guests.json",
        staff_member_required(ExportGuests.as_view()),
        name="export-guests",
    ),
    path(
        "profile/<int:pk>",
        staff_member_required(ProfileDetails.as_view()),
        name="profile",
    ),
    path(
        "profile/<int:pk>/edit",
        staff_member_required(ProfileEdit.as_view()),
        name="profile-edit",
    ),
    path("guest/<int:pk>", staff_member_required(GuestDetails.as_view()), name="guest"),
    path(
        "guest/<int:pk>/approve",
        staff_member_required(GuestApprove.as_view()),
        name="guest-approve",
    ),
    path(
        "message-list",
        staff_member_required(MessageList.as_view()),
        name="message-list",
    ),
    path(
        "message/<int:pk>",
        staff_member_required(MessageDetail.as_view()),
        name="message-detail",
    ),
    path(
        "message/send/<int:pk>",
        staff_member_required(MessageSend.as_view()),
        name="message-send",
    ),
    path(
        "message/send/test/<int:pk>",
        staff_member_required(MessageSendTest.as_view()),
        name="send-to",
    ),
    path(
        "message/preview/<int:pk>",
        staff_member_required(MessagePreview.as_view()),
        name="message-preview",
    ),
    path(
        "message/edit/<int:pk>",
        staff_member_required(MessageUpdate.as_view()),
        name="message-edit",
    ),
    path(
        "message-new",
        staff_member_required(MessageCreate.as_view()),
        name="message-new",
    ),
    path(
        "upload-contacts",
        staff_member_required(UploadContactsView.as_view()),
        name="upload-contacts",
    ),
    path(
        "contacts",
        staff_member_required(MessagesFromGuestList.as_view()),
        name="guest-messages",
    ),
    path("news", staff_member_required(ListNewsView.as_view()), name="list-news"),
    path(
        "news/add", staff_member_required(CreateNewsView.as_view()), name="create-news"
    ),
]
