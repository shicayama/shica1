from django.db import models

class Content(models.Model):
    """内容"""
    id = models.AutoField('番号', primary_key=True)
    site = models.CharField('サイト名', max_length=255, blank=True)
    url = models.CharField('URL', max_length=255, blank=True)
    date = models.DateField('日付')
    start = models.DateTimeField('閲覧開始時刻')
    end = models.DateTimeField('閲覧終了時刻')

    def __str__(self):
        return self.url

