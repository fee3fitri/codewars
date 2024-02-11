'''
You probably know the "like" system from Facebook and other pages. People can "like" blog posts, 
pictures or other items. We want to create the text that should be displayed next to such an item.

Implement the function which takes an array containing the names of people that like an item. 
It must return the display text as shown in the examples:

[]                                -->  "no one likes this"
["Peter"]                         -->  "Peter likes this"
["Jacob", "Alex"]                 -->  "Jacob and Alex like this"
["Max", "John", "Mark"]           -->  "Max, John and Mark like this"
["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this"

Note: For 4 or more names, the number in "and 2 others" simply increases.
'''

def likes(names):
  length = len(names)
  like = ''
  like = 'likes' if length <= 1 else 'like'
  
  names_str = ''
  if length == 0: names_str = 'no one'
  elif length == 1: names_str = str(names[0])
  elif length == 2: names_str = f"{str(names[0])} and {str(names[1])}"
  elif length == 3: names_str = f"{str(names[0])}, {str(names[1]) } and {str(names[2])}"
  else: names_str = f"{str(names[0])}, {str(names[1]) } and {str(length - 2)} others"

  return names_str + ' ' + like + ' this'

print(likes([]))
print(likes(["Peter"]))
print(likes(["Jacob", "Alex"]))
print(likes(["Jacob", "Alex", "Mark"]))
print(likes(["Jacob", "Alex", "Mark", "Max"]))
