import re

text = 'news/2021/12/31'
# non-capturing groups, groups()
# pattern = "\w+/\d{4}/\d{2}/\d{2}"
# res = re.findall(pattern, text)
# print(res)


pattern = '(?P<resource>\w+)/(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})'

matches = re.finditer(pattern, text)
# print(matches)
for match in matches:
    print(match.groupdict())