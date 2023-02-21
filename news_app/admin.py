from django.contrib import admin

from .models import News, Category, Contact


# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title",)
    prepopulated_fields = {"slug": ("title",)}  # new


admin.site.register(News, ArticleAdmin)
admin.site.register(Category)
admin.site.register(Contact)
