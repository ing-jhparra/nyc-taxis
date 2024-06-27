# Importamos las librerías a usar 
import numpy as np
import streamlit as st 
from funciones import ObtenerCoordenadas, ObtenerRuta
from joblib import load 

# Configurar la página
st.set_page_config(
    page_title="Creative Mobile App",
    page_icon="🚕",  
)

# Cargamos el modelo

modelo = load('../MachineLearning/ridge_model.joblib?raw=True')

# CSS para la imagen de fondo y estilos de texto
page_bg_img = '''
<style>
[data-testid="stAppViewContainer"] {
    background-image: url("https://images.pexels.com/photos/1521580/pexels-photo-1521580.jpeg");
    background-size: cover;
    background-position: center;
    color: white;  /* Color de texto predeterminado para todo el contenido */
}

h1 {
    color: white;  /* Color del título */
}

label, .stTextInput > div > div {
    color: white;  /* Color de las etiquetas de las barras de entrada */
}

.stTextInput > div > div > input {
    color: black;  /* Color del texto dentro de las barras de entrada */
}

.stButton > button {
    color: black;
    background-color: white;
}

</style>
'''

# Cargar la imagen de fondo y estilos
st.markdown(page_bg_img, unsafe_allow_html=True)

# Parte del estilo
st.title("Bienvenido a la app de Creative Mobile Technologies")
st.markdown("*Esta aplicación te dará el precio de tu tarifa una vez ingreses las direcciones*", unsafe_allow_html=True)

# Crear una barra de entrada para la dirección de origen
direccion_origen = st.text_input(label="", placeholder="Ingrese su dirección de origen:")

# Crear una barra de entrada para la dirección de destino
direccion_destino = st.text_input(label="", placeholder="Ingrese su dirección de destino:")

# Añadir un botón para calcular la ruta
if st.button("Calcular"):
    # Inicializar variables
    tiempo = None
    distancia = None

    if direccion_origen == "" or direccion_destino == "":
        st.write('Direcciones no ingresadas.')
    else:
        # Obtener coordenadas
        lat_origen, lon_origen = ObtenerCoordenadas(direccion_origen)
        lat_destino, lon_destino = ObtenerCoordenadas(direccion_destino)

        # Obtener tiempo y distancia
        tiempo, distancia = ObtenerRuta(lat_origen, lon_origen, lat_destino, lon_destino)
        
        # Verificar que tiempo y distancia no sean NaN
        if np.isnan(tiempo) or np.isnan(distancia):
            st.write('No se pudo calcular la ruta. Por favor, verifica las direcciones ingresadas.')
        else:
            # Preparar los datos para el modelo
            new_data = np.array([[distancia, tiempo]])
            
            # Predecir la tarifa
            tarifa = modelo.predict(new_data)[0]
            
            # Mostrar resultados
            st.write(f'Tiempo estimado: {tiempo} minutos, distancia a recorrer: {distancia} millas, el valor de su tarifa es: {round(tarifa, 1)}$')


