from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.index, name="index"),
    path("create", views.create, name="create"),
    path("admin/", admin.site.urls),
    path("search", views.search, name='search'),
    path("settings", views.settings, name="settings"),
    path("login", views.login, name="login"),
    path("signup", views.signup, name="signup"),
    
]
