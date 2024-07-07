# Explicación del proceso y entrenamiento del modelo de machine learning

<p align="center">
    <img src="https://becolve.com/wp-content/uploads/2023/04/grafico-machine-learning-min.png" width="600" height="300">
</p>

Para determinar qué modelo de Machine Learning usar, es importante tener en cuenta muchos factores, ya que dentro del mundo del ML hay una gran variedad de modelos que pueden ser útiles dependiendo del enfoque de tu caso.

Como empresa consultora designada para este proyecto, decidimos desarrollar una aplicación que utilice ML para predecir el precio de las tarifas de los viajes que ofrecerá nuestra empresa cliente. Esto lo hicimos con el fin de maximizar las ganancias de nuestro cliente sin dejar de lado la satisfacción del público por pagar un precio justo por el servicio ofrecido. Teniendo esto en cuenta, a continuación, les mostraremos el paso a paso que seguimos para llegar a nuestro modelo final.

## Selección de los datos

Este es el primer paso y, por lo tanto, un paso fundamental. Como nuestro objetivo es predecir el valor de las tarifas, es decir, un valor continuo de los viajes basándonos en ciertas características que puedan explicar su variabilidad (vea [aquí](https://github.com/ing-jhparra/nyc-taxis/blob/main/EDA/EDA_TaxisTrips.ipynb) para más información sobre estas características seleccionadas), usamos en este caso un enfoque de regresión. Necesitábamos un conjunto de datos etiquetados, los cuales fueron seleccionados desde esta [página](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page). Se seleccionaron mediante un muestreo aleatorio simple, entendiendo esto como una técnica de muestreo probabilístico donde cada individuo de la población tiene la misma probabilidad de ser seleccionado. Esto se hace para obtener una muestra que sea representativa de dicha población, por lo que tomamos los últimos 6 meses del año 2023 para no tener tanto problema con los precios y la inflación, y a ellos les aplicamos esta técnica.

<p align="center">
    <img src="https://deepnote.com/publish/5e3efaeb-d12c-472c-96b7-bb34e377b3e7/file?path=Muestreo-aleatorio-simple.jpg" width="600" height="300">
</p>

## Procesamiento y limpieza de los datos

Después de seleccionar los datos, pasamos a su procesamiento. En esta etapa, lo que se busca es dejar los datos lo más limpios posibles para entregárselos al modelo y que funcione de manera más óptima. En el caso de los valores nulos, como eran una pequeña cantidad, los eliminamos ya que no representaban una gran parte de la data. Se miraron las estadísticas básicas de la muestra, tales como la media, mínimos, máximos, entre otros, para detectar los valores atípicos y tratarlos. Para esto, se aplicó la regla empírica, quedándonos con los datos más concisos, por decirlo de algún modo, y así tener los datos mejor estructurados posibles.

<p align="center">
    <img src="https://www.dongee.com/tutoriales/content/images/2023/04/image-13.png" width="600" height="300">
</p>

## Entrenamiento y selección del modelo

Para ello, se entrenaron tres modelos: la regresión ridge, un árbol de decisión y un bosque aleatorio. Se entrenaron con los datos procesados y se evaluaron en función de tres métricas: el R², el error absoluto medio y el error medio cuadrado, además del coste computacional. Después de las evaluaciones y comparación de resultados, se escogió la regresión ridge como el modelo más óptimo para este caso (ver más información [aquí](https://github.com/ing-jhparra/nyc-taxis/blob/main/MachineLearning/ModelTraining.ipynb)). Una vez seleccionado el modelo, se guarda entrenado y estaría listo para recibir nuevos datos y hacer las predicciones.

<p align="center">
    <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTJB9grk5pmHHxoz7m95_ixjOyLhGzsXxhhlQ&s" width="600" height="300">
</p>

De esta forma se llevó a cabo nuestro proceso de entrenamiento y selección del modelo para nuestra aplicación.

