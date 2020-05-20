from django.urls import path

from . import views

urlpatterns = [
    path('ManagePage/login/', views.login),
]