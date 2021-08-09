import socket
import os
cmd = "vazio" 

#Pyton socket server by Jeferson Oliveira
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
sock.bind(("IP", 11000))
  
def inciarSocket(): #MÉTODO QUE INICIA O SOCKET
   
    try:
       
        sock.listen(1) 
        print ("Aguardando o cliente se conectar") 
        clientes()
    except:
      clientes()

      
  
def clientes(): 
    
    while True:
        
        (client, (ip, port)) = sock.accept() 
        try:            
            print ('Cliente conectado no ip {} e a porta {}'.format(ip, port)) 
            data = client.recv(1024)  
            while len(data):
                print (data.decode())
                if data.decode() == "b1": 
                    global cmd               
                    cmd = data.decode()              
                    client.send(bytes("Gravado o comando", "utf-8"))
                    data =""
                   
                    client.close()
                   
                else:#SE NÃO
                    if data.decode() == "on":              
                        client.send(bytes(cmd,"utf-8"))
                        data =""
                       
                        client.close()                   
                      

                    else:
                        client.send(bytes("----------------", "utf-8"))
                        data =""                        
                        client.close()
            client.close()       
            data =""     

            
            
            
        except:  
            client.close()
            data =""                  
            print('Erro')
            os.system('cls' if os.name == 'nt' else 'clear')
           
            
           
           

inciarSocket() # CHAMA O METODO QUE COLOCA O SERVIDOR EM MODO DE ESCUTA


