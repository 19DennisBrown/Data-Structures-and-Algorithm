

def binarySearch(arr, targetVal):
  left = 0
  right = len(arr)-1

  while left <= right:
    mid = (left + right)//2

    if arr[mid]==targetVal:
      return mid
    if arr[mid]< targetVal:
      left = mid + 1
    else:
      right = mid -1
  return -1

myArray = [0,3,5,5,7,8,11,13,15,23,45,56]
myTarget= 15

result = binarySearch(myArray, myTarget)

if result != -1:
  print(f"Found")
else:
  print(f"Not found")