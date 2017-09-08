c = input()
c = list(c)
slovaboli = ["TALB", "TPE1", "COMM", "TCOM", "TIT13", "(ASCAP)"]
gi = [len(slovaboli) for slovaboli in slovaboli]
pez, cif, slov, mu = [], [], [], []
dlinna_c = len(c)#-1

j = 0p = list(p)

while j < dlinna_c:
    n = 0
    p = []
    i = j
    a = min(gi)
    b = max(gi)
    while n < b:
        while n < a:
            p.append(c[i])
            n += 1
            if i < dlinna_c - 1:
                i += 1
            else:
                break
        p = "".join(p)
        print())
        if p in slovaboli:
            pez.append(p)
            cif.append(i)
            j += 1
            n = b
        else:
            p = list(p)
            a += (2**(a - 4))
            j += 1

for i in range(len(cif) - 1):
    um = cif[i]
    #if len(pez[i]) < 
    num = cif[i + 1] - len(pez[i]) - 1
    while um <= num:
        mu.append(c[um])
        um += 1
        print(c[um])
    mu = "".join(mu)
    slov.append(mu)
    mu = []

#for i in range(len(cif) - 1):
#   print(pez[i], ": ", slov[i])
