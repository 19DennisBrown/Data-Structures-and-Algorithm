

def countSort(arr):
  max_val = max(arr)
  count = [0]*(max_val+1)

  while len(arr):
    num = arr.pop(0)
    count[num]+=1
  for i in range(len(count)):
    while count[i]>0:
      arr.append(i)
      count[i]-=1
  return arr

unsortedArr = [4,2,21,6,30,3,1,66,5]
sortedArr = countSort(unsortedArr)

print(f"This is the new array : {sortedArr}")