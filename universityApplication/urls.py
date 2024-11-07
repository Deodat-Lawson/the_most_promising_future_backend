from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import PersonalStatusFormViewSet
from . import views

PersonalStatusFormRouter = DefaultRouter()
PersonalStatusFormRouter.register(r'personalStatusForm', PersonalStatusFormViewSet)


urlpatterns = [
  path('', views.handleRequest)
]