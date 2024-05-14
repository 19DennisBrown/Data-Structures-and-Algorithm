arr = [2,4,6,8,12,32,45,66,434,12]
size = len(arr)

for i in range(1, size):
  target_index = i
  current_value = arr[i]
  for j in range(i-1, -1, -1):
    if arr[j]>arr[i]:
      arr[j+1]=arr[j]
      target_index = j
    else:
      break
  arr[target_index]= current_value
print(arr)