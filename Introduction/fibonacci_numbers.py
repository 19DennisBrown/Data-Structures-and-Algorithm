# The Fibonacci numbers are very useful for introducing algorithms, so before we continue, here is a short introduction to Fibonacci numbers.
# The two first Fibonacci numbers are 0 and 1, and the next Fibonacci number is always the sum of the two previous numbers, so we get 0, 1, 1, 2, 3, 5, 8, 13, 21, ...


# FIBONACCI USING FOR LOOP

# first = 0
# second = 1

# print(first)
# print(second)

# for i in range(6):
#   next = first + second
#   print(next)
#   first = second
#   second = next


# FIBONACCI USING FOR RECURSION
  
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
    
# FINDING THE nth FIBONACCI NUMBER USING FOR RECURSION
def F(n):
    if n <= 1:
        return n
    else:
        return F(n - 1) + F(n - 2)

print(F(19))