import matplotlib.pyplot as plt
import time
import random

class OnSquareSorting:
    def generate_random_array(size):
        return [random.randint(0, 100000) for _ in range(size)]

    def bubble_sort(arr):
        s_time = time.time()
        n=len(arr)
        for i in range(n):
            swapped= False
            for j in range(0, n-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    swapped = True
            if not swapped:
                break    
        e_time = time.time()
        elapsed_time= e_time - s_time
        print(f"Sorting array of size {len(arr)} using bubble sort in time: {elapsed_time}")
        return elapsed_time

    def selection_sort(arr):
        start_time = time.time()
        # Implementation for selection sort
        for i in range(len(arr)):
            min_idx = i
            for j in range(i + 1, len(arr)):
                if arr[j] < arr[min_idx]:
                    min_idx = j
            if min_idx != i:
                arr[i], arr[min_idx] = arr[min_idx], arr[i]
        end_time = time.time()
        timee = end_time - start_time
        print(f"Sorting array of size {len(arr)} using selection sort in time: {timee}")
        return timee

    def insertion_sort(arr):
        s_time = time.time()
        n=len(arr)
        for i in range(1,n):
            key=arr[i]
            j=i-1
            while j>=0 and arr[j]>key:
                arr[j+1]=arr[j]
                j-=1
            arr[j+1]=key 
        e_time = time.time()
        elapsed_time= e_time - s_time
        print(f"Sorting array of size {len(arr)} using insertion sort in time: {elapsed_time}")
        return elapsed_time

    @staticmethod
    def draw_graph(N_sizes, sorting_times):
        plt.figure(figsize=(10, 5))

        for algorithm_name, execution_times in sorting_times.items():
            plt.plot(
                N_sizes,
                execution_times,
                marker="o",
                linewidth=2,
                label=algorithm_name
            )

        plt.xlabel("Input size (N)", fontweight="bold")
        plt.ylabel("Execution time (sec)", fontweight="bold")
        plt.title("Sorting Algorithms Performance")
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
        bubble_start_time = OnSquareSorting.bubble_sort(arr.copy())
        bubble_sort_times.append(bubble_start_time)

        # Measure selection sort time
        selection_start_time = OnSquareSorting.selection_sort(arr.copy())
        selection_sort_times.append(selection_start_time)

        # Measure insertion sort time
        insertion_start_time = OnSquareSorting.insertion_sort(arr.copy())
        insertion_sort_times.append(insertion_start_time)

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