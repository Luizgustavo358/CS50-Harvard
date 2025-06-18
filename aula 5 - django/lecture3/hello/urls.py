from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:name>", views.greet, name="greet"),
    path("luiz", views.luiz, name="luiz"),
    path("perla", views.perla, name="perla"),
]
