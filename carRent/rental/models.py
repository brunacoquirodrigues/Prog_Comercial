from django.db import models
from datetime import datetime as tempo
from django.core.validators import MinValueValidator, MaxValueValidator
from core.models import Usuario

# Create your models here.

class Cor(models.Model):
    cor = models.CharField(max_length=30, blank=False, null=False)

    class Meta:
        verbose_name = 'Cor'
        verbose_name_plural = 'Cores'

    def __str__(self):
        return "%s" %(self.cor)

class Marca(models.Model):
    marca = models.CharField(max_length=30, blank=False, null=False)

    class Meta:
        verbose_name = 'Marca'
        verbose_name_plural = 'Marcas'

    def __str__(self):
        return "%s" %(self.marca)

class Carro(models.Model):
    modelo = models.CharField(max_length=30, blank=False, null=False)
    ano  = models.PositiveIntegerField(
            validators=[
                MinValueValidator(1900), 
                MaxValueValidator(tempo.now().year)],
            help_text="Use o formato: AAAA")
    cor_carro_fk = models.ForeignKey(Cor, on_delete=models.CASCADE)
    marca_carro_fk = models.ForeignKey(Marca, on_delete=models.CASCADE, default=0)
    #placa unique
    alugado = models.BooleanField(blank=False, null=False)

    class Meta:
        verbose_name = 'Carro'
        verbose_name_plural = 'Carros'

    def __str__(self):
        return "Marca: %s -> Modelo: %s -> Ano: %s -> Alugado:%s" %(self.marca_carro_fk.marca, self.modelo, self.ano, self.alugado)

    # TODO: Define custom methods here


class Informacao(models.Model):
    info_carro = models.OneToOneField(Carro, on_delete=models.CASCADE, primary_key=True)
    tempo_de_uso = models.PositiveIntegerField(blank=False, null=False)
    km_rodados = models.PositiveIntegerField(blank=False, null=False)
    descricao_carro = models.TextField(blank=False, null=False, max_length=300)

    class Meta:
        verbose_name = 'Informação'
        verbose_name_plural = 'Informações'

    def __str__(self):
        pass

class Aluguel(models.Model):
    """Model definition for Aluguel."""
    # usuario
    usuario_fk = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='aluguel')
    aluguel_carro = models.OneToOneField(Carro, on_delete=models.CASCADE, primary_key = True)
    data_inicio = models.DateTimeField(auto_now_add=True)
    data_fim = models.DateTimeField(auto_now=True)
    km_rodadps = models.PositiveIntegerField()

    class Meta:
        """Meta definition for Aluguel."""

        verbose_name = 'Aluguel'
        verbose_name_plural = 'Alugueis'

    def __str__(self):
        """Unicode representation of Aluguel."""
        return "carro: %s alugado em: %s ate: %s" %(self.aluguel_carro.modelo, self.data_inicio, self.data_fim)

class Imagem(models.Model):
    """Model definition for Imagem."""

    carro_imagem = models.ForeignKey(Carro, on_delete=models.CASCADE, related_name='imagens')
    #imagem_file

    class Meta:
        """Meta definition for Imagem."""

        verbose_name = 'Imagem'
        verbose_name_plural = 'Imagens'

    def __str__(self):
        """Unicode representation of Imagem."""
        return "Imagem do carro: %s" %(self.carro_imagem.primary_key)
