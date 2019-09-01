def fibo():
    a = 0
    b = 1
    while True:
        yield b
        a,b = b,a+b

f = enumerate(fibo())
x = 0
while len(str(x)) < 1000:
    i,x = next(f)

print(i+1)


