import matplotlib.pyplot as plt
import time
import random

class OnSquareSorting:
    def generate_random_array(size):
        return [random.randint(0, 100000) for _ in range(size)]

    def bubble_sort(arr):
        n=len(arr)
        for i in range(n):
            swapped= False
            for j in range(0, n-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    swapped = True
            if not swapped:
                break    

    def selection_sort(arr):
        for i in range(len(arr)):
            min_idx = i
            for j in range(i + 1, len(arr)):
                if arr[j] < arr[min_idx]:
                    min_idx = j
            if min_idx != i:
                arr[i], arr[min_idx] = arr[min_idx], arr[i]

    def insertion_sort(arr):
        n=len(arr)
        for i in range(1,n):
            key=arr[i]
            j=i-1
            while j>=0 and arr[j]>key:
                arr[j+1]=arr[j]
                j-=1
            arr[j+1]=key 

    @staticmethod
    def draw_graph(N_sizes, sorting_times):
        plt.figure(figsize=(10, 6))

        for algorithm_name, execution_times in sorting_times.items():
            plt.plot(
                N_sizes,
                execution_times,
                marker="o",
                linewidth=2,
                label=algorithm_name
            )

        plt.yscale("log")
        plt.xlabel("Input size (N)", fontweight="bold")
        plt.ylabel("Execution time (msec)", fontweight="bold")
        plt.title("Sorting Algorithms Performance (logarithmic scale)")
        plt.grid(True, alpha=0.3)
        plt.legend(loc="best", frameon=False)
        plt.xticks(N_sizes)
        plt.tight_layout()
        plt.show()


def main():
    N_sizes = [10000, 20000, 30000, 40000, 50000]
    bubble_sort_times = []
    selection_sort_times = []
    insertion_sort_times = []

    for size in N_sizes:
        arr = OnSquareSorting.generate_random_array(size)

        # Measure bubble sort time
        candidate = arr.copy()
        start_time = time.perf_counter()
        OnSquareSorting.bubble_sort(candidate)
        elapsed_time = (time.perf_counter() - start_time) * 1000
        print(f"Sorting array of size {len(candidate)} using bubble sort in time: {elapsed_time}")
        bubble_sort_times.append(elapsed_time)

        # Measure selection sort time
        candidate = arr.copy()
        start_time = time.perf_counter()
        OnSquareSorting.selection_sort(candidate)
        elapsed_time = (time.perf_counter() - start_time) * 1000
        print(f"Sorting array of size {len(candidate)} using selection sort in time: {elapsed_time}")
        selection_sort_times.append(elapsed_time)

        # Measure insertion sort time
        candidate = arr.copy()
        start_time = time.perf_counter()
        OnSquareSorting.insertion_sort(candidate)
        elapsed_time = (time.perf_counter() - start_time) * 1000
        print(f"Sorting array of size {len(candidate)} using insertion sort in time: {elapsed_time}")
        insertion_sort_times.append(elapsed_time)

    OnSquareSorting.draw_graph(
        N_sizes,
        {
            "Bubble sort": bubble_sort_times,
            "Selection sort": selection_sort_times,
            "Insertion sort": insertion_sort_times,
        },
    )


if __name__ == "__main__":
    main()