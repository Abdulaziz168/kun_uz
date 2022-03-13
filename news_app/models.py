from django.db import models
from django.contrib.contenttypes.fields import GenericRelation


class Categories(models.Model):
    title = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
        db_table = 'categories'


class News(models.Model):
    title = models.CharField(max_length=200, blank=True, null=False)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='media/')
    date_created = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    category_depend_on = models.ForeignKey(Categories, on_delete=models.CASCADE)
    get_shareable_link = models.URLField(max_length=255, blank=True, null=True, )

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
        db_table = 'news'
