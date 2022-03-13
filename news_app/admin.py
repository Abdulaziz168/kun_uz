from django.contrib import admin
from .models import Categories, News


# Register your models here.
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title','category_depend_on']


admin.site.register(News, NewsAdmin)
admin.site.register(Categories)
