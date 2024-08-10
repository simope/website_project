from main.models import Player, Game
from django.db.models import Count
import plotly.express as px
import folium
import requests

def extractIPandLocation(ip):
    # Extract users IP already in the DB
    ip_list = Player.objects.values_list('IP', flat=True)

    # Extract IP and locate user
    ip = "92.109.61.185" # Remove this line if online

    if not(ip in ip_list):
        # Extract data through API
        ip_data = (requests.get('https://ipwho.is/'+ip)).json()

        # Save into model and DB if not already there
        userModel = Player(
            IP=ip,
            nickname='',
            latitude=ip_data["latitude"],
            longitude=ip_data["longitude"],
            points=0)
        
        userModel.save()

def createChart():
    # Extract match statistics
    data_match = (Game.objects
            .values('result')
            .annotate(count=Count('result'))
            .order_by())

    total = 0
    for entry in data_match:
      total += entry['count']

    for entry in data_match:
      entry['count'] /= total
      entry['count'] *= 100

    # Create bar chart
    fig = px.bar(
        data_match,
        x='result',
        y='count',
        color='result',
        labels={
            "result": '',
            "count": "Percentage of occurence %"
        }
    )

    fig.update_layout({
      'plot_bgcolor': 'rgba(0, 0, 0, 0)',
      'paper_bgcolor': 'rgba(0, 0, 0, 0)',
    })

    fig.update_layout(
      showlegend=False,
      title_x=0.5
    )

    chart = fig.to_html

    return chart, total

def createMap():
    # Reading users locations
    data_users = (Player.objects.values('latitude', 'longitude'))

    # Creating the users map
    f = folium.Figure(width="700px")
    m = folium.Map()
    m.add_to(f)  

    # Adding the markers
    for entry in data_users:
        folium.Marker(location=[entry['latitude'], entry['longitude']]).add_to(m)

    m = m._repr_html_()

    return m