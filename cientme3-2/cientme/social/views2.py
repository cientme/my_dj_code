from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Q 
from social.models import (
    Post, Comment, Profile
    )

from .forms import (
    PostForm,
    CommentForm,
    )

from django.views.generic import UpdateView, DeleteView
import random
# x = 
n = random.randint(1, 4)

# Add post here.
class PostAddView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            form = PostForm()

            context = {
                'form':form,
            }

            return render(request, 'social/post_add.html', context)
        else:
            return redirect('login')

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            form = PostForm(request.POST)
            if form.is_valid():
               new_post =  form.save(commit=False)
               new_post.author = request.user
               new_post.save()
               return redirect('post-list')
          
            context = {
                
                'form':form,
            }

            return render(request, 'social/post_add.html', context)
        else:
            return redirect('login')



# Post List.
class PostListView(LoginRequiredMixin ,View):
    def get(self, request, pk=n, *args, **kwargs):
        if request.user.is_authenticated:
            logged_in_user = request.user
            posts = Post.objects.filter(
                author__profile__followers__in=[logged_in_user.id]
            ).order_by('-created_on')
            post = Post.objects.get(pk=pk)
            form = CommentForm()

            comments = Comment.objects.filter(post=post).order_by('-created_on')

            

            context = {
                'posts':posts,
                'form': form,
                'comments': comments,
            }

            return render(request, 'social/post_list.html', context)
        else:
            return redirect('login')
    
    def post(self, request, pk=n, *args, **kwargs):
        if request.user.is_authenticated:
            pk = self.kwargs.get('pk')
            post = Post.objects.get(pk=pk)
            form = CommentForm(request.POST)
            if form.is_valid():
                new_comment =  form.save(commit=False)
                new_comment.author = request.user
                new_comment.post = post
                new_comment.save()
                return redirect('post-list')

            comments = Comment.objects.filter(post=post).order_by('-created_on')


            context = {
                'post': post,
                'form': form,
                'comments':comments,

            }

            return render(request, 'social/post_list.html', context)

        else:
            return redirect('login')



# Post detail.
class PostDetailView(LoginRequiredMixin ,View):
    def get(self, request, pk, *args, **kwargs):
        if request.user.is_authenticated:
            post = Post.objects.get(pk=pk)
            form = CommentForm()
            comments = Comment.objects.filter(post=post).order_by('-created_on')

            context = {
                'post': post,
                'form': form,
                'comments':comments,
            }

            return render(request, 'social/post_detail.html', context)

        else:
            return redirect('login')

    def post(self, request, pk, *args, **kwargs):
        if request.user.is_authenticated:
            post = Post.objects.get(pk=pk)
            form = CommentForm(request.POST)
            if form.is_valid():
                new_comment =  form.save(commit=False)
                new_comment.author = request.user
                new_comment.post = post
                new_comment.save()
                return redirect('post-detail', pk=pk)

            

                
            comments = Comment.objects.filter(post=post).order_by('-created_on')

            context = {
                'post': post,
                'form': form,
                'comments':comments,
            }

            return render(request, 'social/post_detail.html', context)

        else:
            return redirect('login')


# Comment reply here.
class CommentReplyView(LoginRequiredMixin, View):
    def post(self, request, post_pk, pk, *args, **kwargs):
        post = Post.objects.get(pk=post_pk)
        parent_comment = Comment.objects.get(pk=pk)
        form = CommentForm(request.POST)

        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.author = request.user
            new_comment.post = post
            new_comment.parent = parent_comment
            new_comment.save()

        return redirect('post-detail', pk=post_pk)


# post edit here.
class PostEditView(LoginRequiredMixin, UserPassesTestMixin ,UpdateView):
    model = Post
    fields = ('caption',)
    template_name = 'social/post_edit.html'

    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse_lazy('post-detail', kwargs={'pk':pk})


    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author


# post Delete
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'social/post_delete.html'

    def get_success_url(self):
        return reverse_lazy('post-list')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author


# Comment delete.
class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = 'social/comment_delete.html'

    def get_success_url(self):
        pk = self.kwargs['post_pk']
        return reverse_lazy('post-detail', kwargs={'pk':pk})

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author


