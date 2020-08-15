from django.shortcuts import render
from .models import User


def users(request):
    users_list = User.objects.all()
    context = {
        'title': 'Управление переводчиками',
        'users': users_list
    }
    return render(request, 'users/view.html', context)


