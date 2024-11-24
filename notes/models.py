from django.db import models

# ジャンル
class Genre(models.Model):

    class Meta:
        verbose_name = 'ジャンル'
        verbose_name_plural = 'ジャンル'

    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

# カテゴリ
class Category(models.Model):

    class Meta:
        verbose_name = 'カテゴリ'
        verbose_name_plural = 'カテゴリ'
        constraints = [
            models.UniqueConstraint(fields=['name', 'genre'], name='unique_category_in_genre')
        ]

    name = models.CharField(max_length=100)
    genre = models.ForeignKey(Genre, related_name='categories', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

# 本文
class Content(models.Model):

    class Meta:
        verbose_name = '本文'
        verbose_name_plural = '本文'
        constraints = [
            models.UniqueConstraint(fields=['title', 'category'], name='unique_content_in_category')
        ]

    title = models.CharField(max_length=100)
    content = models.TextField()
    category = models.ForeignKey(Category, related_name='contents', on_delete=models.CASCADE)

    def __str__(self):
        return self.title