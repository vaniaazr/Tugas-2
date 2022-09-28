from django.urls import path
from todolist.views import show_todolist
from todolist.views import create_todolist
from todolist.views import register
from todolist.views import login_user
from todolist.views import logout_user
from todolist.views import status
from todolist.views import delete

app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('create-task/', create_todolist, name='create_todolist'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('status/<int:id>/', status, name='status'),
    path('delete/<int:id>/', delete, name='delete'),
]