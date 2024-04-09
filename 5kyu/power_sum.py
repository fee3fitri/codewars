'''
Power Sum
Let’s define a peculiar type of array in which each element is either an integer or another peculiar array. 
Assume that a peculiar array is never empty. 
Write a function that will take a peculiar array as its input and find the sum of its elements. 
If an array is an element in the peculiar array you have to convert it to it’s equivalent value so that 
you can sum it with the other elements. 
Equivalent value of an array is the sum of its elements raised to the number which represents how far nested it is. 

EXAMPLE
[2,3[4,1,2]] = 2+3+ (4+1+2)^2
[1,2,[7,[3,4],2]] = 1 + 2 +( 7+(3+4)^3+2)^2
'''

def power_sum(array,power=1):
  sum = 0
  
  for el in array:
    if type(el) == int:
      sum += el
    else:
      sum += power_sum(el, power + 1)
  
  return sum ** power

print(power_sum([2,3,[4,1,2]],power=1))
print(power_sum([1,2,[7,[3,4],2]],power=1))