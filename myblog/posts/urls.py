from django.urls import path
from . import views

app_name = "posts"

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),

    path("register/", views.register_page, name="register"),
    # Example: /posts/login/
    path("login/", views.login_page, name="login"),
    # Example: /posts/home/ (The page after a successful login)
    path("home/", views.home, name="home"),
    # Example: /posts/logout/
    # path("logout/", views.LogoutView.as_view(), name="logout"),
]
