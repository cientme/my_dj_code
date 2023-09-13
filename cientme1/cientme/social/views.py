from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404
from django.urls import reverse_lazy
from django.views import View
from social.models import Post, Comment
from social.forms import PostForm, CommentForm
from django.views.generic.edit import UpdateView, DeleteView

# module import from account app 
from account.models import Account

# Create your views here.

class AddPostView(View):
    def get(self, request, *args, **kwargs):
        posts = Post.objects.filter(body='body').order_by('-created_on')
        form = PostForm()
        context = {
            'post_list': posts,
            'form':form,

        }
        return render(request, 'social/add_post.html', context)

    def post(self, request, *args, **kwargs):
        posts = Post.objects.filter(body='body').order_by('-created_on')
        form = PostForm(request.POST)
        
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.username = request.user
            new_post.save()
            return redirect('post-list')

        context = {
            'post_list': posts,
            'form':form,

        }
        return render(request, 'social/add_post.html', context)

class PostListView(View):
    def get(self, request, *args, **kwargs):
        posts = Post.objects.all().order_by('-created_on')
        context = {
            'post_list': posts,
            

        }
        return render(request, 'social/post_list.html', context)

class PostDetailView(View):
    def get(self, request, pk, *args, **kwargs):
        account = Account.objects.get()
        post = Post.objects.filter(pk=pk).first()
        comments = Comment.objects.filter(post=post).order_by('-created_on')
        
        if not post:
            return redirect('post-detail')   

        context = {
            'post': post,
            'comments': comments,
            
        }

        return render(request, 'social/post_detail.html', context)

class AddCommentView(View):
    def get(self, request, pk, *args, **kwargs):
        post = Post.objects.get(pk=pk)
        form = CommentForm()

        

        context = {
            'post': post,
            'form': form,
            
        }

        return render(request, 'social/AddComment.html', context)
    def post(self, request, pk, *args, **kwargs):
        post = Post.objects.get(pk=pk)
        form = CommentForm(request.POST)

        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.username = request.user
            new_comment.post = post
            new_comment.save()

        comments = Comment.objects.filter(post=post).order_by('-created_on')

        context = {
            'post': post,
            'form': form,
            'comments': comments,

        }

        return render(request, 'social/post_detail.html', context)


class PostEditView(UpdateView):
    model = Post
    fields = ['body']
    template_name = 'social/post_edit.html'

    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse_lazy('post-detail', kwargs={'pk':pk})

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'social/post_delete.html'
    success_url = reverse_lazy('post-list')


class CommentEditView(UpdateView):
    model = Comment
    fields = ['comment']
    template_name = 'social/comment_edit.html'

    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse_lazy('post-detail', kwargs={'pk':pk})



class CommentDeleteView(DeleteView):
    model = Comment
    template_name = 'social/comment_delete.html'
 
    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse_lazy('post-detail', kwargs={'pk':pk})