import socket
from chatwindow import *
from tkinter import *

from threading import Thread
flag=False
def test(chat):
    def entry_made():
        global flag
        
        flag=True
    def chunkstring(string, length):
        return (string[0+i:length+i] for i in range(0, len(string), length))

    global flag
    host = socket.gethostname()  # as both code is running on same pc
    port = 5010  # socket server port number

    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server
    chat.submit.configure(command=entry_made,state=DISABLED)
    chat.submit.configure(state=NORMAL)
    while not flag:
        pass
    message=str(chat.text_var.get())
   
    chat.text_var.set('')
    flag=False
    chat.submit.configure(state=DISABLED)
    data=list(chunkstring(message, 20))
    data=('\n').join(data)
    prev=chat.chat
    new_msg="\n"+"You: "+data
    data=str(prev)+new_msg
        
        
    
    chat.chat=data
    chat.textarea.delete('msgs')
    chat.textarea.create_text(140,10,fill="darkblue",font="Times 12 italic bold",
                        text=data,tags='msgs')

    while message.lower().strip() != 'bye':
        client_socket.send(message.encode())  # send message
        data = client_socket.recv(1024).decode()  # receive response
        data=list(chunkstring(data, 20))
        data=('\n').join(data)
        
        
        prev=chat.chat
        
        new_msg="\n"+"Care: "+str(data)
        data=str(prev)+new_msg
       
        
        
        
        chat.textarea.delete('msgs')
        chat.chat=data
        chat.textarea.create_text(140,10,fill="darkblue",font="Times 12 italic bold",
                        text=data,tags='msgs')

        

        chat.submit.configure(command=entry_made,state=DISABLED)
        chat.submit.configure(state=NORMAL)
        while not flag:
            pass
        message=str(chat.text_var.get())
   
        chat.text_var.set('')
        flag=False
        chat.submit.configure(state=DISABLED)
        data=list(chunkstring(message, 20))
        data=('\n').join(data)
        prev=chat.chat
        new_msg="\n"+"You: "+data
        data=str(prev)+new_msg
        
        
        
        chat.chat=data
        chat.textarea.delete('msgs')
        chat.textarea.create_text(140,10,fill="darkblue",font="Times 12 italic bold",
                        text=data,tags='msgs')
    
    client_socket.close()  

def client_program():
    chat=chatwindow()
    
    t=Thread(target=test,args=[chat])
    t.start()
    chat.root.mainloop()


if __name__ == '__main__':
    client_program()

