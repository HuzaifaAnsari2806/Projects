from django.urls import path
from . views import (
    create_view,
    detail_view,
    update_view,
    list_view,
    login_user,
    delete_view,
    recipe_ingredient_delete_view,
    recipe_ingredient_image_view
    )

app_name='recipes'
urlpatterns = [
    path('login/',login_user),
    path('list/',list_view,name='list'),
    path('',create_view,name='create'),
    path('<int:id>/edit/',update_view,name='update'),
    path('<int:id>/delete/',delete_view,name='delete'),
    path('<int:parent_id>/ingredient/<int:id>/delete/',recipe_ingredient_delete_view,name='ingredient-delete'),
    path('<int:parent_id>/image-upload/',recipe_ingredient_image_view,name='ingredient-image'),
    path('<int:id>/',detail_view,name='detail')
]
