import factory

from album.models import Executor, Song, AlbumSong, Album


class ExecutorFactory(factory.Factory):
    class Meta:
        model = Executor


class SongFactory(factory.Factory):
    class Meta:
        model = Song


class AlbumFactory(factory.Factory):
    class Meta:
        model = Album
