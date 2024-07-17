from django.urls import path,include
from . import views

app_name='base'
urlpatterns = [
    path('',views.home,name='home'),
    path('create/',views.user_create_view,name='create'),
    path('register/',views.register_user),
    path('authlogin/',views.auth_login_user),
    path('login/',views.login_user),
    path('logout/',views.logout_user),
    path('base/',views.new,name='base'),
    path('base/<slug:slug>/',views.route,name='routes'),
    path('search/',views.user_search_view,name="search")
    
]
