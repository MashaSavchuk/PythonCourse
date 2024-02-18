# знайти ІР адресу

import re

alert = "Bot activity detected: 192.16.4.162, 69.168.21.343 looks suspicios"

# Create a regular expression object with the regular expression '\d'
# r = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
regex = re.compile(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}")

# Search the alert for the regular expression
matches = re.findall(regex, alert)
# print(matches)

# Print all the matches
for match in matches:
    print(match)