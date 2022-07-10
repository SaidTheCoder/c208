#-----------Bolierplate Code Start -----
import socket
from threading import Thread
from tkinter import *
from tkinter import ttk


PORT  = 8080
IP_ADDRESS = '127.0.0.1'
SERVER = None
BUFFER_SIZE = 4096

name=None
listBox=None
textArea=None
labelChat=None
text_message=None

def connectToServer():
    global SERVER
    global name
    global sending_file

    cName=name.get()
    SERVER.send(cName.encode())


def openChatWindow():
    window=Tk()
    window.title("Messenger")
    window.geometry("500x350")

    global name
    global listBox
    global textArea
    global labelChat
    global text_message
    global filePathLabel

    nameLabel=Label(window,text="Enter your name:",font=("Calibri",10))
    nameLabel.place(x=10,y=8)

    name=Entry(window,width=30,font=("Calibri",10))
    name.place(x=120,y=8)
    # ill get 2 number 9s a number 9 large...
    connectServer=Button(window,text="Connect to chat server",font=("Calibri",10),bd=2,command=connectToServer())
    connectServer.place(x=350,y=6)

    separator=ttk.Separator(window,orient="horizontal")
    separator.place(x=0,y=35,relwidth=1,height=0.1)

    labelUsers=Label(window,text="Active Users",font=("Calibri",10))
    labelUsers.place(x=10,y=50)

    listBox=Listbox(window,height=5,width=65,font=("Calibri",10))
    listBox.place(x=10,y=70)

    connectButton=Button(window,text="Connect",font=("Calibri",10),bd=2)
    connectButton.place(x=280,y=160)

    disconnectButton=Button(window,text="Disconnect",font=("Calibri",10),bd=2)
    disconnectButton.place(x=350,y=160)

    refresh=Button(window,text="Refresh",font=("Calibri",10),bd=2)
    refresh.place(x=430,y=160)

    labelChat=Label(window,text="Chat Window",font=("Calibri",10))
    labelChat.place(x=10,y=180)
    
    textArea=Text(window,height=6,width=65,font=("Calibri",10))
    textArea.place(x=10,y=200)

    attach=Button(window,text="Attach and Send",font=("Calibri",10),bd=2)
    attach.place(x=10,y=305)

    send=Button(window,text="Send",font=("Calibri",10),bd=2)
    send.place(x=450,y=305)

    text_message=Entry(window,width=42,font=("Calibri",12))
    text_message.pack()
    text_message.place(x=100,y=305)

    filePathLabel=Label(window,text="",font=("Calibri",10))
    filePathLabel.place(x=10,y=345)

    scrollBar1=Scrollbar(listBox)
    scrollBar1.place(relheight=1,relx=1)
    scrollBar1.config(command=listBox.yview)

    scrollBar2=Scrollbar(textArea)
    scrollBar2.place(relheight=1,relx=1)
    scrollBar2.config(command=listBox.yview)

    window.mainloop()


def setup():
    global SERVER
    global PORT
    global IP_ADDRESS

    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.connect((IP_ADDRESS, PORT))
    openChatWindow()

setup()


#-----------Bolierplate Code Start -----