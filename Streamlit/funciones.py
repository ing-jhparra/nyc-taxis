from opencage.geocoder import OpenCageGeocode
import requests
import folium
from streamlit_folium import folium_static
from config import OPENCAGE_API_KEY


key = OPENCAGE_API_KEY
geocoder = OpenCageGeocode(key)

def ObtenerCoordenadas(query:str):
    results = geocoder.geocode(query)
    
    if results:
        latitude = results[0]['geometry']['lat']
        longitude = results[0]['geometry']['lng']
        return latitude, longitude
    else:
        return None, None
    
    
def ObtenerRuta(lat_inicio, lon_inicio, lat_destino, lon_destino):
    url = f"http://router.project-osrm.org/route/v1/driving/{lon_inicio},{lat_inicio};{lon_destino},{lat_destino}?overview=false"
    response = requests.get(url)
    data = response.json()
    
    if data['code'] == 'Ok':
        ruta = data['routes'][0]
        tiempo = int(round(int(ruta['duration']) / 60, 0))
        distancia = round(int(ruta['distance']) * 0.000621371, 2)
        return tiempo, distancia
    else:
        print(f"Error en la respuesta de OSRM: {data['code']}")
        return None, None
    
def MostrarMapa(lat_origen, lon_origen, lat_destino, lon_destino):
    url = f'http://router.project-osrm.org/route/v1/driving/{lon_origen},{lat_origen};{lon_destino},{lat_destino}?overview=full&geometries=geojson'

    # Hacer la solicitud a la API de OSRM
    response = requests.get(url)
    data = response.json()

    # Extraer los puntos de la ruta
    route = data['routes'][0]['geometry']
    route_points = [(coord[1], coord[0]) for coord in route['coordinates']]

    # Crear un mapa centrado en las coordenadas de origen
    m = folium.Map(location=[lat_origen, lon_origen], zoom_start=13)

    # Agregar la ruta al mapa
    folium.PolyLine(route_points, color="blue").add_to(m)

    # Agregar un marcador verde en el origen
    folium.Marker(
        location=[lat_origen, lon_origen],
        popup="Origen",
        icon=folium.Icon(color="green")
    ).add_to(m)

    # Agregar un marcador rojo en el destino
    folium.Marker(
        location=[lat_destino, lon_destino],
        popup="Destino",
        icon=folium.Icon(color="red")
    ).add_to(m)

    # Mostrar el mapa en Streamlit
    folium_static(m)