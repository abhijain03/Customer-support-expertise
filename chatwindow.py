from tkinter import *

class chatwindow:
    def __init__(self):
        
        self.root=Tk()
        self.root.geometry("600x500")
        self.textareaf=Frame(self.root)
        self.text_var=StringVar()
        self.chat=""
        #self.textarea=Entry(self.textareaf,width=80,height,textvariable=self.text_var)
        self.textarea = Canvas(self.textareaf, width=550, height=400, bg = '#afeeee')
        self.scroll=Scrollbar(self.textareaf)
        self.scroll.pack(side=RIGHT,fill=Y)
        self.scroll.config(command=self.textarea.yview)
        self.textarea.config(yscrollcommand=self.scroll.set)
        self.textarea.pack(side=LEFT)
        self.textareaf.pack(side=TOP)
        self.panel=Frame(self.root,pady=0)
        self.label=Label(self.panel,text="Enter your message here:")
        self.label.place(x=10)
        self.msg=Entry(self.panel,width=70,textvariable=self.text_var)
        self.msg.pack(side=LEFT)
        self.submit=Button(self.panel,text='submit')
        self.submit.pack(side=RIGHT,padx=12,pady=20)
        self.panel.pack(side=BOTTOM,pady=0)
        #root.mainloop()

    
if __name__=='__main__':
    
    chatwindow()


