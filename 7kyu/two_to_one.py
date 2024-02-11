'''
Take 2 strings s1 and s2 including only letters from a to z. Return a new sorted string, 
the longest possible, containing distinct letters - each taken only once - coming from s1 or s2.

Examples:
a = "xyaabbbccccdefww"
b = "xxxxyyyyabklmopq"
longest(a, b) -> "abcdefklmopqwxy"

a = "abcdefghijklmnopqrstuvwxyz"
longest(a, a) -> "abcdefghijklmnopqrstuvwxyz"
'''

def longest(a1, a2):
  set1 = set(list(a1))
  set2 = set(list(a2))
  combined = set(sorted(set1) + sorted(set2))
  return ''.join(sorted(combined))

def longest(a1, a2):
  return ''.join(sorted(set(a1 + a2)))

print(longest("xyaabbbccccdefww", "xxxxyyyyabklmopq"))