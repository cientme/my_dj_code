from django.urls import path
from .views import (
    PostListView, PostAddView, PostDetailView, PostEditView,
    PostDeleteView, CommentDeleteView, ProfileView, ProfileEditView, AddFollowers, RemoveFollowers, AddLike,
    AddSuperLike, SearchView, ListFollowers, AddCommentLike, AddCommentSuperLike, CommentReplyView
)
urlpatterns = [
    path('post-list/', PostListView.as_view(), name='post-list'),
    path('post-list/<int:pk>/like/', AddLike.as_view(), name='like'),
    path('post-list/<int:pk>/slike/', AddSuperLike.as_view(), name='slike'),
    path('post-list/<int:post_pk>/comment/<int:pk>/like/', AddCommentLike.as_view(), name="comment-like"),
    path('post-list/<int:post_pk>/comment/<int:pk>/slike/', AddCommentSuperLike.as_view(), name="comment-slike"),
    path('post/<int:post_pk>/comment/<int:pk>/reply', CommentReplyView.as_view(), name='comment-reply'),
    path('post-add/', PostAddView.as_view(), name='post-add'),
    path('post/detail/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/edit/<int:pk>/', PostEditView.as_view(), name='post-edit'),
    path('post/delete/<int:pk>/', PostDeleteView.as_view(), name='post-delete'),
    path('post/<int:post_pk>/comment/delete/<int:pk>/', CommentDeleteView.as_view(), name='comment-delete'),
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),
    path('profile/edit/<int:pk>/', ProfileEditView.as_view(), name='profile-edit'),
    path('profile/<int:pk>/followers/', ListFollowers.as_view(), name='list-followers'),
    path('profile/<int:pk>/followers/add/', AddFollowers.as_view(), name='add-follower'),
    path('profile/<int:pk>/followers/remove/', RemoveFollowers.as_view(), name='remove-follower'),
    path('search/', SearchView.as_view(), name='profile-search'),
]
