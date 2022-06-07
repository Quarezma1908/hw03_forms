from django.contrib import admin
# Из модуля models импортируем модель Post
from .models import Post, Group

class PostAdmin(admin.ModelAdmin):
    # Перечисляем поля, которые должны отображаться в админке
    list_display = ('pk', 'text', 'pub_date', 'author', 'group') 
    #list_editable = {'group',}
    search_fields = ('text',) 
    list_filter = ('pub_date',) 
    empty_value_display = '-пусто-' 
    

admin.site.register(Post, PostAdmin)
admin.site.register(Group) 