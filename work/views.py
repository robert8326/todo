from django.shortcuts import render
from work.models import TodoList


def todo_lists(request):
    context = {
        'todolist_list': TodoList.objects.all()
    }
    return render(request, 'work/todo_list.html', context=context)
