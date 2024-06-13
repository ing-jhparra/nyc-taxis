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

# Si existen variables globales definirlas aqui 
string_vacio = str()
patron_nombre = r"^[a-zA-Z]{1,12}$"   

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
