arr = [2,4,6,8,12,32,45,66,434,12]

input = int(input("Add new index value : "))
arr.append(input)
n = len(arr)
for i in range(n-1):
  index = i
  for j in range(i+1, n):
    if arr[j]<arr[index]:
      index=j
    arr[i],arr[index] = arr[index],arr[i]
print(arr)
