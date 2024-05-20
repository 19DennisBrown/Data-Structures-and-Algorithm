

def countingSort(array):
  max_val = max(array)
  count = [0]*(max_val+1)
  
  while len(array)>0:
    num = array.pop(0)
    count[num] += 1
  for i in range(len(count)):
    while count[i]>0:
      array.append(i)
      count[i]-=1
  return array

givenArray = [1,4,5,43,4,6,6,77,88,23]
sortedArray = countingSort(givenArray)

print(f"Counting sort resulted in the provided array : {sortedArray}")