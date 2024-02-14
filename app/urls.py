"""
URL configuration for skeleton project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),

    path("create_event", views.create_event, name="create_event"),
    path("read_event", views.read_event, name="read_event"),
    path("update_event/<int:id>", views.update_event, name="update_event"),
    path("delete_event/<int:id>", views.delete_event, name="delete_event"),
]
