import matplotlib.pyplot as plt
import time
import random

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
    print(f"Sorting array of size {len(arr)} using insertion sort in time: {time}")

def draw_graph(N_sizes, bubble_sort, selection_sort, insertion_sort):
    # Create the figure
    plt.figure(figsize=(10, 5)) 

    # Plot each sorting algorithm
    plt.plot(
        N_sizes, bubble_sort,
            color="royalblue",
            marker="o",
            linewidth=2,
        label="Bubble sort"
    )

    plt.plot(
        N_sizes, selection_sort,
        color="red",
        marker="o",
        linewidth=2,
        label="Selection sort"
    )

    plt.plot(
        N_sizes, insertion_sort,
        color="orange",
        marker="o",
        linewidth=2,
        label="Insertion sort"
    )

    # Labels
    plt.xlabel("Input size (N)", fontweight="bold")
    plt.ylabel("Execution time (microsec)", fontweight="bold")

    # Title
    plt.title("Sorting Algorithms Performance")

    # Grid
    plt.grid(True, alpha=0.3)

    # Legend
    plt.legend(loc="upper center", ncol=3, frameon=False)

    # Format x-axis
    plt.xticks([0, 25000, 50000, 75000, 100000])

    # Format y-axis
    plt.ylim(0, 20000000)

    # Make layout clean
    plt.tight_layout()

    # Show graph
    plt.show()

def main():
    N_sizes = [10000, 20000, 30000, 40000, 50000]
    bubble_sort_times = []
    selection_sort_times = []
    insertion_sort_times = []

    for size in N_sizes:
        arr = generate_random_array(size)

        # Measure bubble sort time
        bubble_start_time = bubble_sort(arr.copy())
        bubble_sort_times.append(bubble_start_time * 1e6)  # Convert to microseconds

        # Measure selection sort time
        selection_start_time = selection_sort(arr.copy())
        selection_sort_times.append(selection_start_time * 1e6)  # Convert to microseconds

        # Measure insertion sort time
        insertion_start_time = insertion_sort(arr.copy())
        insertion_sort_times.append(insertion_start_time * 1e6)  # Convert to microseconds

    draw_graph(N_sizes, bubble_sort_times, selection_sort_times, insertion_sort_times)

main()