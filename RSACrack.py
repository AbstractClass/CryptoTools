import math
import decimal

n = input("Enter (p-1)(q-1): ")
q = 0
e = input("Enter e: ")
d = 0

while(q < 1000):
    d = ((n * q) + 1) / e
    print('q: ', q)
    if(d == math.floor(d)):
        print('d: ', int(d))
        break
    q += 1
input("Press any key to continue...")
