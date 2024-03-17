

print(0)
print(1)
count = 2

def fibonacci(first, second):
  global count
  if count <= 10:
    next = first + second
    print(next)
    first = second
    second = next
    count += 1
    fibonacci(first, second)
  else:
    return
fibonacci(0, 1)