
array = [64, 34, 25, 12, 22, 112, 90, 5]

n = len(array)

for i in range(1, n):
  insert_index = i
  insert_value = array[i]

  for j in range(i-1, -1, -1):
    if array[j] > insert_value:
      array[j + 1] = array[j]
      insert_index = j
    else:
      break
  array[insert_index] = insert_value
print("Sorted array : ", array)