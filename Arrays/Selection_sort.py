"""
How it works:

0== Go through the array to find the lowest value.
0=== Move the lowest value to the front of the unsorted part of the array.
0== Go through the array again as many times as there are values in the array.
"""


my_array = [64, 34, 25, 5, 2, 1, 9, 12, 12]
length = len(my_array)
for i in range(length-1):
  min_index = i
  for j in range(i+1, length):
    if my_array[j] < my_array[min_index]:
      min_index = j
  min_value = my_array.pop(min_index)
  my_array.insert(i, min_value)
print("Selection sorted array : ", my_array)