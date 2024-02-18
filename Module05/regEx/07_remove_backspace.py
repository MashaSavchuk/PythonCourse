##1 забрати екстра пробіли, зробити тільки один пробіл між словами

import re

# multiline string
string = 'abc 12\
de 23 \n  f45   6'

# re.sub(pattern, "", string)
# re.sub(r"", "", string)
res = re.sub(r"\s+", "", string)

print(res)


##2
import re

# multiline string
string = 'abc 12\
de 23 \n f45 6'

# matches all whitespace characters
pattern = '\s+'

# empty string
replace = ''

new_string = re.sub(pattern, replace, string) 
print(new_string)

new_string = re.subn(pattern, replace, string) 
print(new_string)