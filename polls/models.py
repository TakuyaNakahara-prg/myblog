from django.db import models

class Category(models.Model):
    name = models.CharField(max_length = 50, verbose_name = 'カテゴリー')

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length = 255, verbose_name = 'タイトル')
    text = models.TextField(verbose_name="本文")
    date = models.DateTimeField(auto_now_add = True, blank = True, verbose_name = '投稿日時')
    category = models.ForeignKey(Category, on_delete = models.PROTECT, verbose_name = 'カテゴリー')
    relate_article = models.ManyToManyField('self', verbose_name = '関連記事', blank = True, null = True)

    def __str__(self):
        return self.title

    def summary(self):
        return self.text[:60]


