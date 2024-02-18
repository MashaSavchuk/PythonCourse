# https://www.w3schools.com/python/python_regex.asp

##1 знайти всі двоцифрові цифри у тексті {}

import re

sample_text = "I bought 77 nuts for 6$ and 110 bolts for 3$."

#res = re.findall(r"\d{2}", sample_text)
#res = re.findall(r"\d{1,2}", sample_text) # буде шукати одно- або двоцифрові цифри
res = re.findall(r"\b[\d]{2}\b", sample_text) # буде шукати двоцифрові цифри
#\b - це як пробіл
print(res)


##2
import re

s = "I bought 77 nuts for 6$ and 110 bolts for 3$."
print(re.findall("\d{3}", s))  # ['0']
print(re.findall("[\d]{3}", s))  # ['110']