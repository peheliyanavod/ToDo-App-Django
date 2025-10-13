from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password



# Create your views here.

def home(request):
    if "user_id" not in request.session:
        messages.warning(request, "Please log in to continue.")
        return redirect("login")

    user = User.objects.get(user_id=request.session["user_id"])
    tasks = Task.objects.filter(user=user).order_by("-created_at")

    context = {
        'tasks': tasks,
        'username': request.session.get("username"),
    }
    return render(request, "home.html", context)


def login(request):
    if request.method == "POST":
        username = request.POST.get("username").strip()
        password = request.POST.get("password")

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            messages.error(request, "Invalid username or password.")
            return redirect("login")

        if check_password(password, user.password):
            request.session["user_id"] = user.user_id
            request.session["username"] = user.username
            messages.success(request, f"Welcome back, {user.username}!")
            return redirect("home")
        else:
            messages.error(request, "Invalid username or password.")
            return redirect("login")

    return render(request, "login.html")


def register(request):
    if request.method == "POST":
        username = request.POST.get("username").strip()
        email = request.POST.get("email").strip()
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        if not username or not email or not password:
            messages.error(request, "All fields are required.")
            return redirect("register")

        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect("register")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return redirect("register")

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists.")
            return redirect("register")

        User.objects.create(
            username=username,
            email=email,
            password=make_password(password)
        )

        messages.success(request, "Account created successfully! Please log in.")
        return redirect("login")

    return render(request, "register.html")


def add_task(request):
    if "user_id" not in request.session:
        messages.warning(request, "Please log in to add a task.")
        return redirect("login")

    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        date = request.POST.get("date")
        time = request.POST.get("time")

        user = User.objects.get(user_id=request.session["user_id"])

        Task.objects.create(
            title=title,
            description=description,
            date=date,
            time=time,
            user=user
        )
        messages.success(request, "Task added successfully.")
        return redirect("home")

    return render(request, "add_task.html")


def edit_task(request, task_id):
    if "user_id" not in request.session:
        messages.warning(request, "Please log in to edit a task.")
        return redirect("login")

    try:
        task = Task.objects.get(task_id=task_id, user__user_id=request.session["user_id"])
    except Task.DoesNotExist:
        messages.error(request, "Task not found.")
        return redirect("home")

    if request.method == "POST":
        task.title = request.POST.get("title")
        task.description = request.POST.get("description")
        task.date = request.POST.get("date")
        task.time = request.POST.get("time")
        task.save()
        messages.success(request, "Task updated successfully.")
        return redirect("home")

    context = {
        'task': task
    }
    return render(request, "edit_task.html", context)


def delete_task(request, task_id):
    if "user_id" not in request.session:
        messages.warning(request, "Please log in to delete a task.")
        return redirect("login")

    if request.method != "POST":
        messages.error(request, "Invalid request method.")
        return redirect("home")

    try:
        task = Task.objects.get(task_id=task_id, user__user_id=request.session["user_id"])
        task.delete()
        messages.success(request, "Task deleted successfully.")
    except Task.DoesNotExist:
        messages.error(request, "Task not found.")

    return redirect("home")


def logout_view(request):
    request.session.flush()
    messages.info(request, "You have been logged out successfully.")
    return redirect("login")


