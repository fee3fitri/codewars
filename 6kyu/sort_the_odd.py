'''
Task:
You will be given an array of numbers. You have to sort the odd numbers in ascending order while leaving 
the even numbers at their original positions.

Examples:
[7, 1]  =>  [1, 7]
[5, 8, 6, 3, 4]  =>  [3, 8, 6, 5, 4]
[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]  =>  [1, 8, 3, 6, 5, 4, 7, 2, 9, 0]
'''

def sort_array(source_array):
  # Extract the odd number
  odds = [n for n in source_array if n % 2]

  # Sort the odd number in descending order
  odds.sort(reverse=True)

  # Iterate through source array. If element is odd, replace it from odd list
  res = []
  for n in source_array:
    if n % 2: res.append(odds.pop())
    else: res.append(n)

  return res


print(sort_array([7, 1]))
print(sort_array([5, 8, 6, 3, 4]))
print(sort_array([9, 8, 7, 6, 5, 4, 3, 2, 1, 0]))
