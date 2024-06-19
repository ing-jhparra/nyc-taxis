
# Proyecto: Implementación de una Flota de Taxis Eléctricos en Nueva York
<p align="center">
   <br />
   <img src="https://img.shields.io/badge/STATUS-EN%20DESAROLLO-green">
   <br />
</p>

## Contenido

* [Introdcción](#Introducción)

* [Descripción](#Descripción)

* [Conjunto de Datos](#Conjunto-de-Datos)

* [Propuesta](#Propuesta)

* [Objetivo General y Especificos](#Objetivo-General-y-Especificos)

* [Tecnologías utilizadas](#Tecnologías-Utilizadas)

* [Indicadores claves de Desempeño](#Indicadores-claves-de-Desempeño)

* [Conclusión](#Conclusión)

* [Recomendaciones](#Recomendaciones)

* [Autores](#Autores)

## Introducción

En los últimos años, el tránsito de vehículos se transformó en un problema en New York debido a su gran cantidad que excede la capacidad de las calles y de estacionamiento. Por ese motivo hay una gran demanda de otros medios de transporte como los taxis. Sin embargo, el medio de transporte es el sector que más emisiones de CO2 produce en todo Estados Unidos. Para mitigar el impacto ambiental de dicho rubro, surge la idea de buscar una forma de reducir la contaminación sin descuidar las necesidades de las personas. Para ello, se llevará a cabo el siguiente proyecto para explorar las posibilidades de incorporar una flota de taxis eléctricos en NY.

## Descripción

El objetivo principal de este proyecto es analizar la viabilidad de implementar una flota de taxis eléctricos en Nueva York, considerando su impacto en la reducción de emisiones de CO2, la mejora de la calidad del aire y la reducción de la contaminación sonora.

## Conjunto de Datos

1. **Data de viajes**
2. **Dataset de Kaggle sobre emisiones de CO2 por país y año, con ajustes por población**
3. **Dataset de los sonidos recolectados en NYC**
4. **Dataset de la calidad del aire de NYC**
5. **Electric car and Fuel car**

## Propuesta 

**Limpieza y preparación de datos**:
* Se realizará un análisis exploratorio completo de los datos buscando valores faltantes, nulos, outliers, registros duplicados, tipos de datos y distribución. Se aplicarán técnicas adecuadas para tratar los casos de valores faltantes, como la eliminación de registros incompletos, eliminación de columna, o imputación de valores.
* Se verificará la consistencia y validez de los datos, asegurando que los valores estén dentro de rangos razonables y que no existan incoherencias.

**Análisis descriptivo**:
* Se utilizarán medidas de resumen como la media, mediana, moda, desviación estándar, rango y cuartiles para describir las variables numéricas.
Para las variables categóricas, se calcularán frecuencias y porcentajes, además de medidas de asociación como el chi-cuadrado o el índice de correlación de Cramer.
* Se elaborarán gráficos y tablas adecuados para visualizar la distribución de las variables y las relaciones entre ellas. Se utilizarán histogramas, diagramas de cajas, gráficos de barras y dispersión, entre otros.

**Base de Datos**
* Se implementará un sistema de gestión de base de datos en la nube, garantizando la normalización y alta calidad de los datos, buscando confiabilidad, precisión y facilidad de análisis. 
* El sistema de base de datos almacenará la información que será utilizada por dos subsistemas: un dashboard de visualización que presentará insights y KPIs de manera clara y atractiva, y un modelo de machine learning de inferencia o predicción que aprovechará los datos para generar pronósticos y análisis valiosos.

**Modelo de Aprendizaje Automático**:
* Se seleccionará dos modelos que estarán alineados a los objetivos, pero solo uno será implementado ajustados bien sus parámetros para una mejor predicción o inferencia, Este modelo será implementado utilizando el framework de python Streamlit, el segundo modelo quedará documentado.

### Limpieza y preparación de datos

* Realización de un análisis exploratorio completo de los datos buscando valores faltantes, nulos, outliers, registros duplicados, tipos de datos y distribución.
* Aplicación de técnicas adecuadas para tratar los casos de valores faltantes, como la eliminación de registros incompletos, eliminación de columna, o imputación de valores.
* Verificación de la consistencia y validez de los datos, asegurando que los valores estén dentro de rangos razonables y que no existan incoherencias.

### Análisis descriptivo

* Utilización de medidas de resumen como la media, mediana, moda, desviación estándar, rango y cuartiles para describir las variables numéricas.
* Cálculo de frecuencias y porcentajes para las variables categóricas, además de medidas de asociación como el chi-cuadrado o el índice de correlación de Cramer.
* Elaboración de gráficos y tablas adecuados para visualizar la distribución de las variables y las relaciones entre ellas, utilizando histogramas, diagramas de cajas, gráficos de barras y dispersión, entre otros.

### Base de Datos

* Implementación de un sistema de gestión de base de datos en la nube, garantizando la normalización y alta calidad de los datos, buscando confiabilidad, precisión y facilidad de análisis.
* El sistema de base de datos almacenará la información que será utilizada por dos subsistemas: un dashboard de visualización y un modelo de machine learning para inferencia o predicción.

### Modelo de Aprendizaje Automático

* Selección de dos modelos alineados a los objetivos, implementando solo uno ajustado correctamente para una mejor predicción o inferencia.
* Este modelo se implementará utilizando el framework de Python Streamlit, mientras que el segundo modelo quedará documentado.

## Objetivo General y Especificos

### Objetivo General

Evaluar la viabilidad y el impacto de la implementación de vehículos Eléctricos / Híbridos / Gasolina en la flota de transporte de pasajeros de la empresa, utilizando datos de viajes en taxis y servicios de transporte compartido en Nueva York, así como datos de calidad del aire, para proporcionar recomendaciones estratégicas basadas en análisis de datos robustos

### Objetivos Específicos

1. Evaluar la viabilidad económica de la implementación de distintos tipos de vehículos, considerando costos, rendimiento y retorno de inversión, entre otros factores.
2. Estudiar cómo la implementación de taxis alternativos mejora la calidad del aire en Nueva York, comparando datos de calidad del aire antes y después de la implementación.
3. Proporcionar un modelo de Machine Learning que ayude en distintos aspectos del proyecto, como el cálculo de tarifas de los viajes.
4. Comparar las emisiones de CO2 entre taxis tradicionales y taxis alternativos para analizar la viabilidad ambiental.
5. Analizar la demanda de taxis en diferentes zonas para poder focalizar la operación.
6. Brindar toda la información posible y útil al cliente para que pueda tomar decisiones informadas y basadas en datos.

## Indicadores claves de Desempeño

1. **TasaReducción_Carbono**: Reducir en un 50% la emisión de dióxido de carbono en comparación con los taxis tradicionales a gasolina.
   <center>
$\frac{\text{Cantidad de carbono emitida por taxis alternativos} - \text{Cantidad de carbono emitida por taxis tradicionales}}{\text{Cantidad de carbono emitida por taxis tradicionales}} \times 100$
</center>

2. **TasaGanancia_Bruta**: Superar en un 10% la tasa media de ganancia bruta con taxis alternativos respecto a los taxis tradicionales.

   <center>
$\frac{\text{Ganancia bruta taxis alternativos} - \text{Ganancia bruta taxis tradicionales}}{\text{Ganancia bruta taxis tradicionales}} \times 100$
</center>

3. **Tiempo_Retorno_Inversión**: Medir el retorno de inversión de la implementación de la flota de taxis.

   <center>
$\frac{\text{Inversión total} - \text{Ganancia bruta diaria}}{\text{Ganancia bruta diaria}}$
</center>

## Tecnologías Utilizadas

### Herramientas de Organización y Comunicación

* **Discord**: Para la comunicación en tiempo real y la colaboración en equipo.
* **Slack**: Para la gestión de conversaciones y la integración con otras herramientas.
* **Google Meet**: Para videoconferencias y reuniones virtuales.
* **Trello / Jira**: Para la gestión de proyectos y seguimiento de tareas.

### Herramientas de Trabajo en la Elaboración del ETL y el EDA

- **Git**: Para el control de versiones y la colaboración en el desarrollo de código.
- **Python**: Utilizado con librerías específicas para data science como Numpy, Pandas, Matplotlib, entre otras.

### Infraestructura Tecnológica para el Ciclo de Datos

**Propuesta 1**: Local

* **Docker**: Para la contenedorización y despliegue de aplicaciones.
* **Datalake Hadoop**: Para el almacenamiento y procesamiento de grandes volúmenes de datos.
* **Orquestador Airflow**: Para la gestión y procesamiento de grandes volúmenes de datos.
* **MySQL**: Para el almacenamiento y gestión de bases de datos relacionales.
* **Render (ML)**: Para el despliegue y ejecución de modelos de machine learning.

**Propuesta 2**: Servicios de la Nube

* **Lucidchart**: Como software de diagramación online.
* **Cloud Storage**: Para el almacenamiento de datos en la nube.
* **Cloud Functions**: Para la ejecución de código sin necesidad de gestionar servidores.
* **BigQuery**: Para el análisis y procesamiento de grandes conjuntos de datos.

### Herramientas para la Visualización de Datos

* **Power BI**: Para la creación de informes interactivos y dashboards.
* **Streamlit**: Para la creación de aplicaciones web interactivas y visualización de datos en tiempo real.

### Herramienta para Presentaciones Visuales

* **Prezi**: Para la creación de presentaciones dinámicas y visualmente atractivas.

### Justificación de Utilizar Google Cloud

Google Cloud ofrece una infraestructura escalable adaptable a las necesidades de crecimiento de cualquier organización. Un servicio Google Storage, para un Data Lake , que permite almacenar cantidades masivas de datos sin preocuparse por las limitaciones de capacidad. Además, Google BigQuery, como plataforma de analíticas de datos, que permite realizar consultas de manera rápida y eficiente, lo que es esencial para el análisis de grandes volúmenes de datos.
Google Cloud proporciona una integración entre distintos servicios. El proceso ETL/ELT que puede ser gestionado eficientemente utilizando herramientas como Google Cloud Dataflow, que permite el procesamiento de datos en tiempo real y por lotes. La compatibilidad de BigQuery con diversas herramientas de ETL/ELT garantiza que los datos sean procesados y transferidos sin problemas desde el data lake a BigQuery.

## Contribución

Por favor, sigue estas pautas para contribuir al proyecto:
1. Realiza un fork del repositorio.
2. Crea una nueva rama (`git checkout -b feature/nueva-feature`).
3. Realiza tus cambios y commitea (`git commit -m 'Añadir nueva feature'`).
4. Sube tus cambios (`git push origin feature/nueva-feature`).
5. Abre un Pull Request.

## Conclusión

## Recomendaciones

## Autores

La dedicación y el trabajo en equipo de estas personas hicieron posible la realización de este proyecto

| [<img src="https://avatars.githubusercontent.com/u/166193432?v=4" width=115><br><sub>Juan Camilo Torres Salas</sub>](https://github.com/JuankTS/JuankTS) | [<img src="https://avatars.githubusercontent.com/u/166779106?v=4" width=115><br><sub>Adrian Facundo Corvalan</sub>](https://github.com/facu-corvalan) | [<img src="https://avatars.githubusercontent.com/u/123128073?v=4" width=115><br><sub>Javier Yañez</sub>](https://github.com/javyleonhart) | [<img src="https://avatars.githubusercontent.com/u/163685041?v=4" width=115><br><sub>Michael Martinez</sub>](https://github.com/bkmay1417) | [<img src="https://avatars.githubusercontent.com/u/123877201?v=4" width=115><br><sub>Jesus H. Parra B.</sub>](https://github.com/ing-jhparra)
| :---: | :---: | :---: | :---: | :---: |
