import socket

domain=input("Enter Your Target Domain Name : ")
ip=socket.gethostbyname(domain)
srange=int(input("Enter the starting range of port : "))
erange=int(input("Enter the ending range of port : "))

for port in range(srange,erange+1):
    s = socket.socket()
    s.settimeout(1)
    res = s.connect_ex((ip, port))
    if res == 0:
        print(port, "open in", ip)
    else:
        print(port," is closed")
    s.close()
