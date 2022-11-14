a = [1, 2, 2, 3, 4, 5, 3]
for i in range(len(a)):
    for n in range(len(a)):
        if i != n and a[i] == a[n]:
            break
    else:
        print(a[i], end=' ')