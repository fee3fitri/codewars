'''
Write a function named first_non_repeating_letter that takes a string input, and returns the first character that is not repeated anywhere in the string.

For example, if given the input 'stress', the function should return 't', since the letter t only occurs once in the string, and occurs first in the string.

As an added challenge, upper- and lowercase letters are considered the same character, but the function should return the correct case for the initial letter. For example, the input 'sTreSS' should return 'T'.

If a string contains all repeating characters, it should return an empty string ("") or None -- see sample tests.

'''

# def first_non_repeating_letter(s):
#     count = {}

#     for char in s:
#         count[char.lower()] = count.get(char.lower(), 0) + 1

#     singles = [char for char, val in count.items() if val == 1]

#     if singles:
#       if s.find(singles[0].upper()) > s.find(singles[0]):
#         return singles[0].upper()
#       else:
#         return singles[0]
#     else:
#       return ''
    
def first_non_repeating_letter(s):
  # lower_s = s.lower()
  # for i, char in enumerate(lower_s):
  #   if lower_s.count(char) == 1: return s[i]
  # return ''

  count = dict()
  
  for char in s.lower():
    return char

print(first_non_repeating_letter('sTreSS'))
print(first_non_repeating_letter('Go hang a salami, I\'m a lasagna hog!'))
