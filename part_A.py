import socket
from decimal import *
from Crypto.Util.number import *
import math
import time

getcontext().prec = 700

def find_cube_root(x):
    l = 1
    r = int(Decimal(x).sqrt())
    ret = -1
    # print(f"Rentang pencarian: [{l}, {r}]")
    iter = 0
    while (l<=r):
        iter +=1
        mid = (l+r)//2
        if(mid**3 <= x):
            ret = mid
            l = mid+1
        else:
            r = mid-1
    # print(f"plain yang ditemukan: {ret}")
    # print(f"Banyak iterasi dalam binary search: {iter}")
    return ret

def solve(paket_soal, n, e, c):
    if(paket_soal=='A'):
        k = math.ceil(Decimal(n).sqrt())
        # print(f"[k awal: {k}]")
        while True:
            diff2 = (k*k - n)
            diff = math.ceil(Decimal(diff2).sqrt())
            if(diff*diff == diff2):
                # print(f"[k: {k}]")
                # print(f"[h: {diff}, h^2: {diff2}]")
                p = k + diff
                q = k - diff
                # print(f"[p: {p}, q: {q}]")
                tot = (p-1)*(q-1)
                # print(f"[totient: {tot}]")
                d = pow(e,-1,tot)
                # print(f"[d: {d}]")
                m_int = pow(c,d,n)
                m_asli = long_to_bytes(m_int).decode()
                return m_asli
            k += 1
    elif (paket_soal=='B'):
        p = int(Decimal(n).sqrt())
        # print(f"[p: {p}]")
        # print(isPrime(p))
        tot = (p)*(p-1)
        # print(f"[tot: {tot}]")
        d = pow(e, -1, tot)
        # print(f"[d: {d}]")
        m_int = pow(c, d, n)
        m_asli = long_to_bytes(m_int).decode() 
        return m_asli
    elif (paket_soal=='C'):
        for d in range(2**15,(2**16)+1):
            try:
                m_int = pow(c,d,n)
                m_asli = long_to_bytes(m_int).decode()
                if(m_asli.startswith("KRIPTOGRAFIITB{")):
                    # print(f"[nilai d yang tepat: {d}]")
                    return m_asli
            except Exception as e:
                continue
    elif (paket_soal=='D'):
        m_int = find_cube_root(c)
        m_asli = long_to_bytes(m_int).decode()
        return m_asli
    elif (paket_soal=='E'):
        totient = n-1 # because n is prime
        d = pow(e, -1, totient)
        m = pow(c, d, n)
        return long_to_bytes(m).decode()
    return "0"

def netcat(hn, p):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((hn,p))
    file = sock.makefile("rb")
    print(file.readline().decode())
    token = "u46S5y327z\n"
    sock.send(token.encode())
    paket_soal = "A"
    n = 0
    e = 0
    c = 0
    m_asli = "30\n"
    for _ in range(3):
        print(file.readline().decode())
    for _ in range(30):
        print(file.readline().decode())
        res = file.readline().decode()
        print(res)
        paket_soal = res.split('=')[-1].strip().strip('\n')
        res = file.readline().decode()
        print(res)        
        n = res.split('=')[-1].strip().strip('\n')
        res = file.readline().decode()
        print(res)
        e = res.split('=')[-1].strip().strip('\n')
        res = file.readline().decode()
        print(res)        
        c = res.split('=')[-1].strip().strip('\n')
        n = int(n)
        e = int(e)
        c = int(c)
        m_asli = solve(paket_soal,n,e,c)
        sock.send(m_asli.encode())
        print(file.readline().decode(), m_asli)
        time.sleep(1)
    print(file.readline().decode()) # flag
    sock.close()

netcat("165.232.161.196", 4020)