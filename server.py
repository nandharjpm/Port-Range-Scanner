# size=int(input())
# a=[]
# for i in range(size):
#     e=int(input("$ "))
#     a.append(e)
# for j in a:
#     c= j%2
#     if c==0:
#         print("even -> ",j,end=" ")
#         print()
#     elif c==1:
#         print("odd -> ",j,end=" ")
#         print()

# inp1=input()
# inp2=input()
# count=0
# for i in inp1:
#     for j in inp2:
#         if i==j:
#             count+=1
# print(count)

# inti=list(map(int,input().split()))
# for i in inti:
#     c=i%10 + i//10
#     print(c)
#
#     d=i%10
#     up=i//10

# init=list(map(int,input().split()))
# b=[]
# for i in init:
#     sum = 0
#     while i!=0:
#         rem=i%10
#         sum+=rem
#         i//=10
#     b.append(sum)
# print(b)

# init1=int(input())
# init2=int(input())
# for i in range(init1):
#     for j in range(init2):
#         if i==j:
#             print("Same")
#             break
#         elif i!=0:
#             print("Not Same")
#         break

# import math
# num=float(input())
# print(int(num))
# print(math.ceil(num))
# print(math.floor(num))


# import socket
# s=socket.socket()
# host=socket.gethostname()
# port=1234
# s.bind((host,port))
# s.listen(5)
# while 1:
#     connect,address=s.accept()
#     print("connection from ", address)
#     connect.send(b'you connected to in snk host')
#     connect.close()


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

# C:\Users\Nandhakumar\PycharmProjects\pytest.py\server.py


















