
import re

a = "Write a Python program  adfdsfb to replace all occurrences of space, comma, or dot with a colon."

p = re.compile(r'a\wb')
m = p.findall(a)

print(m)