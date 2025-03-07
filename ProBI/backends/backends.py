from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.hashers import check_password
from ProBI.models import Usuario

class UsuarioBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        """
        Permite autenticação por e-mail ou nome de usuário.
        """
        try:
            user = Usuario.objects.get(email=username)  
        except Usuario.DoesNotExist:
            try:
                user = Usuario.objects.get(nomedeusuario=username) 
            except Usuario.DoesNotExist:
                return None

        if user and check_password(password, user.password):
            return user
        
        return None

    def get_user(self, user_id):
        try:
            return Usuario.objects.get(pk=user_id)
        except Usuario.DoesNotExist:
            return None
