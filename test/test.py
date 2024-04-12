
this_array = [64, 34, 25, 12, 22, 11, 90, 5]
min_val = this_array[0]

for val in this_array:
  if val < min_val:
    min_val = val
print("Lowest value : ", min_val)

n = len(this_array)

for i in range(n-1):
  swapped = False
  for j in range(n-i-1):
    if this_array[j] > this_array[j+1]:
      this_array[j], this_array[j+1] = this_array[j+1], this_array[j]
      swapped = True
  if not swapped:
    break
print("This is the sorted array : ", this_array)      