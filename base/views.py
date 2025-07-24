from django.shortcuts import render

# Create your views here.

rooms = [
    {"id": 1, "name": "room name 1"},
    {"id": 2, "name": "room name 2"},
    {"id": 3, "name": "room name 3"},
]


def home(request):
    context = {"rooms": rooms}
    return rener(request, "home.html", context)


def room(request):
    return render(request, "room.html")
