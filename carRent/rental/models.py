from django.db import models
from datetime import datetime as tempo
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Carro(models.Model):
    """Model definition for Carro."""
    nome = models.CharField(max_length=30, blank=False, null=False)
    ano  = models.PositiveIntegerField(
            validators=[
                MinValueValidator(1900), 
                MaxValueValidator(tempo.now().year)],
            help_text="Use the following format: <YYYY>")

    alugado = models.BooleanField(blank=False, null=False)

    class Meta:
        """Meta definition for Carro."""
        verbose_name = 'Carro'
        verbose_name_plural = 'Carros'

    def __str__(self):
        """Unicode representation of Carro."""
        return "{} {}".format(self.nome, self.ano)

    # TODO: Define custom methods here

class Cor(models.Model):
    """Model definition for Cor."""
    carro = models.OneToOneField(Carro, on_delete=models.CASCADE, primary_key = True)
    cor = models.CharField(max_length=30, blank=False, null=False)

    class Meta:
        """Meta definition for Cor."""

        verbose_name = 'Cor'
        verbose_name_plural = 'Cores'

    def __str__(self):
        """Unicode representation of Cor."""
        return "cor:%s do carro %s" %s(self.cor, self.carro.nome)

class Marca(models.Model):
    """Model definition for Marca."""
    carro = models.OneToOneField(Carro, on_delete=models.CASCADE, primary_key = True)
    marca = models.CharField(max_length=30, blank=False, null=False)

    class Meta:
        """Meta definition for Marca."""

        verbose_name = 'Marca'
        verbose_name_plural = 'Marcas'

    def __str__(self):
        """Unicode representation of Marca."""
        return "carro: %s de marca: %s" %(self.carro.nome, self.marca)

class Informacao(models.Model):
    """Model definition for Informacao."""
    carro = models.OneToOneField(Carro, on_delete=models.CASCADE, primary_key=True)
    tempo_de_uso = models.PositiveIntegerField(blank=False, null=False)
    km_rodados = models.PositiveIntegerField(blank=False, null=False)
    descricao_carro = models.TextField(blank=False, null=False, max_length=300)

    class Meta:
        """Meta definition for Informacao."""

        verbose_name = 'Informação'
        verbose_name_plural = 'Informações'

    def __str__(self):
        """Unicode representation of Informacao."""
        pass

class Aluguel(models.Model):
    """Model definition for Aluguel."""
    # usuario
    carro = models.OneToOneField(Carro, on_delete=models.CASCADE, primary_key = True)
    data_inicio = models.DateTimeField(auto_now_add=True)
    data_fim = models.DateTimeField(auto_now=True)
    km_rodadps = models.PositiveIntegerField()

    class Meta:
        """Meta definition for Aluguel."""

        verbose_name = 'Aluguel'
        verbose_name_plural = 'Alugueis'

    def __str__(self):
        """Unicode representation of Aluguel."""
        pass
