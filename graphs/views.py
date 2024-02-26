from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Graph
from .forms import GraphForm  # Assuming you have a form for Graph


def graph_list(request):
    graphs = Graph.objects.all()
    return render(request, "graph_list.html", {"graphs": graphs})


def create_graph(request):
    if request.method == "POST":
        form = GraphForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("graphs:graph_list")
    else:
        form = GraphForm()
    return render(request, "graph_create.html", {"form": form})


def graph_detail(request, pk):
    graph = get_object_or_404(Graph, pk=pk)
    # Additional context might be needed to display the graph using Plotly
    return render(request, "graph_detail.html", {"graph": graph})
