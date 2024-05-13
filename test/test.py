
array = [64, 34, 25, 12, 22, 11, 90, 5]
size = len(array)

for i in range(1,size):
  insert_index = i
  current_val = array[i]
  for j in range(i-1, -1, -1):
    if array[j] > current_val:
      array[j+1] = array[j]
      current_val = j
    else:
      break
  array[insert_index] = current_val
print("Insertion sorted array : ", array)