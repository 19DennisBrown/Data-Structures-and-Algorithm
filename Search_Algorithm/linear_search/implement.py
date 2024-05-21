

def linearSearch(arr, targetVal):
  for i in range(len(arr)):
    if arr[i] == targetVal:
      global position
      position = arr[i]
      return i, position
  return -1
arr = [3,7,2,9,5]
targetVal = 9

result = linearSearch(arr, targetVal)

if result != -1:
  print(f"Value, {targetVal}, found at {position}.")
else:
  print(f"Value, {targetVal}, not found.")
