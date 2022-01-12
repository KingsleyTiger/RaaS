import random
import math

def gcd(a,b):
    while b != 0:
        a,b = b,a%b
    return a
    
def prime_num(num):
    pm_num = num
    for i in range(2,int(math.sqrt(pm_num)) + 1):
        if pm_num % i == 0:
           return prime_num(pm_num+1)
    return pm_num 
        
def get_public_key_e(euler):
    e = 2
    while e<euler and gcd(e,euler) != 1:
        e += 1
    return e

def get_private_key_d(e,euler):
    d = 1
    while (e*d) % euler != 1 or d == e:
        d = d+1
    return d

def encrypt(pk,m):
    n,e = pk
    #C = M^e mod n
    C = [(ord(char) ** e) % n for char in m]
    return C

def main():
    m = input("enter plaintext : ")

    pp = prime_num(random.randrange(1,20))
    pq = prime_num(random.randrange(1,20))

    print("(p , q) = ("+str(pp)+","+str(pq)+")")
    
    #get public_key
    n = pp*pq
    print("n = ",str(n))
    
    euler = ((pp-1)*(pq-1))
    print("Φ(n) = ",str(euler))
    
    e = get_public_key_e(euler)
    print("e = ",str(e))
    
    print("public_key(n,e) = ("+str(n)+","+str(e)+")")
    
    
    #get private_key
    print("pok")
    d = get_private_key_d(e,euler)
    print("ok")
    print("private_key(n,d) = (" + str(n) + "," + str(d) + ")")
    
    #encrypt
    encrypted_M = encrypt((n,e),m)
    print("encrypted_M : "+ ''.join(map(lambda x:str(x),encrypted_M)))
    
if __name__ == "__main__":
    main()
