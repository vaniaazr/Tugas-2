from django.urls import path

# Register, Login, Logout
from todolist.views import register
from todolist.views import login_user
from todolist.views import logout_user

from todolist.views import create_task
from todolist.views import delete_task
from todolist.views import add_task
from todolist.views import change_status

from todolist.views import show_todolist_ajax
from todolist.views import show_json

app_name = 'todolist'

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),

    path('create-task/', create_task, name='create_task'),
    path('delete-task/<int:id>', delete_task, name='delete_task'),
    path('add-task/', add_task, name='add_task'),
    path('change-status/<int:id>', change_status, name='change_status'),

    path('', show_todolist_ajax, name='show_todolist_ajax'),
    path('json/', show_json, name='show_json'),
]