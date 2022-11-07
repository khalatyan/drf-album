from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APISimpleTestCase, APITransactionTestCase
from rest_framework.test import APIRequestFactory

from album.models import Executor, Song, AlbumSong, Album
from album.factories import ExecutorFactory, SongFactory, AlbumFactory
from album.views import ExecutorViewSet, AlbumViewSet, SongViewSet


class TestCaseForCity(APITestCase):

    def test_get_executor_request_factory(self):
        executor = ExecutorFactory(name="Test")
        request_factory = APIRequestFactory()
        request = request_factory.get("/api/v1/executor/")
        executor_view = ExecutorViewSet.as_view({"get": "list"})
        response = executor_view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_executor_request_factory(self):
        request_factory = APIRequestFactory()
        request = request_factory.post(
            "/api/executor/", {"name": "Test"}, format="json"
        )
        executor_view = ExecutorViewSet.as_view({"post": "create"})
        response = executor_view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)