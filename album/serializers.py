from rest_framework import serializers
from rest_framework.utils import model_meta

from album.models import Executor, Song, Album, AlbumSong


class ExecutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Executor
        fields = "__all__"


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = "__all__"


class AlbumSongSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlbumSong
        fields = ['song', 'order']


class AlbumSerializer(serializers.ModelSerializer):
    album_songs = AlbumSongSerializer(many=True)

    class Meta:
        model = Album
        fields = "__all__"

    def create(self, validated_data):
        album_songs = validated_data['album_songs']
        del validated_data['album_songs']
        album = Album.objects.create(**validated_data)

        # Добавляет песни с проверкой корректности порядковых номеров
        order_list = []
        for album_song in album_songs:
            if not album_song["order"] in order_list:
                AlbumSong.objects.create(album=album, **album_song)
                order_list.append(album_song["order"])
            else:
                raise serializers.ValidationError({"error": "Порядковые номеру у песен не могут повторяться"})
        return album

    def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.executor = validated_data.get("executor", instance.executor)
        instance.year_of_issue = validated_data.get("year_of_issue", instance.year_of_issue)

        album_songs = validated_data['album_songs']
        # Добавляет песни с проверкой корректности порядковых номеров
        order_list = []
        for album_song in album_songs:
            if not album_song["order"] in order_list:
                AlbumSong.objects.get_or_create(album=instance, **album_song)
                order_list.append(album_song["order"])
            else:
                raise serializers.ValidationError({"error": "Порядковые номеру у песен не могут повторяться"})
        instance.save()
        return instance