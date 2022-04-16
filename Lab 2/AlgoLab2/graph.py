import time
import random

from matplotlib import pyplot as plt

from MergeSort import MergeSort
from InsertionSort import InsertionSort

def generate_random_list(size):
    return [random.choice(range(size)) for i in range(size)]


def calculate_time(func):
    """Decorator function for calculating time"""

    def inner(*args, **kwargs):

        tic = time.time_ns()
        func(*args, **kwargs)
        toc = time.time_ns()

        return toc - tic

    return inner


@calculate_time
def check_time_insertion_sort(arr):
    return InsertionSort(arr)


@calculate_time
def check_time_merge_sort(arr):
    r = len(arr)
    return MergeSort(arr,0,r)


if __name__ == "__main__":
    samples = [generate_random_list(i) for i in range(0, 1000, 10)]

    sample_sizes = []
    insertion_sort_times = []
    merge_sort_times = []

    for sample in samples:
        sample_sizes.append(len(sample))
        insertion_sort_times.append(check_time_insertion_sort(sample))
        merge_sort_times.append(check_time_merge_sort(sample))

    # Plotting
    plt.figure(figsize=(10, 6))
    plt.xlabel("Sample Size (n)")
    plt.ylabel("Time Elasped (ns)")


    plt.title("Time Complexity: Insertion sort vs Merge Sort")
    plt.plot(sample_sizes, insertion_sort_times, ",-", label="Insertion Sort")
    plt.plot(sample_sizes, merge_sort_times, ",-", label="Merge Sort")

    plt.legend()
    plt.show()
    print("done")












# from InsertionSort import InsertionSort
# from MergeSort import MergeSort
# import random
# import time
# from matplotlib import pyplot as plt

# def SampleGenerator(size):
#     return [random.choice(range(size)) for i in range(size)]

# def TimeCalc(func):

#     def calculate(*args):
#         tic = time.time_ns()
#         func(*args)
#         toc = time.time_ns()
#         net = toc-tic

#         return net
#     return calculate

# @TimeCalc
# def checkTimeInsertionSort(arr):
#     return InsertionSort(arr)

# # @TimeCalc
# # def checkTimeMergeSort(arr):
# #     r= len(arr)
# #     return MergeSort(arr,0,r)



# samples = [SampleGenerator(i) for i in range(0,10000,10)]

# sampleSize=[]
# insertionSortTime = []
# mergeSortTime = []

# for sample in samples:
#     sampleSize.append(len(sample))
#     insertionSortTime.append(checkTimeInsertionSort(sample))
#     # mergeSortTime.append(checkTimeMergeSort(sample))

# plt.figure(figsize=(10,6))
# plt.xlabel("Sample Size (n)")
# plt.ylabel("Time Elapsed (ns)")

# plt.title("Time Complexity: Insertion Sort")
# plt.plot(sampleSize, insertionSortTime, ",-", label ="Insertion Sort")
# # plt.plot(sampleSize, mergeSortTime, ",-", label="Merge Sort")


# plt.legend()
# plt.show()