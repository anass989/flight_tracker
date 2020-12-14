from flask import render_template
import requests

# 40.463667, -3.74922
def get_active_flights():
    flights = []
    response = requests.get(f'http://aviation-edge.com/v2/public/flights?key={params["edge_key"]}&lat=40.463667&lng=-3.74922&distance=2000&limit=700').json()
    for flight in response:
        if flight["flight"]["iataNumber"]:
            flights.append(flight)
    print(flights)
    return flights

def get_flight_details(flight_iata):
    response = requests.get(f'http://aviation-edge.com/v2/public/timetable?key={params["edge_key"]}&status=active&flight_iata={flight_iata}').json()
    return response

def get_arrivals(arr_icao):
    response = requests.get(f'https://api.aviationstack.com/v1/flights?access_key={params["access_key"]}&flight_status=active&arr_icao={arr_icao}').json()
    return response

def get_departures(dep_icao):
    response = requests.get(f'https://api.aviationstack.com/v1/flights?access_key={params["access_key"]}&flight_status=active&dep_icao={dep_icao}').json()
    return response

def get_coordinates(flight_iata):
    coords = []
    response = requests.get(f'https://opensky-network.org/api/states/all?icao24={flight_icao}')
    coords.append(response["states"][6])
    coords.append(response["states"][7])
    return coords
    
# def get_airport_image():
def get_aircraft_image(aircraft_type):
    url = ''
    response = requests.get(url).json()
    return response

def get_modal(details):
    if details != None:
        print(details[0]['flight'])
        res = """<div class='flight-info'>
                <span class='airline-number'>{details[0][flight][iataNumber]}</span>
                <span class='airline-name'>{details[0][airline][name]}</span>
            </div>
            <div class='flight-timetable'>
            <div class='departure'>
                <span class='airline-code'>{details[0][departure][iataCode]}</span>
                <div class='airline-time'>
                    <span class='time'>Scheduled Time: {details[0][departure][scheduledTime]}</span>
                    <span class='time'> Time: {details[0][departure][actualTime]}</span>
                </div>
            </div>
            <div class='arrival'>
                <span class='airline-code'>{details[0][arrival][iataCode]}</span>
                <div class='airline-time'>
                    <span class='time'>Schedule time: {details[0][arrival][scheduledTime]}</span>
                    <span class='time'>Estimated time: {details[0][arrival][estimatedTime]}</span>
                </div>
            </div>
            </div>
            <button class="close-form" onclick="close()">X</button>"""
        new = res.format(details=details)
        return new
    else:
        return 0