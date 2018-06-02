from django.db import models
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
'''
    APP pra trabalhar com os Usuarios
'''
SEXO = (
        (u'M', u'Masculino'),
        (u'F', u'Feminino'),
)

class ProfileUsuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cpf = models.CharField(max_length=11, null=False, unique=True)
    sexo = models.CharField(max_length=1, null=False, choices=SEXO)
    profile_pic = models.ImageField(upload_to="profile_pic/", blank=True, null=True)

    class Meta:
        verbose_name = 'Perfil Usuário'
        verbose_name_plural = 'Perfis Usuários'

    def __str__(self):
        return "%s %s" %(self.user.first_name, self.user.last_name )
