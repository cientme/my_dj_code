from django.shortcuts import render
from .models import Post
from django.core.paginator import Paginator

# Create your views here.

def post_list(request):
    all_post = Post.objects.all().order_by('id')
    paginator = Paginator(all_post, 3, orphans=1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    print('All Post=', all_post)
    print('Paginator=', paginator)
    print('Page Number=', page_number)
    print('page object=', page_obj)
    context = {'page_obj': page_obj}
    return render(request, 'blog/home.html', context)