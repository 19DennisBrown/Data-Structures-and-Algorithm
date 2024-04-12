
"""
>>Algorithm design

Variable 'minVal' = array[0]
For each element in the array
    If current element < minVal
        minVal = current element
"""

this_array = [9,4,6,4,5,6,8,1]
min_val = this_array[0]

for low_val in this_array:
  if low_val < min_val:
    min_val = low_val
print(min_val)