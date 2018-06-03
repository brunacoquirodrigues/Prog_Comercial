from django.urls import reverse_lazy
from django.views import generic
from core.forms import UserForm

# Create your views here.
class SignUp(generic.CreateView):
    form_class = UserForm
    success_url = reverse_lazy('login')
    template_name = 'registration/registrar.html'