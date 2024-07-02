#  Análisis de la Implementación de Vehículos Eléctricos en el Transporte de Pasajeros en NYC
<p align="center">
   <br />
   <img src="img\Logo_cliente.jpeg" width="55%">
   <br />
</p>

## Contextualización 

Sabemos que la movilidad en las ciudades es un tema importante, el tránsito de vehículos en New York no es la excepción, se ha aumentado la demanda de taxis y con ella se han visto afectadas otras dimesiones, como ejemplo tenemos el transporte, que es el sector que más emisiones de CO2 produce en Estados Unidos. Por esto y para mitigar su impacto ambiental sin descuidar las necesidades de transporte, este proyecto explotarará la incorporación de una flota de taxis eléctricos en New York.

## Nuestro Rol
<p>Gendata, como empresa consultora designada para este espectacular proyecto, nos hemos propuesto abarcar desde todas las perspectivas: ingeniería, análisis y ciencia de datos, para entregar un producto completo para nuestro cliente y su público objetivo.</p>
 <p>Nos dedicamos a diseñar soluciones innovadoras y eficientes, asegurando la máxima calidad en cada etapa del proyecto. Hacemos todo con el fin proporcionar insights valiosos y facilitar la toma de decisiones que informadas que conlleven a una mejora significativa para nuestros clientes.</p>

<p align = 'center'><img src="img/LogoGendata.jpeg" width=300 height=300> </p>


## Objetivo General

Evaluar la viabilidad y el impacto de la implementación de vehículos Eléctricos / Híbridos / Gasolina en la flota de transporte de pasajeros de la empresa, utilizando datos de viajes en taxis y servicios de transporte compartido en Nueva York, así como datos de calidad del aire, para proporcionar recomendaciones estratégicas basadas en análisis de datos robustos

## Objetivos Específicos

1. Evaluar la viabilidad económica de la implementación de distintos tipos de vehículos, considerando costos, rendimiento y retorno de inversión, entre otros factores.
2. Estudiar cómo la implementación de taxis alternativos mejora la calidad del aire en Nueva York, comparando datos de calidad del aire antes y después de la implementación.
3. Proporcionar un modelo de Machine Learning que ayude en distintos aspectos del proyecto, como el cálculo de tarifas de los viajes.
4. Comparar las emisiones de CO2 entre taxis tradicionales y taxis alternativos para analizar la viabilidad ambiental.
5. Analizar la demanda de taxis en diferentes zonas para poder focalizar la operación.
6. Brindar toda la información posible y útil al cliente para que pueda tomar decisiones informadas y basadas en datos.

## Conjunto de Datos
Para este proyecto usaremos distintos datos, que nos permitan englobar desde las áreas este proyecto:
1. **Data de viajes**
2. **Dataset de Kaggle sobre emisiones de CO2 por país y año, con ajustes por población**
3. **Dataset de los sonidos recolectados en NYC**
4. **Dataset de la calidad del aire de NYC**
5. **Electric car and Fuel car**

## Propuesta 

**Esquema de datos en la nube**: Un sistema organizado de almacenamiento y procesamiento de datos en la nube, donde se gestionará la información y se distribuirá a los componentes necesarios.

**Aplicativo de Machine Learning**: Una aplicación basada en Machine Learning que funcionará como calculadora de tarifas de viajes, ajustando el precio en función de la distancia y el tiempo del recorrido, garantizando así un costo justo para cada viaje.

**Dashboard interactivo**: Un tablero de control interactivo que presentará información relevante basada en los KPI definidos, promoviendo una toma de decisiones informada y efectiva.

<div style="display: flex; justify-content: center;">
    <img align="center "src="img/logos.png" alt="Imagen 3" width="51%" height="51%">
</div>

## Tecnologías Utilizadas

### Herramientas de Organización y Comunicación

<img src="https://assets-global.website-files.com/6257adef93867e50d84d30e2/636e0a6a49cf127bf92de1e2_icon_clyde_blurple_RGB.png" width="20px" > **Discord**: Para la comunicación en tiempo real y la colaboración en equipo.