#  User Profile
class ProfileView(View):
    def get(self, request, pk, *args, **kwargs):
        profile = Profile.objects.get(pk=pk)
        user = profile.user
        posts = Post.objects.filter(author=user).order_by('-created_on')
    
        post = Profile.objects.get(pk=pk)
        form = CommentForm()
        comments = Comment.objects.filter(author=user).order_by('-created_on')

        followers = profile.followers.all()

        if len(followers) == 0:
            is_following = False

        for follower in followers:
            if follower == request.user:
                is_following = True
                break
            else:
                is_following = False

        number_of_followers = len(followers)

        context = {
            'profile': profile,
            'user': user,
            'posts': posts,
            'number_of_followers': number_of_followers,
            'is_following': is_following,
            # comments items
            'post': post,
            'form': form,
            'comments':comments,
            
        }

        return render(request, 'social/profile.html', context)

    def post(self, request, pk, *args, **kwargs):
        if request.user.is_authenticated:
            profile = Profile.objects.get(pk=pk)
            user = profile.user
            post_instance = get_object_or_404(Profile, id=profile.id)

            form = CommentForm(request.POST)
            if form.is_valid:
                new_comment =  form.save(commit=False)
                new_comment.user = request.user
                new_comment.profile = post_instance
                new_comment.save()
                return redirect('profile', pk=pk)

                
            comments = Comment.objects.filter(profile=profile).order_by('-created_on')

            context = {
                'profile': profile,
                'user':user,
                'form': form,
                'comments':comments,
            }
        return render(request, 'social/profile.html', context)


# Eddit profile.
class ProfileEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Profile
    fields = ('name', 'bio', 'dob', 'location','picture')
    template_name = 'social/profile_edit.html'

    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse_lazy('profile', kwargs={'pk':pk})

    def test_func(self):
        profile = self.get_object()
        return self.request.user == profile.user


# Add followers.
class AddFollowers(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        profile = Profile.objects.get(pk=pk)
        profile.followers.add(request.user)
        return redirect('profile', pk=profile.pk)


# Remove followers.
class RemoveFollowers(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        profile = Profile.objects.get(pk=pk)
        profile.followers.remove(request.user)
        return redirect('profile', pk=profile.pk)


# Add like post.
class AddLike(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        post = Post.objects.get(pk=pk)

        is_slike = False

        for slike in post.slikes.all():
            if slike == request.user:
                is_slike = True
                break

        if is_slike:
            post.slikes.remove(request.user)

        is_like = False

        for like in post.likes.all():
            if like == request.user:
                is_like = True
                break
            

        if not is_like:
            post.likes.add(request.user)

        if is_like:
            post.likes.remove(request.user)

        next = request.POST.get('next', '/')
        return HttpResponseRedirect(next)

# Add super like post.
class AddSuperLike(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        post = Post.objects.get(pk=pk)

        is_like = False

        for like in post.likes.all():
            if like == request.user:
                is_like = True
                break

        if is_like:
            post.likes.remove(request.user)

        is_slike = False

        for slike in post.slikes.all():
            if slike == request.user:
                is_slike = True
                break
            

        if not is_slike:
            post.slikes.add(request.user)

        if is_slike:
            post.slikes.remove(request.user)
        

        next = request.POST.get('next', '/')
        return HttpResponseRedirect(next)


# Add comment like.
class AddCommentLike(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        comment = Comment.objects.get(pk=pk)

        is_slike = False

        for slike in comment.slikes.all():
            if slike == request.user:
                is_slike = True
                break

        if is_slike:
            comment.slikes.remove(request.user)

        is_like = False

        for like in comment.likes.all():
            if like == request.user:
                is_like = True
                break
            

        if not is_like:
            comment.likes.add(request.user)

        if is_like:
            comment.likes.remove(request.user)

        next = request.POST.get('next', '/')
        return HttpResponseRedirect(next)
       

# Add comment super like.
class AddCommentSuperLike(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        comment = Comment.objects.get(pk=pk)

        is_like = False

        for like in comment.likes.all():
            if like == request.user:
                is_like = True
                break

        if is_like:
            comment.likes.remove(request.user)

        is_slike = False

        for slike in comment.slikes.all():
            if slike == request.user:
                is_slike = True
                break
            

        if not is_slike:
            comment.slikes.add(request.user)

        if is_slike:
            comment.slikes.remove(request.user)
        

        next = request.POST.get('next', '/')
        return HttpResponseRedirect(next)

class SearchView(View):
    def get(self, request, *args, **kwargs):
        query = self.request.GET.get('query')
        profile_list = Profile.objects.filter(
            Q(user__username__icontains=query)

        )

        context = {
            'profile_list': profile_list,
        }
    
        return render(request, 'social/search.html', context)


class ListFollowers(View):
    def get(self, request, pk, *args, **kwargs):
        profile = Profile.objects.get(pk=pk)
        followers = profile.followers.all()

        context = {
            'profile': profile,
            'followers': followers,
        }

        return render(request, 'social/followers_list.html', context)