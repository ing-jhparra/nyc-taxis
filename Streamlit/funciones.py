from opencage.geocoder import OpenCageGeocode
import requests


key = 'ba4325302d1d4934b228b068cf0fbdf0'
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