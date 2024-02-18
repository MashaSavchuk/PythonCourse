# https://www.codewars.com/kata/59c5f4e9d751df43cf000035/python

##1 знайти найдовшу послідовність голосних у тексті

# import re

pattern = r"[aeiou]+"
#pattern = re.compile(r"[aeiou]+")

res = re.findall(pattern, "sdaeruionbvftroihytifgh")
print(res)

##2
def solve(s):
    st="aeiou"
    
    for i in s:
        if not i in st:
            s=s.replace(i,".")

    return max([len(i) for i in s.split(".")])

def solve(s):
    current = 0
    longest = 0
    vowels = ("a", "e", "i", "o", "u")
    for x in s:
        if x in vowels:
            current += 1
            if current > longest:
                longest = current
        else:
            current = 0
    return longest

import re
def solve(s):
  return len(max(re.findall(r"[aeiou]+", s), key=len, default=""))