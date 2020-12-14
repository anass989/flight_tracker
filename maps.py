from app import app, utils
import os, json, requests
import folium
from folium import plugins

def create_base_map():
    if os.path.exists('./app/templates/map.html'):
        os.remove('./app/templates/map.html')
    response = utils.get_active_flights()
  
    map = folium.Map(location=[40.463667, -3.74922], zoom_start=6)
    tooltip = "See flight information"

    logoIcon = folium.features.CustomIcon('./app/static/img/paperplane.png', icon_size=(50, 50))
    # api_result = requests.get('http://api.aviationstack.com/v1/flights', params)
    # Latitud Mínima Longitud Mínima [25.483, -20.039], Latitud Máxima Longitud Máxima [45.089, 7.031]

    for flight in response:
        flight_id = flight["flight"]["iataNumber"]
        marker=folium.Marker(location=[flight["geography"]["latitude"], flight["geography"]["longitude"]], popup=f'<span>Flight: {flight_id}</span><button id="flight_button" class="show" value="{flight_id}" onclick="func()">Show flight details</button>', tooltip=tooltip, icon=folium.features.CustomIcon('./app/static/img/paperplane.png', icon_size=(30, 30))).add_to(map)

    map.save('./app/templates/map.html')  

def create_airport_locations_map():
    filename = os.path.join(app.static_folder, 'airports.json')
    with open(filename) as airport_json:
        airports = json.load(airport_json)
    map = folium.Map(location=[40.463667, -3.74922], zoom_start=5)
    for airport in airports["airports"]:
        marker = folium.Marker(location=[airport["geometry"]["y"], airport["geometry"]["x"]]).add_to(map)
    
    if os.path.exists('./app/templates/airports.html'):
        os.remove('./app/templates/airports.html')
    map.save('./app/templates/airports.html')

def create_airport_map(airport_coords, arrivals, departures, icao):
    map = folium.Map(location=[airport_coords[1], airport_coords[0]], zoom_start=5)
    group = folium.FeatureGroup(name="All active flights")
    map.add_child(group)
    # incoming flights
    incoming = folium.plugins.FeatureGroupSubGroup(group, "Incoming flights")
    map.add_child(incoming)
    # departing flights
    departing = folium.plugins.FeatureGroupSubGroup(group, "Departing flights")
    map.add_child(departing)

    for arrival in arrivals["data"]:
        if(arrival["live"] != None):
            marker=folium.Marker(location=[arrival["live"]["latitude"], arrival["live"]["longitude"]], icon=folium.features.CustomIcon('./app/static/img/paperplane.png', icon_size=(30, 30))).add_to(incoming)
    #     # else:
    #     #     coords = []
        #     coords = utils.get_coordinates(arrival["flight_icao"])
        #     marker=folium.Marker(location=[coords[0], coords[1]])

    for departure in departures["data"]:
        if(departure["live"] != None):
            marker=folium.Marker(location=[departure["live"]["latitude"], departure["live"]["longitude"]], icon=folium.features.CustomIcon('./app/static/img/paperplane.png', icon_size=(30, 30))).add_to(departing)
        # else:
        #     coords = []
        #     coords = utils.get_coordinates(departure["flight_icao"])
        #     marker=folium.Marker(location=[coords[0], coords[1]])
    marker=folium.Marker(location=[airport_coords[1], airport_coords[0]], icon=folium.Icon(color="red", icon_color="white", icon="luggage-cart", prefix='fa')).add_to(map)

    folium.LayerControl(collapsed=True).add_to(map)

    if os.path.exists(f'./app/templates/{icao}.html'):
        os.remove(f'./app/templates/{icao}.html')
    map.save(f'./app/templates/{icao}.html')
    return f'./app/templates/{icao}.html'
    # if os.path.exists('./app/templates/airports.html'):
    #     os.remove('./app/templates/airports.html')
    # map.save('./app/templates/airports.html')
    
    


    
