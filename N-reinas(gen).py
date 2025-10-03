import random

# Parámetros del algoritmo genético
N = 8  # Tamaño del tablero N x N
P_SIZE = 100  # Tamaño de la población
MUTATION_RATE = 0.1  # Tasa de mutación
GENERATIONS = 1000  # Número de generaciones

# Función para generar un individuo aleatorio
def generate_individual():
    return random.sample(range(N), N)

# Función de fitness: cuenta cuántos pares de reinas no se atacan
def fitness(individual):
    non_attacking_pairs = 0
    total_pairs = N * (N - 1) // 2
    
    for i in range(N):
        for j in range(i + 1, N):
            # Si no están en la misma columna ni en la misma diagonal
            if individual[i] != individual[j] and abs(individual[i] - individual[j]) != abs(i - j):
                non_attacking_pairs += 1
                
    return non_attacking_pairs

# Selección por torneo
def selection(population, fitnesses):
    tournament = random.sample(range(len(population)), 3)
    best = tournament[0]
    for i in tournament[1:]:
        if fitnesses[i] > fitnesses[best]:
            best = i
    return population[best]

# Cruce de un punto
def crossover(parent1, parent2):
    point = random.randint(1, N - 1)
    child1 = parent1[:point] + [gene for gene in parent2 if gene not in parent1[:point]]
    child2 = parent2[:point] + [gene for gene in parent1 if gene not in parent2[:point]]
    return child1, child2

# Mutación: intercambiar dos posiciones
def mutate(individual):
    if random.random() < MUTATION_RATE:
        i, j = random.sample(range(N), 2)
        individual[i], individual[j] = individual[j], individual[i]

# Algoritmo genético principal
def genetic_algorithm():
    population = [generate_individual() for _ in range(P_SIZE)]
    for generation in range(GENERATIONS):
        # Evaluar fitness de la población
        fitnesses = [fitness(ind) for ind in population]
        
        # Si encontramos una solución óptima
        if max(fitnesses) == N * (N - 1) // 2:
            print(f"Solución encontrada en la generación {generation}:")
            solution = population[fitnesses.index(max(fitnesses))]
            print(solution)
            return solution
        # Crear nueva población
        new_population = []
        for _ in range(P_SIZE // 2):
            # Seleccionar dos padres
            parent1 = selection(population, fitnesses)
            parent2 = selection(population, fitnesses)
            # Realizar cruce y mutación
            child1, child2 = crossover(parent1, parent2)
            mutate(child1)
            mutate(child2)
            new_population.extend([child1, child2])
        
        # Reemplazar población antigua con la nueva
        population = new_population
    
    return None

# Ejecutar el algoritmo genético
genetic_algorithm()

# Análisis del Algoritmo:
#
# Población inicial: Se genera una población de soluciones aleatorias.
#
# Evaluación de fitness: Se evalúa cada solución en función de cuántos pares de reinas no se atacan entre sí.
#
# Selección: Los individuos con mejor fitness tienen una mayor probabilidad de ser seleccionados para la reproducción.
#
# Cruce y mutación: Se combinan las soluciones seleccionadas para generar nuevas soluciones, y se mutan algunas de ellas para introducir diversidad.
#
# Generaciones: El proceso continúa hasta que se encuentra una solución válida o se alcanzan el número máximo de generaciones.