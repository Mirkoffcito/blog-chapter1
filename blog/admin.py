from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish', 'status') # list_display es un atributo que nos sirve para mostrar los campos en el panel de administrador
    list_filter = ('status', 'created', 'publish', 'author') # Crea una barra lateral para incluir filtros de busqueda
    search_fields = ('title', 'body') # crea una barra de busqueda de posts
    prepopulated_fields = {'slug': ('title',)} # rellena automaticamente el campo de 'slug' con el campo 'title'
    raw_id_fields = ('author',) # se utiliza para buscar al autor del post
    date_hierarchy = 'publish'
    ordering = ('status', 'publish') # ordena los posts por su status y su publish date

