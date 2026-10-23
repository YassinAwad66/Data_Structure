from ..Assignment1.sorting import OnSquareSorting
import time
import random

def max_heap(arr, i, heap_size=None):
    if heap_size is None:
        heap_size = len(arr)
    largest = i
    left = 2*i + 1
    right = 2*i + 2

    if left < heap_size and arr[left] > arr[largest]:
        largest = left
    if right < heap_size and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heap(arr, largest, heap_size)

def build_max_heap(arr):
    for i in range(len(arr)//2 - 1, -1, -1):
        max_heap(arr, i)

def heap_sort(arr):
    start_time = time.time()
    build_max_heap(arr)
    for i in range(len(arr)-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        max_heap(arr, 0, i)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Sorting array of size {len(arr)} using heap sort in time: {elapsed_time}")
    return elapsed_time

def randomized_partition(arr, low, high):
    pivot_index = random.randint(low, high)
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def randomized_quick_sort(arr, low, high):
    if low < high:
        pi = randomized_partition(arr, low, high)
        randomized_quick_sort(arr, low, pi - 1)
        randomized_quick_sort(arr, pi + 1, high)

def main():
    N_sizes = [100, 500, 1000, 2000, 5000]
    sorting_times = {
        "Bubble sort": [],
        "Selection sort": [],
        "Insertion sort": [],
        "Heap sort": [],
        "Randomized quick sort": [],
    }
    sorters = {
        "Bubble sort": OnSquareSorting.bubble_sort,
        "Selection sort": OnSquareSorting.selection_sort,
        "Insertion sort": OnSquareSorting.insertion_sort,
        "Heap sort": heap_sort,
    }

    for size in N_sizes:
        arr = OnSquareSorting.generate_random_array(size)
        expected = sorted(arr)

        for algorithm_name, sorter in sorters.items():
            candidate = arr.copy()
            elapsed_time = sorter(candidate)
            if candidate != expected:
                raise RuntimeError(f"{algorithm_name} produced an incorrectly sorted array")
            sorting_times[algorithm_name].append(elapsed_time)

        candidate = arr.copy()
        start_time = time.perf_counter()
        randomized_quick_sort(candidate, 0, len(candidate) - 1)
        elapsed_time = time.perf_counter() - start_time
        if candidate != expected:
            raise RuntimeError("Randomized quick sort produced an incorrectly sorted array")
        print(
            f"Sorting array of size {len(arr)} using randomized quick sort "
            f"in time: {elapsed_time}"
        )
        sorting_times["Randomized quick sort"].append(elapsed_time)

    OnSquareSorting.draw_graph(N_sizes, sorting_times)


if __name__ == "__main__":
    main()