<img src="img\Slack.png" width="20px"> **Slack**: Para la gestión de conversaciones y la integración con otras herramientas.

<img src="https://www.uc3m.es/sdic/media/sdic/img/mediana/original/im_servicios_comunicacion_google-meet_icono/im_servicios_comunicacion_google_meet.png" width="20px" height="20px"> **Google Meet**: Para videoconferencias y reuniones virtuales.

<img src="img\Jira.png" width="20px"> **Trello / Jira**: Para la gestión de proyectos y seguimiento de tareas.

### Herramientas de Trabajo en la Elaboración del ETL y el EDA

<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/git/git-original.svg" width="20px" height="20px" alt="git logo"  />  **Git**: Para el control de versiones y la colaboración en el desarrollo de código.

<img src="https://cdn3.emoji.gg/emojis/9794-python.png" width="20px" height="20px" alt="python"></a> **Python**: Utilizado con librerías específicas para data science como Numpy, Pandas, Matplotlib, entre otras.

### Infraestructura Tecnológica para el Ciclo de Datos

**Propuesta 1**: Local

* **Docker**: Para la contenedorización y despliegue de aplicaciones.
* **Datalake Hadoop**: Para el almacenamiento y procesamiento de grandes volúmenes de datos.
* **Orquestador Airflow**: Para la gestión y procesamiento de grandes volúmenes de datos.
* **MySQL**: Para el almacenamiento y gestión de bases de datos relacionales.
* **Render (ML)**: Para el despliegue y ejecución de modelos de machine learning.

**Propuesta 2**: Servicios de la Nube

<div style="display: flex; justify-content:space-between;">
        <img src="img/Arquitectura.png" alt="Imagen 3" width="800" height="350">
</div>
</br>

* **Lucidchart**: Como software de diagramación online.
* **Cloud Storage**: Para el almacenamiento de datos en la nube.
* **Cloud Functions**: Para la ejecución de código sin necesidad de gestionar servidores.
* **BigQuery**: Para el análisis y procesamiento de grandes conjuntos de datos.

### Herramientas para la Visualización de Datos

<img src="img\PowerBi.png" width="30px"> **Power BI**: Para la creación de informes interactivos y dashboards.

<img src="img\streamlit-removebg-preview.png" width="30px"> **Streamlit**: Para la creación de aplicaciones web interactivas y visualización de datos en tiempo real.

### Herramienta para Presentaciones Visuales

<img src="img\Prezi_logo.png" width="20px"> **Prezi**: Para la creación de presentaciones dinámicas y visualmente atractivas.

### Justificación de Utilizar Google Cloud

Google Cloud ofrece una infraestructura escalable adaptable a las necesidades de crecimiento de cualquier organización. Un servicio Google Storage, para un Data Lake , que permite almacenar cantidades masivas de datos sin preocuparse por las limitaciones de capacidad. Además, Google BigQuery, como plataforma de analíticas de datos, que permite realizar consultas de manera rápida y eficiente, lo que es esencial para el análisis de grandes volúmenes de datos.
Google Cloud proporciona una integración entre distintos servicios. El proceso ETL/ELT que puede ser gestionado eficientemente utilizando herramientas como Google Cloud Dataflow, que permite el procesamiento de datos en tiempo real y por lotes. La compatibilidad de BigQuery con diversas herramientas de ETL/ELT garantiza que los datos sean procesados y transferidos sin problemas desde el data lake a BigQuery.

## Distribución la tareas en la semanas

Adoptamos SCRUM con reuniones diarias para revisar el avance y organizar las actividades. Empleamos un gráfico de Gantt y Jira para representar las tareas, sus tiempos y relaciones, lo que simplifica la organización y monitoreo del proyecto. Además, hemos dividido el proyecto en tres sprints para una gestión más efectiva y un seguimiento más detallado de cada fase

### Sprint 1

Durante el primer sprint del proyecto, nos enfocamos en establecer una base sólida para el desarrollo del producto final. Utilizamos técnicas avanzadas de ciencia de datos y análisis para maximizar el valor entregado al cliente y su público objetivo. Se seleccionaron tecnologías adecuadas para manejar eficientemente los datos, se exploraron modelos de machine learning para predecir tarifas de taxi y se organizó una estructura de trabajo clara para asegurar un flujo de trabajo ordenado y eficaz. Este sprint sentó las bases para futuros desarrollos y refinamientos del producto.

