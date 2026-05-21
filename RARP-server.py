import socket 

s = socket.socket() 
s.bind(('localhost', 9000)) 
s.listen(5) 

c, addr = s.accept() 

address = {
    "6A:08:AA:C2": "192.168.1.100",
    "8A:BC:E3:FA": "192.168.1.99"
}

while True: 
    ip = c.recv(1024).decode() 
    if not ip:
        break
    try: 
        c.send(address[ip].encode()) 
    except KeyError: 
        c.send("Not Found".encode()) 

c.close()
