from django.urls import path
from work.views import todo_lists


urlpatterns = [
    path('', todo_lists, name='todo_list')
]
