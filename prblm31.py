end = 200
tot=0

for a in range(end+1,0,-200):
    for b in range(a,0,-100):
        for c in range(b,0,-50):
            for d in range(c,0,-20):
                for e in range(d,0,-10):
                    for f in range(e,0,-5):
                        for g in range(f,0,-2):
                            tot+=1
print(tot)
