a = 'doppleganger'
d = dict()
for b in a:
    if b not in d:
        d[b] = 1
    else:
        d[b] = d[b] + 1
c = 0
for b in a:
    if d[b] >= c:
        c = d[b]
print(c)

if b == c:
    print()



