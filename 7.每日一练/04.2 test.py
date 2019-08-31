import re,string
s = 'a,asda'
for c in string.punctuation:
    s = s.replace(c, "")
print(s)