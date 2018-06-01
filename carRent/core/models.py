from django.db import models
from django.contrib.auth.models import User
# Create your models here.
'''
    APP pra trabalhar com os Usuarios
'''
SEXO = (
        (u'M', u'Masculino'),
        (u'F', u'Feminino'),
)

class Usuario(models.Model):
    """Model definition for Usuario."""

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cpf = models.CharField(max_length=11, null=False, unique=True)
    sexo = models.CharField(max_length=1, null=False, choices=SEXO)
    #profile_pic

    class Meta:
        """Meta definition for Usuario."""

        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    def __str__(self):
        """Unicode representation of Usuario."""
        return 
