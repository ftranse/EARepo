from django.db import models
from django.urls import reverse


class Product(models.Model):
    title = models.CharField(max_length=150, verbose_name='Наименование')
    comment = models.TextField(blank=True, verbose_name='Комментарий')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    diagram = models.ImageField(upload_to='diagrams/%Y/%m/%d/', verbose_name='Диаграмма', blank=True)
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категория')
    views = models.IntegerField(default=0)

    def get_absolute_url(self):
        return reverse('view_product', kwargs={"pk": self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Приложение'
        verbose_name_plural = 'Приложения'
        ordering = ['title']


class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Наименование')

    def get_absolute_url(self):
        return reverse('category', kwargs={"category_id": self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']
