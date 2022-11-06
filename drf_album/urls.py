from django.contrib import admin
from django.urls import path, include

from rest_framework import routers

from album.views import ExecutorViewSet, SongViewSet, AlbumViewSet

router = routers.SimpleRouter()
router.register(r'executor', ExecutorViewSet)
router.register(r'song', SongViewSet)
router.register(r'album', AlbumViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
]
