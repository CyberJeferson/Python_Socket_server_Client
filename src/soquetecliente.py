import socket
from tkinter import*

#Python socket client by Jeferson Oliveira
   
#ESSE É O CLIENTE ESSE CÓDIGO DEVER SER ADAPTADO NO PROJETO
HOST = 'ip' #DEFINE O IP DO SERVIDOR 
PORT = 11000
tela = Tk() 

def LerComando(comando): 
    
    if comando == "b1": 
        botao['text'] = "1" 
    

def de():   #ESSA FUNÇÃO INFORMA QUE ESTÁ ONLINE AO SERVIDOR VAI RODAR EM LOOP
        EnviarMenssagem("on")
        tela.after(100, de)
def EnviarMenssagem(msg):  
     
    try: #PARA TRATAMENTO DE ERROS
        CLIENTE = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        
        CLIENTE.connect((HOST,PORT)) 
        CLIENTE.sendall(str.encode(msg)) 
        data = CLIENTE.recv(1024)    
        print("Resposta do servidor:", data.decode())
        CLIENTE.close()
        LerComando(data.decode())
        data = ""
    except:
        CLIENTE.close()
       
        
    
    CLIENTE.close()


       
        
   


 




#EXEMPLO COM UM BOTÃO=====================

def btn1clique(): #MÉTODOPARA O CLIQUE DO BOTÃO
    botao['text'] = "1" #O TEXTO DO BOTÃO MUDARÁ PARA 1
    EnviarMenssagem("b1")# ENVIA ESSA INFORMAÇÃO AO SERVIDOR SOCKET
    


 
    





    
tela.title('Exemplo') #TITULO DA TELA DO FORMULARIO
tela.geometry('720x500') #TAMANHO DA TELA
botao = Button(tela, text="   ", command = lambda:btn1clique()) #CRIA UM BOTÃO QUE COM O EVENTO DE CLIQUE QUE MÉTODO btnclique()
botao.grid()#DESENHA O BOTÃO NA TELA
botao['width'] = 30 #DEFINE O TAMANHO HORIZONTAL DO BOTÃO
botao['height'] = 20 #DEFEINE A ALTURA DO BOTÃO
tela.after(100, de)
tela.mainloop()# COLOCA O FORMULARIO EM LOOP PRINCIPAL

    


    
