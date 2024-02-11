'''
Given an array of integers, find the one that appears an odd number of times.
There will always be only one integer that appears an odd number of times.

Examples:
[7] should return 7, because it occurs 1 time (which is odd).
[0] should return 0, because it occurs 1 time (which is odd).
[1,1,2] should return 2, because it occurs 1 time (which is odd).
[0,1,0,1,0] should return 0, because it occurs 3 times (which is odd).
[1,2,2,3,3,3,4,3,3,3,2,2,1] should return 4, because it appears 1 time (which is odd).
'''

def find_it(seq):
  # Initialize dictionary
  counts = dict()
  
  for num in seq:
    # Use .get to get counts dictionary's values and set it to 0 as the default value
    counts[num] = counts.get(num, 0) + 1
  
  for num in counts:
    if counts[num] % 2 != 0:
      return num

print(find_it([1,2,2,3,3,3,4,3,3,3,2,2,1]))
print(find_it([0,1,0,1,0]))
print(find_it([1,1,2]))
print(find_it([0]))
print(find_it([7]))