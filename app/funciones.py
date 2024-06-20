'''
Proyecto : <Nombre> 
Version : 0.0
Fecha : 12-06-2024
Autores :
        Juan Camilo Torres Salas
        Adrian Facundo Corvalan
        Javier Yañez
        Michael Martinez
        Jesus H. Parra B.
'''

# Area de carga de librerias necesaria
import pandas as pd
import numpy as np
import re
import requests
import warnings
warnings.filterwarnings('ignore')
from bs4 import BeautifulSoup
from datetime import date
import os

# Si existen variables globales definirlas aqui 
string_vacio = str()
patron_nombre = r"^[a-zA-Z]{1,12}$"   

'''
 Funcion de testeo, recibe como argumento un nombre de persona y devuelve un mensaje de Bienvenido mas nombre
'''
def bienvenido (nombre):

    mensaje = string_vacio

    if type(nombre) == str:
        if re.match(patron_nombre, nombre):
            mensaje = f"Bienvenido {nombre}" 
        else:
            mensaje = "Debe colocar solo caracteres alfabeticos"
    else :
        mensaje = "El valor no es de tipo string"
    return mensaje

'''
 Función crear un listado de las descargar por hacer de la siguiente 
 pagina https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page, utilizando webscrapping
'''
def crear_listado_descarga(ruta, nombre_archivo):

    mensaje = str()

    # Redefinir la variable "user-agent" para evitar que los servidores detecten que se trata de un robot
    encabezados = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"
    }

    # Definicon de url semilla
    url = 'https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page'

    # Solictar peticion de la url
    respuesta = requests.get(url,headers=encabezados)

    # Parsear y extraer informacion de enlaces
    soup = BeautifulSoup(respuesta.text,"html.parser")
    contenedor_parquet = soup.find_all(class_="faq-answers")
    https_links = [a['href'].strip() for a in soup.find_all('a', href=True) if a['href'].startswith('https')]

    # Eliminar enlaces que no son para descargar archivos parquet
    links_borrar = list() 
    for lnk in https_links:
        if "parquet" not in lnk:
            links_borrar.append(lnk)
    for lnk in links_borrar:
        https_links.remove(lnk)

    # Crear una variable fecha y estuctura de datos que guardarda informacion de los enlaces 
    today = "1999-01-01"
    taxi = dict(enlace=list(),fecha_descarga=list(), fecha_dataset=list(),status=list(),nombre=list(),tipo=list(), descargado=list())

    # Cargar la estructura de datos a partir de los datos obtenidos en https_links
    taxi["enlace"] = https_links
    for lnk in taxi["enlace"] :
        taxi["fecha_descarga"].append(today)
        taxi["fecha_dataset"].append(lnk[-15:-8])
        taxi["status"].append("Malo")
        taxi["nombre"].append(lnk.split('/')[-1])
        if "yellow" in lnk:
            taxi["tipo"].append("Yellow")
        elif "green" in lnk:
            taxi["tipo"].append("Green")
        elif "fhv" in lnk:
            taxi["tipo"].append("FHV")
        else:
            taxi["tipo"].append("HVFHV")
        taxi["descargado"].append("No")

    # Creando el archivo en la ruta
    lista_taxi = pd.DataFrame(taxi)
    lista_taxi.to_csv(ruta + nombre_archivo, sep=';', index=False, encoding='utf-8')

     
    # Como forma de validacion se calcula el tamaño del archivo
    sizefile = os.stat(ruta + nombre_archivo).st_size
    if sizefile > 0:
        mensaje = "Bueno"
    else:
        mensaje = "Malo"  
         
    return mensaje

def descargar_dataset(ruta, nombre_archivo, tipo, fechas):
    mensaje = str()
    taxi = pd.read_csv(ruta + nombre_archivo,sep=";", encoding='utf-8')
    filtrado = taxi[(taxi["tipo"]==tipo) & (taxi["fecha_dataset"].isin(fechas))]
    today = date.today()
    descargados = 0
    for ind in range(len(filtrado)):
        response = requests.get(filtrado["enlace"].iloc[ind], stream=True)
        if response.status_code == 200:
            with open(ruta + filtrado["nombre"].iloc[ind], 'wb') as file:
                for chunk in response.iter_content(chunk_size=8192):
                    file.write(chunk)
            descargados += 1
            # Leer el archivo desde el lugar almacenado y calcular su tamaño si este es 0 esta malo
            sizefile = os.stat(ruta + nombre_archivo).st_size
            if sizefile > 0:
                filtrado["status"].iloc[ind] = "Bueno"
                filtrado["fecha_descarga"].iloc[ind] = today
                filtrado["descargado"].iloc[ind] = "Si"
    # Actualizar valores utilizando
    taxi.update(filtrado)
    taxi.to_csv(ruta + nombre_archivo, sep=";")
    if descargados == len(filtrado):
        mensaje = "OK"
    else :
        mensaje = "Revisar"
    return mensaje
