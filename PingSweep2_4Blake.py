import ipaddress
# ask user for network
address = []
netnum = 0
network = input("Please enter start of network as type x.x.x :")
# print(network)
while netnum < 255:
    ip = str(str(network) + "." + str(netnum))
    address.append(ip)
    netnum +=1
# print(address)

import socket

# Get ports from users
ports=[]
print("Please enter ports one at a time")
print('press X to finish')

while True:
    port = input("Port: ")
    if port.isdigit() and int(port) >0 and int(port) < 65536:
        ports.append(port)
    elif port == "x" or port == "x":
        break
    else:
        print("Please input a valid port")
        print("Numbers between 0 and 65535")

# print(ports)

# print a list of each IP with each port
for ip in address:
    for i in ports:
        print(ip + ":" + i)

# host = "192.168.100.67"
# p = 90
# s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# s.connect((host,p))
# print("We connected")
# s.close


def portscan(ip, port):
    try:
        socket.setdefaulttimeout(1)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result= sock.connect_ex((ip, int(port)))
        if result == 0:
            print("IP: ", ip,",", port, "Open")
        #else:
            #print("IP:, ":", port, "Closed/Filtered or host is offline")
        sock.close()

    except KeyboardInterrupt:
        print ("You press Ctrl+c")
        sys.exit()
    except socket.error:
        print("Cant connecto to IP: ", ip)
        sys.exit()

for ip in address:
    for i in ports:
        portscan(ip,i)
