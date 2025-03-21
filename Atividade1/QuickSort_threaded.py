import random
import threading
import time

# Função principal do QuickSort

def quicksort(arr):

    if len(arr) <= 1:
        return arr

    pivot = arr[-1]
    left = [x for x in arr[:-1] if x <= pivot] # Elementos menores ou iguais ao pivô
    right = [x for x in arr[:-1] if x > pivot] # Elementos maiores que o pivô

    sorted_left = []
    sorted_right = []

    left_thread = threading.Thread(target=lambda: sorted_left.extend(quicksort(left)))
    right_thread = threading.Thread(target=lambda: sorted_right.extend(quicksort(right)))

    left_thread.start()
    right_thread.start()
    left_thread.join()
    right_thread.join()

    return sorted_left + [pivot] + sorted_right

# Função para gerar números aleatórios

def gerar_numeros_aleatorios(n=100, min_val=1, max_val=200):
    return [random.randint(min_val, max_val) for _ in range(n)]

# Função principal para testar o QuickSort

if __name__ == "__main__":
    numeros = gerar_numeros_aleatorios()
    print("Primeiros 10 números antes da ordenação:", numeros[:10])

    start_time = time.time()

    numeros_ordenados = quicksort(numeros)
    print("Primeiros 10 números após a ordenação:", numeros_ordenados[:10])

    end_time = time.time()
    print("Tempo de execução:", end_time - start_time)