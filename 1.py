import re

a1 = ["a", "ab", "abb", "ac", "bcd"]

p = re.compile(r'ab*')

for i in a1:
    if p.fullmatch(i):
        print(f'Found: {i}')
    else:
        print(f'Not found: {i}')
