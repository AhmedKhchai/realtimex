from django.shortcuts import render
import requests
import plotly.graph_objs as go
from plotly.offline import plot


def data_sources(request):
    return render(request, "data_sources.html")


def alphavantage(request):
    # Fetch data from Alpha Vantage
    url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&apikey=demo"
    response = requests.get(url)
    data = response.json()["Time Series (Daily)"]

    dates = list(data.keys())
    closes = [float(data[date]["4. close"]) for date in dates]

    # Create Plotly graph
    fig = go.Figure(data=[go.Scatter(x=dates, y=closes)])
    plot_div = plot(fig, output_type="div", include_plotlyjs=False)

    # Pass the graph to the template
    return render(request, "alphavantage.html", context={"plot_div": plot_div, 'url': url })
