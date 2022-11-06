from django.contrib import admin

from adminsortable2.admin import SortableInlineAdminMixin, SortableAdminMixin

from album.models import Executor, Album, Song, AlbumSong


@admin.register(Executor)
class ExecutorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class AlbumSongInline(SortableInlineAdminMixin, admin.TabularInline):
    model = AlbumSong
    extra = 0


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'executor', 'year_of_issue')
    list_filter = ('executor', 'year_of_issue')
    inlines = [AlbumSongInline, ]


@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')