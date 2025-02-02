from django.urls import path

from core.views import HomePageView, ItemListView, ItemDetailView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("items/", ItemListView.as_view(), name="item_list"),
    path("items/<int:id>", ItemDetailView.as_view(), name="item_detail"),
]
