import re

text = "Ima.Fool@iana.org Ima.Fool@iana.o Fool1@iana.org first_last@iana.org first.middle.last@iana.or a@test.com " \
       "abc111@test.com.net 12Fool1@iana.org"

# # uppercase letter
# pattern = r"\b[A-Z]{1}[\w\.]+@[a-zA-Z]+\.[a-z]{2,}"
# res = re.findall(pattern, text)

# print(res)

# https://regex101.com/

# знайти все що є до @
pattern = r"\b([A-Z]{1}[\w\.]+)@[a-zA-Z]+\.[a-z]{2,}" 
# pattern = r"\b[A-Z]{1}[\w\.]+@[a-zA-Z]+(\.[a-z]{2,})" 
# те що в () називається група, це можливість сказати інтерпритаторк 
# яку частину виразу записати в результат, але будуть шукатися співпадіння по повному патерну
res = re.findall(pattern, text)
print(res)

# знайти email
result = re.findall(
    r'\b[a-zA-Z]{1}[\w\.]+@[a-zA-Z]+\.[a-zA-Z]{2,}', text)
print(result)

# знайти домен
result = re.findall(r'\b[a-zA-Z]{1}[\w\.]+@([a-zA-Z]+\.[a-zA-Z]{2,})', text)
print(result)
