from django.urls import path,include
from rest_framework.routers import DefaultRouter

from .views import (
    BlogMixinView,
    BlogRetrieveUpdateDestroyMixinView,
    formapi,
    formupdateapi,
    Blogcreateview,
    formimageapi,
    ImageUpdateDeleteView,
    StatsView,
)


urlpatterns = [
    path("", BlogMixinView.as_view(), name="list"),
    path("stats/", StatsView.as_view(), name="stats"),
    path('create-blog/',Blogcreateview.as_view(),name="create-view"),
    path("create/", formapi, name="create"),
    path("upload-image/",formimageapi, name="image-upload"),
    path("update/<int:pk>/", formupdateapi, name="update"),
    path("rud/<int:pk>/", BlogRetrieveUpdateDestroyMixinView.as_view(), name="rud"),
    path("<int:parent_id>/imagerud/<int:id>/", ImageUpdateDeleteView),
]
