from django import forms
from .models import Graph


class GraphForm(forms.ModelForm):
    class Meta:
        model = Graph
        fields = ["title", "data_endpoint", "graph_type"]
