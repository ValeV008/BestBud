from django.shortcuts import render

# Create your views here.

rooms = [
    {"id": 1, "name": "room name 1"},
    {"id": 2, "name": "room name 2"},
    {"id": 3, "name": "room name 3"},
]


def home(request):
    context = {"rooms": rooms}
    return render(request, "base/home.html", context)


def room(request, room_id):
    room = None
    for i in rooms:
        if i["id"] == int(room_id):
            room = i

    context = {"room": room}
    return render(request, "base/room.html", context)
