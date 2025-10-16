
from django.shortcuts import render, redirect
from django.views import generic
from .models import Post
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib import messages
from django.contrib.auth import authenticate, login

# Create your views here.
class IndexView(generic.ListView):
    template_name = "posts/index.html"
    context_object_name = "latest_post_list"

    def get_queryset(self):
        return Post.objects.filter(updated_at__lte=timezone.now()).order_by("-updated_at")[:5]

class DetailView(generic.DetailView):
    model = Post
    template_name = "posts/detail.html"

    def get_queryset(self):
        return Post.objects.filter(updated_at__lte=timezone.now())

def home(request):
    return render(request,"posts/home.html")

def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username=username).exists():
            messages.error(request, "Invalid username")
            return redirect("/login/")

        user = authenticate(username=username,password=password)

        if user is None:
            messages.error(request,"Invalid Password")
        else:
            login(request,user)
            return redirect("posts:home")

    return render(request, "posts/login.html")

def register_page(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Check if a user with the provided username already exists
        user = User.objects.filter(username=username)

        if user.exists():
            # Display an information message if the username is taken
            messages.info(request, "Username already taken!")
            return redirect('/register/')

        # Create a new User object with the provided information
        user = User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username
        )

        # Set the user's password and save the user object
        user.set_password(password)
        user.save()

        # Display an information message indicating successful account creation
        messages.info(request, "Account created Successfully!")
        return redirect('/login/')

    # Render the registration page template (GET request)
    return render(request, 'posts/register.html')
