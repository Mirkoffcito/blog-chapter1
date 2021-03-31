from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    #path('', views.post_list, name='post_list'),
    path('', views.PostListView.as_view(), name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>', views.post_detail, name='post_detail'), #int(requiere un integer):year(argumento que estoy devolviendo desde el reverse en models.py)
]
