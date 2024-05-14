arry = [2,4,6,8,12,32,45,66,434,12]
arry.append(int(input("Enter value : ")))
len = len(arry)
for i in range(len-1):
  swapped = False
  for j in range(len-i-1):
    if arry[j]>arry[j+1]:
      arry[j],arry[j+1]=arry[j+1],arry[j]
      swapped = True
  if not swapped:
    break
print(arry)