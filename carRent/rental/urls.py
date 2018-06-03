from django.urls import path
from . import views


urlpatterns = [
    path('registrar/', views.SignUp.as_view(), name='signup'),
]