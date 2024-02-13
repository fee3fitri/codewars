def persistence(n):
  if n < 10:
    return 0
  
  total = 1
  for i in str(n):
    total *= int(i)
  
  # Add one as a counter for each iteration
  # If only call the function, it will return 0 since the last call will always satisfies the base casae
  return persistence(total) + 1 
  
  
print(persistence(39))
print(persistence(4))
print(persistence(25))
print(persistence(999))