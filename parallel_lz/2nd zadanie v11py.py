import time
import math
import multiprocessing

def factorial(n):
    return math.factorial(n)

def multi(numbers):
    with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
        results = pool.map(factorial, numbers)
    return results

def solo(numbers):
    return [factorial(n) for n in numbers]

def main():
    numbers = list(range(1, 501))

    start_time = time.time()
    parallel_results = multi(numbers)
    parallel_time = time.time() - start_time

    start_time = time.time()
    sequential_results = solo(numbers)
    sequential_time = time.time() - start_time

    print(f"\nПараллельное вычисление : {parallel_time:.4f} сек.")
    print(f"Последовательное вычисление : {sequential_time:.4f} сек.\n")

    print("Первые 100 результатов:")
    for i in range(100):
        print(f"{i + 1}! = {sequential_results[i]}")

if __name__ == "__main__":
    main()
