
"""
Sorts an array by counting the number of times each value occurs.
-It does not compare values like the rest of algorithms

  ===HOW IT WORKS===
  1. Create a new array for counting how many there are of different values.
  2. Go through the array that needs to be sorted.
  3. For each value, count it by increasing the counting array at the corresponding index.
  4. After counting the values, go through the counting  array to create the sorted array.
  5. For each count in the counting array, create the correct number of elements, with values that correspond to the  counting array index.

???conditions {
 a. Must be integer values.
 b. Must be non-negative numbers.
 c. Must have limited range of values.
}

????IMPLEMENTATION
  1. Array with values to sort.
  2. A 'countingSort' method that recieves an array of integers.
  3. An array inside the method to keep count of the values.
  4. A loop inside the method that counts and removes values, by incrementing elements in the counting array.
  5. A loop inside the method that recreates the array by using the counting  array , so that the elements appear in the right order.
"""

def countingSort(arr):
  max_val = max(arr)
  count = [0]*(max_val + 1)

  while len(arr) > 0:
    num = arr.pop(0)
    count[num] += 1

  for i in range(len(count)):
    while count[i]>0:
      arr.append(i)
      count[i] -= 1
    
  return arr

unsortedArr = [4,2,2,6,3,3,1,6,5]
sortedArr = countingSort(unsortedArr)

print(f"Sorted array: {sortedArr}")
  
