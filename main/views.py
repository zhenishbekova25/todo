from django.shortcuts import render, HttpResponse
from .models import Todo


def homepage(request):
    return render(request, "index.html")


def test(request):
    todo_list = ToDo.objects.all()
    return render(request, "test.html", {"todo_list": todo_list})

def test3 (request):
    return HttpResponse("This is page test3")