<a href="https://prezi.com/view/pvweYTGST5krJY1gnDmv/">
    <img src="img\Prezi_logo.png" width="40px"> 
    <strong style="font-size: 1.2em;">Presentación primer sprint</strong>
</a>

### Sprint 2
Durante este sprint, hemos avanzado significativamente en el proyecto mediante la incorporación de funciones complejas adicionales y la respuesta a las necesidades específicas planteadas por el Product Owner. Se ha desarrollado un proceso automatizado y unificado para la extracción, transformación y carga de datos, garantizando la reproducibilidad y eficiencia en todas las etapas. Además, hemos delineado un ciclo completo del dato, desde la captura inicial hasta su análisis y disponibilidad para su uso en aplicaciones de machine learning y dashboards, hemos implementado un pipeline end-to-end diseñado para adaptarse a las necesidades del proyecto, utilizando herramientas de orquestación para gestionar de manera eficiente las tareas críticas del proceso. Este sprint ha fortalecido significativamente la infraestructura de datos del proyecto, proporcionando una base sólida y escalable para futuros desarrollos y mejoras.


<a href="https://docs.google.com/presentation/d/1VRstjEbTX15bOQhK2bVjOZgtzYu7yK3clcrjbERmqiY/edit?usp=sharing">
    <img src="img\PowerPoint.png" width="40px"> 
    <strong style="font-size: 1.2em;">Presentación segundo sprint</strong>
</a>

### Sprint 3

Se ha puesto un énfasis especial en el diseño visual del dashboard, asegurando que los colores, gráficos y elementos visuales estén adecuadamente adaptados al tipo de datos y escala apropiada. Se ha empleado una jerarquía visual clara para destacar la información más relevante y se han utilizado técnicas de diseño para guiar la atención del usuario hacia los elementos clave.

El dashboard resultante es interactivo y permite explorar los datos de manera intuitiva. Los filtros, selecciones y acciones implementadas mejoran la experiencia del usuario y facilitan el análisis de datos estratégicos. Se han integrado al menos tres KPIs bien formulados que reflejan el enfoque del negocio, presentados de manera efectiva en visualizaciones adecuadas

Finalmente, el modelo de machine learning se encuentra deployado en la web, accesible a través de una interfaz gráfica tipo Streamlit. Esta implementación asegura que la salida del modelo pueda ser consumida por otros componentes del proyecto de manera efectiva.


## Contribución

Por favor, sigue estas pautas para contribuir al proyecto:
1. Realiza un fork del repositorio.
2. Crea una nueva rama (`git checkout -b feature/nueva-feature`).
3. Realiza tus cambios y commitea (`git commit -m 'Añadir nueva feature'`).
4. Sube tus cambios (`git push origin feature/nueva-feature`).
5. Abre un Pull Request.

## Autores

La dedicación y el trabajo en equipo de Gendata, estas personas hicieron posible la realización de este proyecto.

| [<img src="https://avatars.githubusercontent.com/u/166193432?v=4" width=115><br><sub>Juan Camilo Torres Salas</sub>](https://github.com/JuankTS/JuankTS) | [<img src="https://avatars.githubusercontent.com/u/166779106?v=4" width=115><br><sub>Adrian Facundo Corvalan</sub>](https://github.com/facu-corvalan) | [<img src="https://avatars.githubusercontent.com/u/123128073?v=4" width=115><br><sub>Javier Yañez</sub>](https://github.com/javyleonhart) | [<img src="https://avatars.githubusercontent.com/u/163685041?v=4" width=115><br><sub>Michael Martinez</sub>](https://github.com/bkmay1417) | [<img src="https://avatars.githubusercontent.com/u/123877201?v=4" width=115><br><sub>Jesus H. Parra B.</sub>](https://github.com/ing-jhparra)
| :---: | :---: | :---: | :---: | :---: |
