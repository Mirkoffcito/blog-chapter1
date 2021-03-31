from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Published(models.Manager): # custom manager
    def get_queryset(self):
        return super(Published, self).get_queryset().filter(status='published')

class Post(models.Model):

    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    title = models.CharField(max_length=250) # Titulo del post
    slug= models.SlugField(max_length=250, unique_for_date='publish') # el slug se utiliza en la URL, SEO friendly. "unique for date" utilizará la fecha de publicado en la URL
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now) # Cuando el post fue publicado
    created = models.DateTimeField(auto_now_add=True) # La fecha será guardada automaticamente con auto_now_add
    updated = models.DateTimeField(models.DateTimeField(auto_now=True)) # auto_now actualizará la fecha automaticamente cuando modifiquemos un objeto
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft') #
    objects = models.Manager() # default manager (todos los objetos) ES NECESARIO INCLUIRLO EXPLICITAMENTE SI VAMOS A UTILIZAR UN CUSTOM MANAGER
    published = Published() # custom manager (solo objetos publicados) 

    class Meta: # se utiliza para organizar los resultados por un campo en la base de datos
        ordering=('-publish',) # en este caso estaran organizados por el campo publish, el "-" indica que estará organizado descendientemente, es decir, mas recientes primero

    def __str__(self): # Muestra el campo de titulo en formato texto legible en el panel de administrador a la hora de crear/modificar
        return self.title

    def get_absolute_url(self): # devuelve la URL de un post individual a la aplicacion blog en la url name=post_detail en views.py
        return reverse(         # con los argumentos year(int)/month(int)/day(int)/slug:slug
            'blog:post_detail',
            args=[self.publish.year, #es un entero
                    self.publish.month, #es un entero
                    self.publish.day, #es un entero
                    self.slug] # es un slug(words and hyphens)
            )

