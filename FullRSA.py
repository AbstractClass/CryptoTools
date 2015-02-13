def encrypt():
    i,d,n,e = 0,0,0,0
    prime = []
    
    while True:
        plain=input("Enter message in number form (cannot start with 0): ")
        try:
            plain = int(plain)
            break
        except:
            print("Bad format/message.  Please enter message with no spaces in number form.")
            continue

    while True:
        try:
            p = int(input("Enter 1st prime(p): "))
            if is_prime(p):
                q = int(input("Enter second prime(q): "))
                if is_prime(q):
                    break
                else:
                    print("Not prime.")
                    continue
            else:
                print("Not prime.")
                continue
        except Exception as inst:
            print(inst)
            print("Not a number")
            continue

    n = p*q
    e_values = find_Es(p,q) #NOTE! p,q must already be parsed as int

    print("Here are possible e values: ", ', '.join(str(x) for x in e_values))
    while True:
        try:
            e = int(input("Enter your e value: "))
        except:
            print("e is not a valid number.")
            continue
        if e in e_values:
            break
        else:
            print("Selected e value is not in list of possible e's.")
            continue

    d = find_d(p,q,e) #NOTE! p,q,e must already be parsed as int
        
    cipher = pow(plain, e, n)

    print("Public n: {}\nPublic e: {}\nPrivate d: {}\nCipher Message: {}".format(n, e, d, cipher))
    print("")

def decrypt():
    while True:
        try:
            p = int(input("Enter p value: "))
            q = int(input("Enter q value: "))
            e = int(input("Enter e value: "))
            n = p*q
            cipher = int(input("Enter cipher message (no spaces):"))
            break
        except:
            print("Invalid value.")
            continue

    d = find_d(p,q,e)
    print("Private d: ", d)

    plain = pow(cipher, d, n)
    print("Plaintext message: ", plain)
    
            
def is_prime(p):
    return all(p % i for i in range(2, p))

def find_d(p,q,e):
    import math
    d = 0
    Q = 0
    n = (p-1)*(q-1)
    while(q < 1000):
        d = ((n * Q) + 1) / e
        #print('Q: ', Q)
        if(d == math.floor(d)):
            return int(d)
            break
        Q += 1

def find_Es(p,q):
    from fractions import gcd
    e_values = []
    n = (p-1)*(q-1)
    for i in range(n):
        if gcd(i, n) == 1:
            e_values.append(i)
    return e_values

#CODE START HERE
while True:
    selector=(input("Choose encryption(E) or decryption(D).  Note: decryption requires you to already have p and q: ")).lower()
    if selector == "e":
        encrypt()
    if selector == "d":
        decrypt()
