n = int(input())
sour, bitter = [], []
for i in range(n):
    s, b = [int(x) for x in input().split()]
    sour.append(s)
    bitter.append(b)   

diff = 1000000000

for i in range(1, 2**n):
    s, b, m = 1, 0, 1
    for j in range(n):
        if i & m:
            b += bitter[j]
            s *= sour[j]
        m <<= 1 
    if diff > abs(s-b):
        diff = abs(s-b)

print(diff)
