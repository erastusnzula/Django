from django.urls import path
from projects import views

app_name = 'projects'
urlpatterns = [
    path('projects/', views.projects_list, name='projects'),
    path('projects/<int:id>/', views.project_details, name='project_detail'),
    path('projects/<category>/', views.project_category, name='project-category')
]
