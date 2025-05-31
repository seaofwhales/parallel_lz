import time
import threading
import queue

def queuecheck(index, progress):
    time.sleep(2)
    progress.put(1)

def main():
    num_elements = 50
    threads = []
    progress = queue.Queue()

    print("Начало обработки элементов")

    for i in range(1, num_elements + 1):
        thread = threading.Thread(target=queuecheck, args=(i, progress))
        threads.append(thread)
        thread.start()

    element = 0
    while element < num_elements:
        progress.get()
        element += 1
        print(f"Обработано элементов: {element}/ {num_elements }")
        time.sleep(0.2)


    for thread in threads:
        thread.join()

    print("Обработка завершена")

if __name__ == "__main__":
    main()
