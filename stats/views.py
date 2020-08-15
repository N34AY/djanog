from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect
from .models import Stats
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def stats(request):
    if not request.user.is_authenticated:
        return redirect('/login')
    else:
        stats_list = Stats.objects.all()
        page = request.GET.get('page', 1)
        paginator = Paginator(stats_list, 100)
        try:
            stats_list = paginator.page(page)
        except PageNotAnInteger:
            stats_list = paginator.page(1)
        except EmptyPage:
            stats_list = paginator.page(paginator.num_pages)
        context = {
            'stats_list': stats_list,
        }
        return render(request, 'stats/stats.html', context)


def users(request):
    return render(request, 'stats/stats.html')
