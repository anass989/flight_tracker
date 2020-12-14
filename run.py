from app import app

if __name__ == "__main__":
  app.run()


# def index():
#     start_coords = (46.9540700, 142.7360300)
#     folium_map = folium.Map(location=start_coords, zoom_start=14)
#     return folium_map._repr_html_()

# params = {
#   'access_key':'ec5eec6171bae77ee785ec2c01cdd1ea'
# }

# api_result = requests.get('http://api.aviationstack.com/v1/flights', params)

# api_response = api_result.json()

# for flight in api_response['res']:
#     if (flight['live']['is_ground'] is False):
#         print(u'%s flight %s from %s (%s) to %s (%s) is in the air.' % (
#             flight['airline']['name'],
#             flight['flight']['iata'],
#             flight['departure']['airport'],
#             flight['departure']['iata'],
#             flight['arrival']['airport'],
#             flight['arrival']['iata']))