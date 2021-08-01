from django.shortcuts import render, get_object_or_404
from .models import GamePost, AboutUs, ContactUs
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def games_post_list(request):
    object_list = GamePost.published.all()
    paginator = Paginator(object_list, 4)
    page = request.GET.get('page')
    try:
        games_post = paginator.page(page)
    except PageNotAnInteger:
        games_post = paginator.page(1)
    except EmptyPage:
        games_post = paginator.page(paginator.num_pages)
    return render(request,
                  'IndigoGamesStudio/post/index.html',
                  {'page': page,
                   'games_post': games_post})

def games_post_detail(request, year, month, day, post):
    post = get_object_or_404(GamePost, slug=post,
                             status = 'published',
                             publish__year = year,
                             publish__month = month,
                             publish__day = day)
    return render(request,
                  'IndigoGamesStudio/post/games_detail.html',
                  {'post': post})

def about_us_list(request):
    person_list = AboutUs.objects.all()
    return render(request,
                  'IndigoGamesStudio/post/about_us.html',
                  {'person_list': person_list})

def contact_us_list(request):
    social_media_list = ContactUs.objects.all()
    return render(request,
                  'IndigoGamesStudio/post/contact.html',
                  {'social_media_list': social_media_list})