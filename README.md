# Redes Bayesianas

Una librería para construir redes bayesianas y realizar inferencia probabilística.

## Instalación

Con el manejador de paquetes pip:
\_pip install redes_bayesianas

## Uso

<sub> 
    import redes_bayesianas

    # Crea una red bayesiana
    red_bayesiana = mi_libreria_python.BayesianNetwork()
    red_bayesiana.add_node("clima", ["soleado", "nublado", "lluvioso"], [0.6, 0.3, 0.1])
    red_bayesiana.add_node("temperatura", ["caliente", "templada", "fria"], [0.4, 0.5, 0.1])
    red_bayesiana.add_edge("clima", "temperatura", [[0.8, 0.2, 0], [0.4, 0.5, 0.1], [0.2, 0.4, 0.4]])

    # Realiza inferencia probabilística
    inference = mi_libreria_python.Inference(red_bayesiana)
    resultados = inference.probability("temperatura", {"clima": "soleado"})
    print(resultados)

</sub>

## API

Se incluyen las siguientes clases

### Clase BayesianNetwork

#### add_node(nombre, valores, probabilidades): Agrega un nodo a la red bayesiana con el nombre especificado, los valores posibles y las probabilidades iniciales.

#### add_edge(nodo_padre, nodo_hijo, probabilidades): Agrega una relación entre dos nodos de la red bayesiana, especificando las probabilidades condicionales.

### Clase Inference

#### probability(nodo, evidencias): Devuelve la distribución de probabilidad de un nodo dado un conjunto de evidencias.
