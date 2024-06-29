import random
from matplotlib import pyplot as plt, animation
import time

def swap(a, i, j):
    a[i], a[j] = a[j], a[i]

def bubble_sort(a):
    n = len(a)
    for i in range(n-1):
        swapped = False
        for j in range(n-1-i):
            if a[j] > a[j+1]:
                swap(a, j, j+1)
                swapped = True
                yield a, j, j+1
        if not swapped:
            break

def insertion_sort(a):
    n = len(a)
    for i in range(1, n):
        key = a[i]
        j = i - 1
        while j >= 0 and key < a[j]:
            a[j+1] = a[j]
            j -= 1
            yield a, j, i
        a[j+1] = key
        yield a, j, i

def selection_sort(a):
    n = len(a)
    for i in range(n-1):
        min_index = i
        for j in range(i+1, n):
            if a[j] < a[min_index]:
                min_index = j
        if min_index != i:
            swap(a, i, min_index)
            yield a, i, min_index

def merge_sort(a):
    def merge(a, left, mid, right):
        merged = []
        i = left
        j = mid + 1
        while i <= mid and j <= right:
            if a[i] < a[j]:
                merged.append(a[i])
                i += 1
            else:
                merged.append(a[j])
                j += 1
        while i <= mid:
            merged.append(a[i])
            i += 1
        while j <= right:
            merged.append(a[j])
            j += 1
        for i, val in enumerate(merged):
            a[left + i] = val
            yield a, left + i, -1 

    def merge_sort_helper(a, left, right):
        if left < right:
            mid = (left + right) // 2
            yield from merge_sort_helper(a, left, mid)
            yield from merge_sort_helper(a, mid + 1, right)
            yield from merge(a, left, mid, right)

    n = len(a)
    yield from merge_sort_helper(a, 0, n-1)

def quick_sort(a):
    def partition(a, low, high):
        pivot = a[high]
        i = low - 1
        for j in range(low, high):
            if a[j] < pivot:
                i += 1
                swap(a, i, j)
                yield a, i, j
        swap(a, i+1, high)
        yield a, i+1, high
        return i + 1

    def quick_sort_helper(a, low, high):
        if low < high:
            pi = yield from partition(a, low, high)
            yield from quick_sort_helper(a, low, pi-1)
            yield from quick_sort_helper(a, pi+1, high)

    n = len(a)
    yield from quick_sort_helper(a, 0, n-1)

def heap_sort(a):
    def heapify(a, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        if left < n and a[i] < a[left]:
            largest = left
        if right < n and a[largest] < a[right]:
            largest = right
        if largest != i:
            swap(a, i, largest)
            yield a, i, largest
            yield from heapify(a, n, largest)

    n = len(a)
    for i in range(n // 2 - 1, -1, -1):
        yield from heapify(a, n, i)
    for i in range(n-1, 0, -1):
        swap(a, 0, i)
        yield a, 0, i
        yield from heapify(a, i, 0)

def shell_sort(a):
    n = len(a)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = a[i]
            j = i
            while j >= gap and a[j-gap] > temp:
                a[j] = a[j-gap]
                j -= gap
                yield a, j, i
            a[j] = temp
            yield a, j, i
        gap //= 2

def visualize():
    try:
        N = int(input("Enter the number of elements: "))
    except ValueError:
        print("Please enter a valid number.")
        return

    a = list(range(1, N + 1))
    random.shuffle(a)
    
    # Dictionary of sorting algorithms
    sort_algorithms = {
        'Bubble Sort': bubble_sort,
        'Insertion Sort': insertion_sort,
        'Selection Sort': selection_sort,
        'Merge Sort': merge_sort,
        'Quick Sort': quick_sort,
        'Heap Sort': heap_sort,
        'Shell Sort': shell_sort
    }
    
    print("Choose a sorting algorithm:")
    for i, name in enumerate(sort_algorithms.keys()):
        print(f"{i + 1}. {name}")
    
    try:
        choice = int(input("Enter the number of your choice: ")) - 1
        algorithm_name = list(sort_algorithms.keys())[choice]
    except (ValueError, IndexError):
        print("Invalid choice.")
        return
    
    sort_algorithm = sort_algorithms[algorithm_name]
    generator = sort_algorithm(a)
    
    
    fig, ax = plt.subplots()
    ax.set_title(f"{algorithm_name} Visualization")
    bar_sub = ax.bar(range(len(a)), a, align="edge", color="skyblue")
    ax.set_xlim(0, N)
    ax.set_ylim(0, N + 1)
    text = ax.text(0.02, 0.95, "", transform=ax.transAxes)
    iteration = [0]

    def update(data):
        a, i, j = data
        for rect, val in zip(bar_sub, a):
            rect.set_height(val)
            rect.set_color("skyblue")

        if i != -1:
            bar_sub[i].set_color("orange")
        if j != -1:
            bar_sub[j].set_color("orange")
        
        iteration[0] += 1
        text.set_text(f"Time to execute: {iteration[0]}")

    anim = animation.FuncAnimation(
        fig,
        func=update,
        frames=generator,
        repeat=False,
        blit=False,
        interval=50,
        save_count=N * (N - 1) // 2
    )
    plt.show()

if __name__ == "__main__":
    visualize()
