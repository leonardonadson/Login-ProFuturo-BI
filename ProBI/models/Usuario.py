from ProBI.models import *

class Usuario(models.Model):
    id = models.AutoField(primary_key=True)  # ID autoincrementável
    nome = models.CharField(null=False, max_length=100)
    email = models.EmailField(null=False, unique=True)
    telefone = models.CharField(null=False, max_length=20)
    criado_em = models.DateTimeField(auto_now_add=True)
    alterado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{} - {}'.format(self.id, self.nome)
