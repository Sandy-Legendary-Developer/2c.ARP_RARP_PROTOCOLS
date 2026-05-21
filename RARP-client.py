import socket 

s = socket.socket() 
s.connect(('localhost', 9000)) 

while True: 
    mac = input("Enter MAC Address: ") 
    if not mac:   # stop if user presses Enter without input
        break
    s.send(mac.encode()) 
    ip = s.recv(1024).decode() 
    print("Logical Address:", ip) 

s.close()