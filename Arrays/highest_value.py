

this_array = [64, 34, 25, 12, 22, 1, 0, 5]

max_value = this_array[0]
for val in this_array:
  if val > max_value:
    max_value = val
print("Maximum value in the array is : ", max_value)