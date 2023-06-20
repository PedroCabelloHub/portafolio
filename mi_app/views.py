from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404, render, redirect
from .forms import CreateNewTask, CreateNewProject


# Create your views here.
def hello(request, username):
    print(username)
    return HttpResponse('Hello %s' % username)

def index(request):
    title = "Welcome to Django Course"
    return render(request,'index.html',{
        'title':title
    })

def projects(request):
    #projects = list(Project.objects.values())
    projects = Project.objects.all()
    return render(request, 'projects.html',{
        "projects" : projects
    })


def tasks(request):
    #task = get_object_or_404(Task, id=id)
    task = Task.objects.all()
    return render(request, 'tasks.html',{
        "tasks":task
    })

def create_tasks(request):
    if request.method == 'GET':
        return render(request,'create_tasks.html',{
            'form':CreateNewTask()
        })
    else:
        Task.objects.create(titulo=request.POST['title'],description = request.POST['description'], project_id=2)
        return redirect('task')

def create_project(request):
    if request.method == 'GET':
        return render(request, 'create_project.html',{
            'form': CreateNewProject()
        })
    else:
        Project.objects.create(name=request.POST['name'])
        return redirect('project')

def project_detail(request, id):
    print(id)
    project = get_object_or_404(Project, id=id)
    tasks = Task.objects.filter(project_id=id)
    return render(request, 'detail.html',{
        'project' : project,
        'tasks': tasks
    })
