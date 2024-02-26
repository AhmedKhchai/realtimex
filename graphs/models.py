from django.db import models


class Graph(models.Model):
    title = models.CharField(max_length=255)
    data_endpoint = models.URLField()
    graph_type = models.CharField(max_length=50)
    # Additional fields as necessary

    def __str__(self):
        return self.title
