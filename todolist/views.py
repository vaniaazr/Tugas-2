from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from todolist.forms import FormTask
from todolist.models import Task
from django.http import HttpResponseRedirect, HttpResponse, HttpRequest
from django.urls import reverse
from django.core import serializers

# @login_required(login_url='/todolist/login/')
# def show_todolist(request):
#     data_task = Task.objects.filter(user=request.user).all()
#     context = {'task': data_task}
#     return render(request, "todolist.html", context)

@login_required(login_url='/todolist/login/')
def show_todolist_ajax(request):
    data = Task.objects.filter(user=request.user).all()
    context = {
        'todo_list': data,
    } 
    return render(request, "todolist_ajax.html", context)

def show_json(request):
    data = Task.objects.filter(user=request.user).all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def add_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        new_task = Task(
            title=title, 
            description=description,
            user=request.user,
        )
        new_task.save()
    return redirect('todolist:show_todolist_ajax')

def create_task(request):
    form = FormTask()
    if request.method == "POST":
        form = FormTask(request.POST)
        if form.is_valid():
            form = Task(
                title=form.cleaned_data["title"],
                description=form.cleaned_data["description"],
                user=request.user,
            )
            form.save()
            return redirect("todolist:show_todolist")

    context = {'form': form}
    return render(request, "create_task.html", context)

def delete_task(request, id):
    Task.objects.get(pk=id).delete()
    return redirect('todolist:show_todolist_ajax')

def change_status(request, id):
    task = Task.objects.get(pk=id) 
    if (not task.is_finished):
        task.is_finished = True
    task.save()
    return redirect('todolist:show_todolist_ajax')

def register(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account has been created successfully!')
            return redirect('todolist:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('todolist:show_todolist_ajax')
        else:
            messages.info(request, 'Wrong username or password:(')
    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    messages.info(request, 'Logout Successful')
    return redirect('todolist:login')