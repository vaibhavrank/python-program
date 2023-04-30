
l1=[]

for i in range(1,31):
    for j in range(1,31):
        for k in range(1,31):
            if i*i + j*j ==k*k:
                l1.append([i,j,k])



print(l1)