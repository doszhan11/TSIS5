import re

a = ["abc", "abb", "aabb", "ac", "bb", "aabc"]


p = re.compile(r'a(bb){2,3}')

for i in a:
    if p.search(p):
        print(f'Found: {i}')
    else:
        print(f'Not found: {i}')
