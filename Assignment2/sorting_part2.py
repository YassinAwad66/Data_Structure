from Assignment1.sorting import OnSquareSorting
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
    build_max_heap(arr)
    for i in range(len(arr)-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        max_heap(arr, 0, i)

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

def merge(left ,right):
    result=[]
    i=j=0
    while(i<len(left)and j<len(right)):
        if(left[i]<=right[j]):
            result.append(left[i])
            i+=1
        else:   
            result.append(right[j])
            j+=1     
    result.extend(left[i:])
    result.extend(right[j:])    
    return result

def merge_sort(arr):
    if(len(arr)<=1):
        return arr
    mid=len(arr)//2
    left=merge_sort(arr[:mid])
    right=merge_sort(arr[mid:])
    return merge(left, right)

def hybrid_merge_sort(arr,cutoff=16):
    if len(arr) <= cutoff:
        OnSquareSorting.selection_sort(arr)
        return arr
    mid = len(arr) // 2
    left = hybrid_merge_sort(arr[:mid], cutoff)
    right = hybrid_merge_sort(arr[mid:], cutoff)
    return merge(left, right)


def main():
    N_sizes = [10000, 20000, 30000, 40000, 50000]
    sorters = {
        "Bubble sort": OnSquareSorting.bubble_sort,
        "Selection sort": OnSquareSorting.selection_sort,
        "Insertion sort": OnSquareSorting.insertion_sort,
        "Heap sort": heap_sort,
        "Randomized quick sort": lambda arr: randomized_quick_sort(
            arr, 0, len(arr) - 1
        ),
        "Merge sort": merge_sort,
        "Hybrid merge sort": hybrid_merge_sort,
    }
    sorting_times = {algorithm_name: [] for algorithm_name in sorters}

    for size in N_sizes:
        arr = OnSquareSorting.generate_random_array(size)
        expected = sorted(arr)

        for algorithm_name, sorter in sorters.items():
            candidate = arr.copy()
            start_time = time.perf_counter()
            sorted_candidate = sorter(candidate)
            elapsed_time = (time.perf_counter() - start_time)*1000
            if sorted_candidate is not None:
                candidate = sorted_candidate
            if candidate != expected:
                raise RuntimeError(f"{algorithm_name} produced an incorrectly sorted array")
            sorting_times[algorithm_name].append(elapsed_time)
            print(
                f"Sorting array of size {len(candidate)} using {algorithm_name.lower()} "
                f"in time: {elapsed_time}"
            )

    OnSquareSorting.draw_graph(N_sizes, sorting_times)


if __name__ == "__main__":
    main()