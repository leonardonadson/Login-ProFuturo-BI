from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from ProBI.forms.AuthForm import LoginForm, RegisterForm
from ProBI.models import Usuario
from django.contrib.auth.decorators import login_required

def login_view(request):
    loginForm = LoginForm()
    message = None

    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        username = request.POST['username']  # Pode ser e-mail ou nome de usuário
        password = request.POST['password']
        loginForm = LoginForm(request.POST)

        if loginForm.is_valid():
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(request.GET.get('next', '/'))
            else:
                message = {'type': 'danger', 'text': 'Credenciais inválidas'}

    context = {
        'form': loginForm,
        'message': message,
        'title': 'Login',
        'button_text': 'Entrar',
        'link_text': 'Registrar',
        'link_href': '/register'
    }

    return render(request, 'auth/auth.html', context)


def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def register_view(request):
    registerForm = RegisterForm()
    message = None

    if request.user.is_staff == False:
        return redirect('/')

    if request.method == 'POST':
        registerForm = RegisterForm(request.POST)
        if registerForm.is_valid():
            user = registerForm.save(commit=False)
            user.set_password(registerForm.cleaned_data['password']) 
            user.save()

        else:
            message = {'type': 'danger', 'text': 'Erro ao criar conta. Verifique os dados.'}

    context = {
        'form': registerForm,
        'message': message,
        'title': 'Registrar',
        'button_text': 'Registrar',
        'link_text': 'Já tem uma conta? Faça login',
        'link_href': '/login'
    }

    return render(request, 'auth/register.html', context)