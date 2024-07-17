from django.urls import path
from .views import (
    BlogPostCreateView,
    BlogPostRetrieveUpdateDestroy
)

urlpatterns = [
    path('blogposts/',BlogPostCreateView.as_view(),name='create'),
    path('blogposts/<int:pk>/',BlogPostRetrieveUpdateDestroy.as_view(),name='modify')
]
