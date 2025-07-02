from django.shortcuts import render
from .models import Todo
from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy


def todo_list(request):  # 테스트용
    todos = Todo.objects.all()
    return render(request, "todo/todo.html", {"todos": todos})


# 전체보기
class TodoListViews(ListView):  # 제너릭뷰
    model = Todo
    template_name = "todo/list.html"
    context_object_name = "todos"
    ordering = ["-created_at"]
    success_url = reverse_lazy("todo_List")


# 생성
class TodoCreateViews(CreateView):
    model = Todo
    template_name = "todo/create.html"
    fields = ["name", "description", "complete", "exp"]
    success_url = reverse_lazy("todo_List")


# 상세보기
class TodoDetailViews(DetailView):
    model = Todo
    template_name = "todo/detail.html"
    context_object_name = "todos"


class TodoUpdateViews(UpdateView):
    model = Todo
    fields = ["name", "description", "complete", "exp", "completed_at", "image"]
    template_name = "todo/update.html"
    context_object_name = "todos"
    success_url = reverse_lazy("todo_List")