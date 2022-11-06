from django.db import transaction
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
        fields = "__all__"


class AlbumSerializer(serializers.ModelSerializer):
    album_songs = AlbumSongSerializer(many=True)

    class Meta:
        model = Album
        fields = "__all__"

    @transaction.atomic
    def create(self, validated_data):
        album_songs = validated_data['album_songs']
        del validated_data['album_songs']
        album = Album.objects.create(**validated_data)

        # Добавляет песни с проверкой корректности порядковых номеров
        order_list = []
        for album_song in album_songs:
            if not album_song.get("order", None) in order_list:
                serializer = AlbumSongSerializer(data={
                    "song": album_song.get("song", None).id,
                    "order": album_song.get("order", None),
                    "album": album.id
                })
                serializer.is_valid(raise_exception=True)
                serializer.save()
                order_list.append(album_song.get("order", None))
            else:
                raise serializers.ValidationError({"error": "Порядковые номера у песен не могут повторяться"})
        return album

    @transaction.atomic
    def update(self, instance, validated_data):
        album_songs = validated_data['album_songs']
        instance.title = validated_data.get("title", instance.title)
        instance.executor = validated_data.get("executor", instance.executor)
        instance.year_of_issue = validated_data.get("year_of_issue", instance.year_of_issue)

        album_old_songs = set(AlbumSong.objects.filter(album=instance).values_list('id', flat=True))
        # Добавляет песни с проверкой корректности порядковых номеров
        order_list = []
        album_new_songs = []
        for album_song in album_songs:
            if not album_song.get("order", None) in order_list:
                new_song = AlbumSong.objects.get_or_create(album=instance, **album_song)
                order_list.append(album_song.get("order", None))
                album_new_songs.append(new_song[0].id)
            else:
                raise serializers.ValidationError({"error": "Порядковые номеру у песен не могут повторяться"})

        # Удаляет старые
        AlbumSong.objects.filter(id__in=(album_old_songs - set(album_new_songs))).delete()

        instance.save()
        return instance