# graphs/urls.py
from django.urls import path
from . import views

app_name = "graphs"  # Django's way to namespace your app's URLs

urlpatterns = [
    path("", views.graph_list, name="graph_list"),
    path("create/", views.create_graph, name="create_graph"),
    path("<int:pk>/", views.graph_detail, name="graph_detail"),
]
