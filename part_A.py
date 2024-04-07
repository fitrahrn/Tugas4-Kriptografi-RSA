import socket

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
        for _ in range(4):
            print(file.readline().decode())
        m_asli = solve(paket_soal,n,e,c)
        sock.send(m_asli.encode())
        for _ in range(2):
            print(file.readline().decode())
    print(file.readline().decode()) # flag
    sock.close()

netcat("165.232.161.196", 4020)