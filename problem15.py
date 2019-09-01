n=20
num=1
den=1
for i in range(2,n+1):
    den*=i
for i in range(2,(2*n)+1):
    num*=i
print((num)/(den*den))
