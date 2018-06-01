from django.contrib import admin
from rental.models import Carro, Marca, Cor, Informacao, Imagem
from rental.models import Aluguel
from core.models import Usuario
# Register your models here.

admin.site.register((Carro,Marca,Cor,Informacao,Imagem))
admin.site.register((Usuario))
