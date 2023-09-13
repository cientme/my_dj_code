from xml.dom.minidom import Document
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

# Here viws file import from cientme project.
from .views import Index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Index.as_view(), name='index'),
    # path('comment-delete-message', CommentDeleteMessage.as_view(), name='comment-delete-message'),
    path('accounts/', include('accounts.urls')),
    path('social/', include('social.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)