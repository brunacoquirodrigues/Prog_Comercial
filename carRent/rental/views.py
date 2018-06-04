from django.urls import reverse_lazy
from django.views import generic
from core.forms import UserForm
from .models import Carro, Informacao

# Create your views here.
class SignUp(generic.CreateView):
    form_class = UserForm
    success_url = reverse_lazy('login')
    template_name = 'registration/registrar.html'

class CarroListView(generic.ListView):
    model = Carro
    template_name = "homepage.html"

class CarroDetailView(generic.DetailView):
    model = Informacao
    template_name = "detail.html"

# TODO: FAZER O ALUGUEL