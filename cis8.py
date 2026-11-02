import socket 
import threading  

def monitor():     
    server = socket.socket()     
    server.bind(("127.0.0.1", 9999))     
    server.listen(5)     
    print("IDS Started - Monitoring Network...")      
    while True:         
        conn, addr = server.accept()         
        print("ALERT: Connection Detected!", addr[0])         
        conn.close()  
threading.Thread(target=monitor, daemon=True).start()  
client = socket.socket() 
client.connect(("127.0.0.1", 9999)) 
print("Test Connection Successful!") 
client.close()
