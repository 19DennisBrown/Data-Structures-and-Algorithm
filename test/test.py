arr = [2,4,6,8,12,32,45,66,434,12]
size = len(arr)

for i in range(size-1):
  min_index = i
  for j in range(i+1, size):
    if arr[j]<arr[min_index]:
      min_index=j
    arr[i],arr[min_index]=arr[min_index],arr[i]
print(arr)