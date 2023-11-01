t = int(input())

for _ in range(t):
    n = int(input())
    set1 = set()
    for a in range(0,4):
        for b in range(0,4):
            for c in range(0,4):
                for d in range(0,4):
                    for e in range(0,4):
                        for f in range(0,4):
                            for g in range(0,4):
                                for h in range(0,4):
                                    for i in range(0,4):
                                        for j in range(0,4):
                                            if a + b + c + d + e + f + g + h + i + j== n:
                                                temp = [a,b,c,d,e,f,g,h,i,j]
                                                temp2 = []
                                                for t in temp:
                                                    if t != 0:
                                                        temp2.append(t)
                                                set1.add(tuple(temp2))
    print(len(set1))