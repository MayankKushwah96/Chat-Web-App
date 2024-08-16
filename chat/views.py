from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Room, Message


@login_required
def EntryView(request):
    if request.method == "POST":
        username = request.POST["username"]
        room = request.POST["room"]
        try:
            existing_room = Room.objects.get(room_name__icontains=room)
        except Room.DoesNotExist:
            r = Room.objects.create(room_name=room)
        return redirect("room", room_name=room, username=username)
    return render(request, "entry.html")

@login_required
def RoomView(request, room_name, username):
    existing_room = Room.objects.get(room_name__icontains=room_name)
    get_messages = Message.objects.filter(room=existing_room)
    context = {
        "messages": get_messages,
        "user": username,
        "room_name": existing_room.room_name,
    }

    return render(request, "room.html", context)


@login_required
def home_page(request):
    return render(request, 'home.html')

def logout_page(request):
    logout(request)
    return redirect('login_page')

def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username=username).exists():
            messages.error(request, 'Invalid Username')
            return redirect('login_page')
        
        user = authenticate(username=username, password=password)

        if user is None:
            messages.error(request, 'Invalid Password')
            return redirect('login_page')
        else:
            login(request, user)
            return redirect('entry') 

    return render(request, 'login.html')

def register_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'User Already Exists')
            return redirect('register_page')

        user = User.objects.create_user(
            username=username,
            password=password
        )
        
        messages.success(request, 'Account Created Successfully')
        return redirect('login_page')

    return render(request, 'register.html')