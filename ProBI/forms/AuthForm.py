from django import forms
from ProBI.models import Usuario

class LoginForm(forms.Form):
    username = forms.CharField(label="E-mail ou Nome de Usuário")
    password = forms.CharField(widget=forms.PasswordInput, label="Senha")

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label="Senha")
    password_confirm = forms.CharField(widget=forms.PasswordInput, label="Confirmar Senha")

    class Meta:
        model = Usuario
        fields = ['nome', 'nomedeusuario', 'email', 'telefone', 'password', 'is_staff']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")

        if password and password_confirm and password != password_confirm:
            self.add_error('password_confirm', "As senhas não coincidem.")

        return cleaned_data