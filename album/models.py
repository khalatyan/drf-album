from django.db import models

class Executor(models.Model):
    """ Исполнитель """

    name = models.CharField(
        max_length=512,
        verbose_name=u'Название'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u'Исполнитель'
        verbose_name_plural = u'исполниетли'


class Album(models.Model):
    """ Альбом """

    title = models.CharField(
        max_length=512,
        verbose_name=u'Название'
    )

    executor = models.ForeignKey(
        Executor,
        verbose_name=u'Исполнитель',
        on_delete=models.CASCADE,
        blank=False,
        null=False
    )

    year_of_issue = models.PositiveIntegerField(
        verbose_name=u'Год выпуска',
        default=2000
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = u'Альбом'
        verbose_name_plural = u'альбомы'


class Song(models.Model):
    """ Песня """

    title = models.CharField(
        max_length=512,
        verbose_name=u'Название'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = u'Песня'
        verbose_name_plural = u'песни'


class AlbumSong(models.Model):
    album = models.ForeignKey(
        Album,
        verbose_name=u'Альбом',
        related_name=u'album_songs',
        on_delete=models.CASCADE,
        blank=False,
        null=False
    )

    song = models.ForeignKey(
        Song,
        verbose_name=u'Песня',
        on_delete=models.CASCADE,
        blank=False,
        null=False
    )

    order = models.PositiveIntegerField(
        verbose_name=u'Порядковый номер',
        default=1
    )

    class Meta:
        verbose_name = u'Песня в альбоме'
        verbose_name_plural = u'песни в альбоме'
        ordering = ['order']

    def __str__(self):
        return u'%s' % self.song.title