# def persistence(n):
#   if n < 10:
#     return 0
  
#   total = 1
#   for i in str(n):
#     total *= int(i)
  
#   # Add one as a counter for each iteration
#   # If only call the function, it will return 0 since the last call will always satisfies the base casae
#   return persistence(total) + 1 


# Using iteration
def persistence(n):
  count = 0
  
  while n > 9:
    count += 1

    total = 1
    for i in str(n):
      total *= int(i)
    n = total

  return count
  
  
print(persistence(39))
print(persistence(4))
print(persistence(25))
print(persistence(999))