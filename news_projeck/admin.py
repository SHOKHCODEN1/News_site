from django.contrib import admin
from .models import Category , Contact , News

admin.site.register(Category)

admin.site.register(Contact)

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title' , 'slug']
    list_filter = ['status']
    search_fields = ['title']
    prepopulated_fields = {'slug': ('title',)}