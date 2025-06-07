from django.urls import path
from django.views.generic import TemplateView

from photos.views import (
    FilePolicyAPI,
    FileUploadCompleteHandler,
    GalleryList,
    GalleryView,
    AlbumView,
    AlbumNew,
    AlbumAdd,
)

urlpatterns = [
    path("policy", FilePolicyAPI.as_view(), name="upload-policy"),
    path(
        "", TemplateView.as_view(template_name="photos/upload.html"), name="upload-home"
    ),
    path("complete", FileUploadCompleteHandler.as_view(), name="upload-complete"),
    path("galleries", GalleryList.as_view(), name="galleries"),
    path("gallery/<int:pk>", GalleryView.as_view(), name="gallery"),
    path("album/new", AlbumNew.as_view(), name="album-new"),
    path("album/<int:pk>", AlbumView.as_view(), name="album"),
    path("album/<int:pk>/add", AlbumAdd.as_view(), name="album-add"),
]
