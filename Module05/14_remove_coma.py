# забрати зайві коми

import re
text = "sdffgg,ggghhh,,ffgtrr,,,,,fg ,,yuuuu,,,,,"

# через регулярний вираз
# res = re.sub("r,+", ",", text).rstrip(",")
# print(res)

# через цикл
while ",," in text:
    text = text.replace(",,", ",")

print(text.rstrip(","))