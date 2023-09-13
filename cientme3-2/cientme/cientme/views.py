from django.shortcuts import render
from django.views import View

class Index(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')

# class CommentDeleteMessage(View):
#     def get(self, request, *args, **kwargs):
#         return render(request, 'comment_delete_message.html')