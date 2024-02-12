'''
Build Tower
Build a pyramid-shaped tower, as an array/list of strings, given a positive integer number of floors. A tower block is represented with "*" character.

For example, a tower with 3 floors looks like this:

[
  "  *  ",
  " *** ", 
  "*****"
]
And a tower with 6 floors looks like this:

[
  "     *     ", 
  "    ***    ", 
  "   *****   ", 
  "  *******  ", 
  " ********* ", 
  "***********"
]
'''

def tower_builder(n_floors):
  odd_nums = [n for n in range(n_floors * 2) if n % 2]
  tower = []

  for num in odd_nums:
    tower.append(("*" * num).center(odd_nums[-1]))

  return tower

print(tower_builder(3))
print(tower_builder(5))
print(tower_builder(6))

