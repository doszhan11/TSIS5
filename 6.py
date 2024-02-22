
import re

a = "djhknsd  kjndsfn io jknsdofii noisdf noinsdf oinionsdf oinjknds kjnjk."

p = re.compile(r'[ ,.]')
r = p.sub(':', a)

print("Original:", a)
print("After:", r)