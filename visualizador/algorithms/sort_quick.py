def quick_sort(arr):
    # Caso base: si el arreglo tiene 0 o 1 elemento, ya está ordenado
    if len(arr) <= 1:
        return arr

    # 1. Seleccionar un pivote (aquí se elige el último elemento)
    pivote = arr[-1]

    # 2. Partición: crear las sublistas
    menores = []
    mayores = []
    
    # Iteramos sobre todos los elementos EXCEPTO el pivote
    for x in arr[:-1]:
        if x <= pivote:
            menores.append(x)
        else:
            mayores.append(x)
            
    # 3. Recursión: ordenar las sublistas y combinarlas
    # Se concatenan: sublista_menores + [pivote] + sublista_mayores
    return quick_sort(menores) + [pivote] + quick_sort(mayores)

# Ejemplo de uso:
lista = [10, 7, 8, 9, 1, 5]
lista_ordenada = quick_sort(lista)
print(f"Lista original: {lista}")
print(f"Lista ordenada: {lista_ordenada}") # Salida: [1, 5, 7, 8, 9, 10]