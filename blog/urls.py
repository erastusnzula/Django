from django.urls import path

from blog import views

app_name = 'blog'
urlpatterns = [
    path('', views.frontpage, name='frontpage'),
    path('blog/', views.blog_index, name='blog'),
    path('blog/<int:id>/', views.blog_detail, name='blog-detail'),
    path('comment_edit/<int:id>/', views.edit_comment, name='edit-comment'),
    path('blog/<category>/', views.blog_category, name='blog-category'),
]
