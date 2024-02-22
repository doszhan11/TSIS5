import re

a = "NsjfjnkIJINlkf kjs"

p = re.sub(r'([a-z])([A-Z])', r'\1 \2', a)


print("Input:", a)
print("Output:", p)
