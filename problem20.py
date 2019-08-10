def spl(a):
    return list(a)
t=1
for i in range(1,101):
    t*=i
b=spl(str(t))
sum=0
print(len(b))
for j in range(len(b)):
    sum+=int(b[j])
print(sum)