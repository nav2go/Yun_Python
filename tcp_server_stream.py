import socket

TCP_IP = '192.168.2.126'
TCP_PORT = 5005
BUFFER_SIZE = 20  # Normally 1024, but we want fast response

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

try: 
    while True: 
        komm, addr = s.accept() 
        while True: 
            data = komm.recv(BUFFER_SIZE)

            if not data: 
                komm.close() 
                break

            #print "[%s] %s" % (addr[0], data) 
            # nachricht = raw_input("Antwort: ") 
            nachricht = "0102030405060708090102030405060701020304050607"
            komm.send(nachricht) 
finally: 
    s.close()