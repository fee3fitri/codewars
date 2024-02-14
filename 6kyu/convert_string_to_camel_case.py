'''
Complete the method/function so that it converts dash/underscore delimited words into camel casing. The first word within the output should be capitalized only if the original word was capitalized (known as Upper Camel Case, also often referred to as Pascal case). The next words should be always capitalized.

Examples
"" gets converted to "theStealthWarrior"

"The_Stealth_Warrior" gets converted to "TheStealthWarrior"

"The_Stealth-Warrior" gets converted to "TheStealthWarrior"
'''

import re

def to_camel_case(text):
  words = re.sub('[^a-zA-Z]+', ' ', text).split()
  res = []
  for i in range(len(words)):
    if i == 0:
      res.append(words[i])
    else:
      res.append(words[i].capitalize())
  # return ''.join(words)
  return ''.join(res)

print(to_camel_case("the-stealth-warrior"))
print(to_camel_case("The_Stealth_Warrior"))
print(to_camel_case("The_Stealth-Warrior"))
print(to_camel_case("the_stealth_warrior"))