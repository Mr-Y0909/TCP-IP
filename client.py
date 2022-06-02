import socket
import threading


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('10.2.205.86', 22000))


def receive():
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            print(message)
            
        except:
           
            print("An error occured!")
            client.close()
            break

def write():
    while True:
        message = 'client: {}'.format(input(''))
        client.send(message.encode('ascii'))
        
        
receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
