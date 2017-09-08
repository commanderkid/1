slovaboli = ["TALB", "TPE1", "COMM", "TCOM", "TIT13", "(ASCAP)"]
c = list("vhTALBThe Platinum Series ITPE1COMMengOrchestral Epic ActionTCOMPaul Dinletir(ASCAP)TIT13Naomiville Music (ASCAP)")
gi = [len(slovaboli) for slovaboli in slovaboli]
dlinna_c = len(c) - 1
gi = sorted(set(gi))
j, ii, n, i = 0, 0, 0, 0
pez, cif = [], []
for j in range(dlinna_c):
    p = []
    n = 0
    i = j
    ii = 0
    while n < gi[(len(gi) - 1)]:
        while n < gi[ii]:
            p.append(c[i])
            n += 1
            if i < dlinna_c:
                i += 1
            else:
                n = max(gi)
        p = "".join(p)  
        if p in slovaboli:
            pez.append(p)
            cif.append(i - 1)

            j += 1
            p = list(p)
            if ii < (len(gi) - 1):
                ii += 1
            else:
                n = max(gi)
        else:
            p = list(p)
            j += 1
            if ii < (len(gi) - 1):
                ii += 1
            else:
                n = max(gi)


i, j = 0, 0
om, ur = [], []
while j < (len(cif)):
    ur = []
    u = cif[j] - len(pez[j]) + 1
    while i < u:
        ur.append(c[i])
        i += 1
    ur = "".join(ur)
    om.append(ur)
    i = cif[j] + 1
    j += 1       



print(om[0])
om.pop(0)
print("------------")
guum = list(pez[len(pez) - 1])
if (len(c) - 1) == (max(cif) + 1):
    om.append("")
else:
    z = (c[(max(cif) + 1) : len(c)])
    z = "".join(z)
    om.append(z)
for i in range(len(om)):
    print(pez[i], ": ", om[i])
print("------------")

                


        
