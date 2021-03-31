from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Post

from django.views.generic import ListView


class PostListView(ListView):
 queryset = Post.published.all()
 context_object_name = 'posts'
 paginate_by = 3
 template_name = 'blog/post/list.html'


def post_list(request):
    object_list = Post.published.all() #CUSTOM MANAGER DEL QUERYSET DEL MODELO Post
    paginator = Paginator (object_list, 3) # El paginator se encarga de mostrar 3 post a la vez de la lista object_list
    page = request.GET.get('page') # recupera la pagina actual (default sera 1)
    try:   
        posts = paginator.page(page) 
    except PageNotAnInteger:
        #If page is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        #if page is out of range deliver the last page of results
        posts = paginator.page(paginator.num_pages) # num_pages = numero de paginas (ultima pagina) // paginator.page para decirle a que pagina quiere ir

    context = {
        'posts': posts, # utilizaremos 'posts' en nuestro template html para mostrar la lista de posts
        'page': page
    }
    return render(request, 'blog/post/list.html', context)

def post_detail (request, year, month, day, post):
    post = get_object_or_404 ( # es un shortcut al mecanismo de try:, else:, retorna el objeto o da error 404
        Post,
        slug=post,
        status='published',
        publish__year=year, # busca el post por el año publicado
        publish__month=month, # busca el post por el mes publicado
        publish__day=day # busca el post por el dia publicado
    )
    context = {
        'post': post
    }
    return render(request, 'blog/post/detail.html', context)

def index(request):
    pass
