from django.urls import path
from .views import CarroListView, SignUp, CarroDetailView



urlpatterns = [
    path('registrar/', SignUp.as_view(), name='signup'),
    path('<int:pk>', CarroDetailView.as_view(), name='carro-detail'),
]