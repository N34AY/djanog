from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from django.shortcuts import redirect


def main(request):
    if request.user.is_authenticated:
        context = {
            'user': request.user
        }
        print(context)
        return render(request, 'main/main.html', context)
    else:
        return redirect('/login')


def user_login(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == 'POST':
            form = LoginForm(request.POST)
            if form.is_valid():
                cd = form.cleaned_data
                user = authenticate(username=cd['username'], password=cd['password'])
                if user is not None:
                    if user.is_active:
                        login(request, user)
                        return render(request, 'main/main.html')
                    else:
                        context = {
                            'status': False,
                            'message': 'Ваш аккаунт неактивен',
                            'form': LoginForm
                        }
                        return render(request, 'login/login.html', context)
                else:
                    context = {
                        'status': False,
                        'message': 'Неправильные почта или пароль',
                        'form': LoginForm
                    }
                    return render(request, 'login/login.html', context)
        else:
            form = LoginForm()
        return render(request, 'login/login.html', {'form': form})


def user_logout(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        return redirect('/')

