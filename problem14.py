import time
start = time.time()

def collatzSeq (n):
    chainNumber = 1
    n1 = n
    while n1 != 1:
        if n1 % 2 == 0:
            n1 = n1/2
            chainNumber += 1
        else:
            n1 = (3*n1) + 1
            chainNumber += 1
    return [chainNumber,n]

fullList = []
for i in range(2, 1000000):
    fullList.append(collatzSeq(i))
sortedList = sorted(fullList, reverse=True)
print(sortedList[:1])

print('Time:', 1000*(time.time() - start))