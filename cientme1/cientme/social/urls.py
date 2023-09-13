from django.urls import path
from . import views
from .views import PostListView, AddPostView, PostDetailView, AddCommentView, PostEditView, PostDeleteView, CommentEditView ,CommentDeleteView


urlpatterns = [
    path('', PostListView.as_view(), name='post-list'),
    path('post/add', AddPostView.as_view(), name='add-post'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post-detail'),
    path('post/edit/<int:pk>', PostEditView.as_view(), name='post-edit'),
    path('post/detele/<int:pk>', PostDeleteView.as_view(), name='post-delete'),
    path('post/comment/<int:pk>', AddCommentView.as_view(), name='add-comment'),
    path('post/<int:post_pk>/comment/edit/<int:pk>', CommentEditView.as_view(), name='comment-edit'),
    path('post/<int:post_pk>/comment/delete/<int:pk>', CommentDeleteView.as_view(), name='comment-delete'),
    
   
]