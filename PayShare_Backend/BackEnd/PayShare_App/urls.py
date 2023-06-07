from . import views
from django.urls import path

urlpatterns = [
    path('register/', views.RegisterUserApiView.as_view(), name='pippo')
]