from django.contrib import admin
from rental.models import Carro, Marca, Cor, Informacao, Imagem
from rental.models import Aluguel
from core.models import ProfileUsuario
# Register your models here.

admin.site.register((Carro,Marca,Cor,Informacao,Imagem))
admin.site.register((ProfileUsuario))
admin.site.register((Aluguel))
