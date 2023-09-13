from django.contrib import admin
from .models import Post,  Profile, Comment

admin.site.register(Post)
admin.site.register(Profile)
admin.site.register(Comment)

# @admin.register(Post)
# class PostAdmin(admin.ModelAdmin):
#     model = Post
#     fields = ('id', 'autghor', 'created_on')


# @admin.register(Profile)
# class ProfileAdmin(admin.ModelAdmin):
#     model = Profile
#     fields = ('id', 'user')

# @admin.register(Comment)
# class CommentAdmin(admin.ModelAdmin):
#     model = Profile
#     fields = ('cooment', 'author')