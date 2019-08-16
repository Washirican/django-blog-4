from django.urls import path
from blogging.views import list_view
from blogging.views import detail_view
from blogging.views import add_model

urlpatterns = [
    path('', list_view, name="blog_index"),
    path('posts/<int:post_id>/', detail_view, name='blog_detail'),
    path('new/', add_model, name='add_blog'),
    ]
