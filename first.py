c = input()
c = list(c)
slovaboli = ["TALB", "TPE1", "COMM", "TCOM"]

pez = []
dlinna_c = len(c)-1
j, i = 0, 0
   
while j < dlinna_c:
    n = 0
    p = []
    i = j
    while n < 4:
        p.append(c[i])
        n += 1
        if i < dlinna_c:
            i += 1
        else:
            break
    p = "".join(p)
    if p in slovaboli:
        pez.append(p)
        pez.append(i)
        j += 1
    else:
        j += 1
