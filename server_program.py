import socket
from chatwindow import *
from tkinter import *

from threading import Thread

flag=False
def test(chat):
    
    
    def chunkstring(string, length):
        return (string[0+i:length+i] for i in range(0, len(string), length))

    def entry_made():
        global flag
        
        flag=True
        
    
    
    
    global flag
    host=socket.gethostname()
    port=5010


    server_socket=socket.socket()

    server_socket.bind((host,port))

    server_socket.listen(10)
    conn,addr=server_socket.accept()
    print("Connection from: "+str(addr))

    chat.submit.configure(command=entry_made,state=DISABLED)
    while True:
        
        data=conn.recv(2056).decode()
        if not data:
            
            break
        data=list(chunkstring(data, 20))
        data=('\n').join(data)
        
        
        prev=chat.chat
        #print("prev is"+prev)
        #chat.textarea.delete("1.0",END)
        new_msg="\n"+"User: "+str(data)
        data=str(prev)+new_msg
        #chat.textarea.insert(END,str(data))
        #chat.text_var.set(data)
        
        
        
        chat.textarea.delete('msgs')
        chat.chat=data
        chat.textarea.create_text(140,10,fill="darkblue",font="Times 12 italic bold",
                        text=data,tags='msgs')

        chat.submit.configure(state=NORMAL)
        while not flag:
            pass
        data=str(chat.text_var.get())
        print(data)
        chat.text_var.set('')
        flag=False
        chat.submit.configure(state=DISABLED)
        conn.send(data.encode())
        data=list(chunkstring(data, 20))
        data=('\n').join(data)
        prev=chat.chat
        new_msg="\n"+"You: "+data
        data=str(prev)+new_msg
        
        
        
        chat.chat=data
        chat.textarea.delete('msgs')
        chat.textarea.create_text(140,10,fill="darkblue",font="Times 12 italic bold",
                        text=data,tags='msgs')
        
        
        
    
    
    conn.close()
    
    
    
    
    
    
def server_program():
   
    chat=chatwindow()
    chat.submit.configure(state=DISABLED)
    t=Thread(target=test,args=[chat])
    t.start()
    chat.root.mainloop()
    
    
    

if __name__=='__main__':
    server_program()
