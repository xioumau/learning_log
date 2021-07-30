from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm


def register(request):
    """Registro de um novo usuário"""
    if request.method != 'POST':
        # Exibe um formulário de registro em branco
        form = UserCreationForm()
        
    else:
        # Processo do formulário completo
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            # Faz o login do usuário e o redireciona para home
            login(request, new_user)
            return redirect('learning_logs:index')
        
        else:
            username_error = form['username'].errors
            password_error = form['password1'].errors
            password_confirmation_error = form['password2'].errors
            context = {'form': form,
                        'username_error': username_error,
                        'password_error': password_error,
                        'password_confirmation_error': password_confirmation_error,}
            
            return render(request, 'registration/register.html', context)
            
    # Exibe um formulário em branco
    context = {'form': form}
    return render(request, 'registration/register.html', context)
