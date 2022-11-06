from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from drf_yasg import openapi
from drf_yasg.views import get_schema_view as swagger_get_schema_view

from album.views import ExecutorViewSet, SongViewSet, AlbumViewSet

schema_view = swagger_get_schema_view(
    openapi.Info(
        title="Posts API",
        default_version='1.0.0',
        description="API documentation of App",
    ),
    public=True,
)

router = routers.SimpleRouter()
router.register(r'executor', ExecutorViewSet)
router.register(r'song', SongViewSet)
router.register(r'album', AlbumViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('api/v1/',
         include([
             path('', include(router.urls)),
             path('docs', schema_view.with_ui('swagger', cache_timeout=0), name="swagger-schema"),
         ])
    ),
]
