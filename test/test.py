
# Selection sort

stats = [1,12,32,45,7,4,3,5,7,8,9,3,23,12]

n = len(stats)
for i in range(n-1):
  min_index = i
  for j in range(i+1, n):
    if stats[j] < stats[min_index]:
      min_index = j
  stats[i], stats[min_index] = stats[min_index], stats[i]
print("Selection sorted array : ", stats)