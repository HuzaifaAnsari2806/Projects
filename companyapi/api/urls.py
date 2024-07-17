from django .urls import path,include
from rest_framework import routers
from .views import (
    CompanyViewSet,
    EmployeeViewSet,
    formapi
)

router=routers.DefaultRouter()
router.register(r'companies',CompanyViewSet)
router.register(r'emp',EmployeeViewSet)

urlpatterns = [
    path("create/", formapi, name="createform")
]


urlpatterns += router.urls
