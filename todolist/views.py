from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from todolist.forms import FormTask
from todolist.models import Task

@login_required(login_url='/todolist/login/')
def show_todolist(request):
    data_task = Task.objects.filter(user=request.user).all()
    context = {'task': data_task}
    return render(request, "todolist.html", context)

def create_todolist(request):
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

    form = FormTask()
    context = {'form': form}
    return render(request, "create_task.html", context)

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
            return redirect('todolist:show_todolist')
        else:
            messages.info(request, 'Wrong username or password:(')
    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect('todolist:login')