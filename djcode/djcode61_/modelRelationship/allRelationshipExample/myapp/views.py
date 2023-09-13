from django.shortcuts import render
from myapp.models import Page, Post, Song, User

# Create your views here.

def home(request):
    return render(request, 'myapp/home.html')


def show_user_data(request):
    data1 = User.objects.all()
    data2 = User.objects.filter(email='hemibora@gmail.com')
    data3 = User.objects.filter(mypage__page_cat='Yoga')
    data4 = User.objects.filter(post__post_publish_date='2022-06-20')
    data5 = User.objects.filter(song__song_duration=7)
    context = {
        'data1': data1,
        'data2': data2,
        'data3': data3,
        'data4': data4,
        'data5': data5,
    }
    return render(request, 'myapp/user.html', context)


def show_page_data(request):
    data1 = Page.objects.all()
    data2 = Page.objects.filter(page_cat='Yoga')
    data3 = Page.objects.filter(user__email='hemibora@gmail.com')

    context = {
        'data1': data1,
        'data2': data2,
        'data3': data3,
    }
    return render(request, 'myapp/page.html', context)


def show_post_data(request):
    data1 = Post.objects.all()
    data2 = Post.objects.filter(post_publish_date='2022-06-20')
    data3 = Post.objects.filter(user__username='Hemi')

    context = {
        'data1': data1,
        'data2': data2,
        'data3': data3,
    }
    return render(request, 'myapp/post.html', context)


def show_song_data(request):
    data1 = Song.objects.all()
    data2 = Song.objects.filter(song_duration=7)
    data3 = Song.objects.filter(user__username='Hemi')

    context = {
        'data1': data1,
        'data2': data2,
        'data3': data3,
    }
    return render(request, 'myapp/song.html', context)
