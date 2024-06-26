'''
Find the missing letter
Write a method that takes an array of consecutive (increasing) letters as input and that returns the missing letter in the array.

You will always get an valid array. And it will be always exactly one letter be missing. The length of the array will always be at least 2.
The array will always contain letters in only one case.

Example:

['a','b','c','d','f'] -> 'e'
['O','Q','R','S'] -> 'P'
'''

def find_missing_letter(chars):
  for i, char in enumerate(chars):
    next_char = chr(ord(char) + 1)
    if next_char != chars[i + 1]:
      return next_char
    
print(find_missing_letter(['a','b','c','d','f']))
print(find_missing_letter(['O','Q','R','S']))