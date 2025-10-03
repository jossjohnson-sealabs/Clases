def find_combinations(numbers, target, start_index, current_sum, current_combination, results):
    # Caso base: si la suma actual es igual al objetivo, agregar la combinación a los resultados
    if current_sum == target:
        results.append(list(current_combination))
        return

    # Si la suma actual excede el objetivo, retroceder
    if current_sum > target:
        return

    # Probar todos los números posibles desde start_index
    for i in range(start_index, len(numbers)):
        number = numbers[i]
        current_combination.append(number)  # Añadir el número a la combinación actual
        find_combinations(numbers, target, i, current_sum + number, current_combination, results)  # Recursión
        current_combination.pop()  # Retroceso: eliminar el último número añadido


def main(): 
    numbers = [2, 3, 6, 7]  # Conjunto de números
    target = 13  # Valor objetivo
    results = []  # Lista para almacenar las combinaciones válidas
    find_combinations(numbers, target, 0, 0, [], results)

    # Imprimir los resultados
    print("Combinaciones que suman a {}: ".format(target))
    for combination in results:
        print(combination)

# Ejecutar el programa
main()