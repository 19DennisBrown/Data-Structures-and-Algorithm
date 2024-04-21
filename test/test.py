
first = 0
second = 1

print(first)
print(second)

for i in range(20):
  next = first + second
  print(next)
  first = second
  second = next

print(0)
print(1)
count = 2

def Fibonacci(first, second):
  global count

  if count <= 20:
    next = first + second
    print(next)
    first = second
    second = next
    count += 1
    Fibonacci(first, second)
  else:
    return
print(Fibonacci(0,1))

def Fibo(n):
  if n <= 1:
    return n
  else:
    return Fibo(n-1)+Fibo(n-2)
  
print("20th Fibonacci number is : ", Fibo(20))