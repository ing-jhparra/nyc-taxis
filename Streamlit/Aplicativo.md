# Explicación del aplicativo Creative Mobiles App.
Este aplicativo desarrollado en Streamlit permite predecir el precio de la tarifa de un viaje en taxi, basado en las direcciones de origen y destino proporcionadas por el usuario.
<p align="center">
    <img src="https://media.dev.to/cdn-cgi/image/width=1000,height=420,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Ft0jgef3vyjid17z8sf3m.png">
</p>


## Funcionalidades del aplicativo

1. **Importación de Librerías y Configuración Inicial**
    * Se importan las librerías necesarias y se configura la página de la aplicación.

2. **Descarga y Carga del Modelo**
    * Se descarga el modelo entrenado desde un repositorio en GitHub y se carga para su uso en las predicciones.

3. **Estilo de la Página**
    * Se define un estilo personalizado para la página, incluyendo una imagen de fondo y colores específicos para el texto y los elementos de entrada.

4. **Interfaz de Usuario**
    * Se muestra el título de la aplicación y una breve descripción.
    * El usuario puede seleccionar una ciudad de operación y proporcionar las direcciones de origen y destino.

5. **Cálculo de la Ruta y Predicción de la Tarifa**
    * Al hacer clic en el botón "Calcular", se obtienen las coordenadas de las direcciones ingresadas.
    * Se calcula el tiempo y la distancia de la ruta usando una API externa.
    * Se utiliza el modelo cargado para predecir la tarifa del viaje.
    * Se muestran los resultados al usuario, incluyendo tiempo estimado, distancia y tarifa.

## Funciones Adicionales

* **ObtenerCoordenadas:** Obtiene las coordenadas geográficas de una dirección.
* **ObtenerRuta:** Calcula el tiempo y la distancia entre dos coordenadas.
* **MostrarMapa:** Muestra un mapa con la ruta calculada usando Folium.

Estas funciones permiten que la aplicación procese las direcciones ingresadas, obtenga la información necesaria y presente los resultados de manera interactiva y visual.
Para más informacion sobre el codigo vea [Funciones](https://github.com/ing-jhparra/nyc-taxis/blob/main/Streamlit/funciones.py) y [Aplicativo](https://github.com/ing-jhparra/nyc-taxis/blob/main/Streamlit/App.py)

***

Este aplicativo ofrece una forma intuitiva y eficiente para que los usuarios estimen el costo de sus viajes en taxi basándose en ubicaciones específicas.
