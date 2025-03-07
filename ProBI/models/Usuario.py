from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, Group, Permission
from django.db import models
import uuid

class UsuarioManager(BaseUserManager):
    def create_user(self, email, nome, telefone, nomedeusuario, password=None):
        if not email:
            raise ValueError('O usuário deve ter um email válido')

        if not nomedeusuario:
            raise ValueError('O usuário deve ter um nome de usuário')

        user = self.model(
            email=self.normalize_email(email), 
            nome=nome, 
            telefone=telefone, 
            nomedeusuario=nomedeusuario
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, nome, telefone, nomedeusuario, password):
        user = self.create_user(email, nome, telefone, nomedeusuario, password)
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class Usuario(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nome = models.CharField(max_length=100, null=False)
    nomedeusuario = models.CharField(unique=True, max_length=100, null=False)
    email = models.EmailField(unique=True, null=False)
    telefone = models.CharField(max_length=20, null=False)

    is_active = models.BooleanField(default=True) 
    is_staff = models.BooleanField(default=False)  

    groups = models.ManyToManyField(Group, related_name="usuario_groups", blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name="usuario_permissions", blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nome', 'telefone', 'nomedeusuario']

    objects = UsuarioManager()

    def __str__(self):
        return f'{self.id} - {self.nome}'
