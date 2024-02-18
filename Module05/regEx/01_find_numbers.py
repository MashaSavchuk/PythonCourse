##1 знайти всі цифри у тексті []

import re

sample_text = "Alice lives in 1230s First St., Ocean city, MD 124367"

res = re.search(r"\d+", sample_text)
#res = re.search(r"[\d]+", sample_text)
#res = re.search(r"[0-9]+", sample_text)
# + щоб знаходити всі цифри, а не тільки першу
print(res.group())

#res = re.findall(r"\d+", sample_text)
res = re.findall(r"[\ds]+", sample_text)
print(res)


# https://www.w3schools.com/python/python_regex.asp

## 2
import re

# Sample text
sample_text = 'Alice lives in 1230 First St., Ocean City, MD 156789.'

# Create a regular expression object with the regular expression '\d'
regex = re.compile(r'\d+')

# Search the sample_text for the regular expression
matches = re.findall(regex, sample_text)

# Print all the matches
for match in matches:
    print(match)