# знайти повноцінне слово

import re

# pattern = r"be"
# pattern = re.compile(r"\bbe\b")  # знайти повноцінне слово be
pattern = re.compile(r"\bbe")  # знайти всі слова що почінаються на be

res = re.findall(pattern, "to be or not beware")
print(res)