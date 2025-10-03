import random

# Parámetros del problema
pesos = [2, 3, 5, 7, 1]  # Pesos de los objetos
valores = [10, 5, 15, 7, 6]  # Valores de los objetos
capacidad_mochila = 15  # Capacidad máxima de la mochila
NUM_INDIVIDUOS = 10  # Tamaño de la población
NUM_GENERACIONES = 30  # Número de generaciones
PROB_CRUCE = 0.8  # Probabilidad de cruce
PROB_MUTACION = 0.1  # Probabilidad de mutación

# Generar un individuo aleatorio (solución binaria)
def generar_individuo():
    return [random.randint(0, 1) for _ in range(len(pesos))]

# Crear la población inicial de individuos
def generar_poblacion():
    return [generar_individuo() for _ in range(NUM_INDIVIDUOS)]

# Función de aptitud: calcula el valor total y penaliza si el peso total excede la capacidad
def funcion_adaptabilidad(individuo):
    valor_total = sum(individuo[i] * valores[i] for i in range(len(individuo)))
    peso_total = sum(individuo[i] * pesos[i] for i in range(len(individuo)))
    if peso_total > capacidad_mochila:
        return 0  # Penalización por exceder la capacidad
    return valor_total

# Selección: selecciona dos padres usando el método de torneo
def seleccion_por_torneo(poblacion):
    seleccionados = random.sample(poblacion, 3)
    seleccionados.sort(key=lambda x: funcion_adaptabilidad(x), reverse=True)
    return seleccionados[0], seleccionados[1]

# Cruce entre dos padres
def cruce(padre1, padre2):
    if random.random() < PROB_CRUCE:
        punto_cruce = random.randint(1, len(padre1) - 1)
        hijo = padre1[:punto_cruce] + padre2[punto_cruce:]
        return hijo
    else:
        return padre1

# Mutación de un individuo
def mutacion(individuo):
    if random.random() < PROB_MUTACION:
        indice = random.randint(0, len(individuo) - 1)
        individuo[indice] = 1 - individuo[indice]  # Cambia de 1 a 0 o de 0 a 1
    return individuo

# Algoritmo genético
def algoritmo_genetico():
    # Crear la población inicial
    poblacion = generar_poblacion()
    mejor_solucion = None
    mejor_adaptabilidad = float('-inf')

    # Iterar sobre el número de generaciones
    for generacion in range(NUM_GENERACIONES):
        # Evaluar adaptabilidad y encontrar el mejor individuo
        poblacion.sort(key=lambda x: funcion_adaptabilidad(x), reverse=True)
        mejor_individuo = poblacion[0]
        mejor_fitness = funcion_adaptabilidad(mejor_individuo)

        # Imprimir el mejor de esta generación
        print(f"Generación {generacion + 1}: Mejor individuo = {mejor_individuo}, Valor = {mejor_fitness}")

        # Actualizar la mejor solución global
        if mejor_fitness > mejor_adaptabilidad:
            mejor_adaptabilidad = mejor_fitness
            mejor_solucion = mejor_individuo

        # Crear nueva generación
        nueva_poblacion = []
        while len(nueva_poblacion) < NUM_INDIVIDUOS:
            # Selección de padres
            padre1, padre2 = seleccion_por_torneo(poblacion)
            # Cruce para generar un hijo
            hijo = cruce(padre1, padre2)
            # Mutación del hijo
            hijo_mutado = mutacion(hijo)
            nueva_poblacion.append(hijo_mutado)

        poblacion = nueva_poblacion

    # Mostrar el resultado final
    print(f"\nMejor solución encontrada: {mejor_solucion}, Valor = {mejor_adaptabilidad}")

# Ejecutar el algoritmo
algoritmo_genetico()