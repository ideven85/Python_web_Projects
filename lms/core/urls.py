from django.urls import path
from . import views

app_name = "core"
urlpatterns = [
    path("", views.post_list, name="post_list"),
    path("post/<int:id>/", views.post_detail, name="post_detail"),
]
