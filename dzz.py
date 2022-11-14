a, b = input(), 0
for i in range(len(a.split())):
    if a.split()[i] != ' ':
        b += a.split()[i + 1:].count(a.split()[i])
print(b)