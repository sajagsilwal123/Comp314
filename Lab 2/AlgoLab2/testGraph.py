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