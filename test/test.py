
# Selection sort

stats = [1,12,32,45,7,4,3,5,7,8,9,3,23,12]

len = len(stats)

for i in range(len-1):
  min_index = i
  for j in range(i+1, len):
    if stats[j] < stats[min_index]:
      min_index = j
  min_value = stats.pop(min_index)
  stats.insert(i, min_value)
print("Selection sorted array : ", stats)