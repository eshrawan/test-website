import math
n = int(input("Enter the max number"))
print(n)
primeslist = []
for i in range (0, n+1, 1):
    primeslist.append(i)
print(primeslist)
limit = int(math.sqrt(n+1))
print(limit)
for prime in range (2,limit+1):
    for multiple in range(prime*2, n+1, prime):
        primeslist[multiple] = 0
print(primeslist)
while 0 in primeslist:
    primeslist.remove(0)
print (primeslist)
