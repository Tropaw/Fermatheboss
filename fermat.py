from math import *
import argparse

parser = argparse.ArgumentParser(description='A simple argparse example.')
parser.add_argument('N', help='N number')
args = parser.parse_args()

def egcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, y, x = egcd(b % a, a)
        return g, x - (b // a) * y, y

def modinv(a, m):
    g, x, _ = egcd(a, m)
    if g != 1:
        raise Exception('Pas d\'inverse modulaire')
    else:
        return x % m


def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False
    
    limit = isqrt(n)
    for i in range(3, limit + 1, 2):
        if n % i == 0:
            return False
    return True

n = int(args.N)
a = isqrt(n) +1

while True:
    b2 = a**2 - n
    if sqrt(b2):
        b = sqrt(b2)
        break
    a +=1
    
p = int(a + b )
q = int(a - b)

print("p * q = "+ str(q*p)) ## public key
if p*q == n and is_prime(int(q)) == True and is_prime(int(p)) == True:
    print(f"Succes for the public key\n p : {p} \n q : {q}")

phin =(p-1) *(q-1)
e = 65537
d = modinv(e, phin)
print("Private : ", d)