from django.urls import path
from . import views
urlpatterns = [
    path('hello-world/<str:username>',views.hello, name = 'hello'),
    path('projects/',views.projects, name='project'),
    path('tasks/',views.tasks, name='task'),
    path('create_task/',views.create_tasks, name='new_task'),
    path('projects/<int:id>',views.project_detail, name='detail'),
    path('create_project/',views.create_project, name='new_project'),
    path('',views.index, name='index')
]
