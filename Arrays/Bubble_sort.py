"""
>>>BUBBLE SORT

>How it works:
Go through the array, one value at a time.
For each value, compare the value with the next value.
If the value is higher than the next one, swap the values so that the highest value comes last.
Go through the array as many times as there are values in the array.

>>To implement the Bubble Sort algorithm in a programming language, we need:

*An array with values to sort.
*An inner loop that goes through the array and swaps values if the first value is higher than the next value. This loop must loop through one less value each time it runs.
*An outer loop that controls how many times the inner loop must run. For an array with n values, this outer loop must run n-1 times.
"""

this_array = [64, 34, 25, 12, 22, 11, 90, 5]
n = len(this_array)

for i in range(n-1):
  swapped =  False
  for j in range(n-i-1):
    if this_array[j] > this_array[j+1]:
      this_array[j], this_array[j+1] = this_array[j+1], this_array[j]
      swapped = True
  if not swapped:
    break
print(this_array)
