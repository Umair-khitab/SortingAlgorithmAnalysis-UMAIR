# -*- coding: utf-8 -*-
"""
Created on Sat Nov  8 19:33:04 2025

@author: khita
"""

import time

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def measure_time(sort_func, arr):
    times = []
    for _ in range(5):
        start = time.time()
        sort_func(arr.copy())
        end = time.time()
        times.append((end - start) * 1000)
    return sum(times) / len(times)

arr1 = list(range(1, 6))
arr2 = list(range(1, 11))
arr3 = list(range(1, 51))
arr4 = list(range(1, 101))

print("Bubble Sort Times:")
print("Size 5:", measure_time(bubble_sort, arr1), "ms")
print("Size 10:", measure_time(bubble_sort, arr2), "ms")
print("Size 50:", measure_time(bubble_sort, arr3), "ms")
print("Size 100:", measure_time(bubble_sort, arr4), "ms")

import matplotlib.pyplot as plt

input_sizes = [5, 10, 50, 100]
bubble_times = [
    measure_time(bubble_sort, arr1),
    measure_time(bubble_sort, arr2),
    measure_time(bubble_sort, arr3),
    measure_time(bubble_sort, arr4)
]

plt.plot(input_sizes, bubble_times, marker='o', label='Bubble Sort')
plt.xlabel('Input Size (N)')
plt.ylabel('Execution Time (ms)')
plt.title('Bubble Sort Performance')
plt.legend()
plt.grid(True)
plt.show()

import time
import matplotlib.pyplot as plt

# Sorting Algorithms
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]
        merge_sort(L)
        merge_sort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

# Timing Function
def measure_time(sort_func, arr):
    times = []
    for _ in range(5):
        start = time.time()
        sort_func(arr.copy())
        end = time.time()
        times.append((end - start) * 1000)
    return sum(times) / len(times)

# Input Arrays
arr1 = list(range(1, 6))
arr2 = list(range(1, 11))
arr3 = list(range(1, 51))
arr4 = list(range(1, 101))
arrays = [arr1, arr2, arr3, arr4]
input_sizes = [len(arr) for arr in arrays]

# Measure Times
bubble_times = [measure_time(bubble_sort, arr) for arr in arrays]
selection_times = [measure_time(selection_sort, arr) for arr in arrays]
insertion_times = [measure_time(insertion_sort, arr) for arr in arrays]
merge_times = [measure_time(merge_sort, arr) for arr in arrays]

# Print Results
print("Input Sizes:", input_sizes)
print("Bubble Sort:", bubble_times)
print("Selection Sort:", selection_times)
print("Insertion Sort:", insertion_times)
print("Merge Sort:", merge_times)

# Plot Graph
plt.plot(input_sizes, bubble_times, marker='o', label='Bubble Sort')
plt.plot(input_sizes, selection_times, marker='s', label='Selection Sort')
plt.plot(input_sizes, insertion_times, marker='^', label='Insertion Sort')
plt.plot(input_sizes, merge_times, marker='x', label='Merge Sort')
plt.xlabel('Input Size (N)')
plt.ylabel('Average Execution Time (ms)')
plt.title('Sorting Algorithm Performance')
plt.legend()
plt.grid(True)
plt.show()
