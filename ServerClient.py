import pexpect
import paramiko 
import scp
from paramiko import SSHClient
from scp import SCPClient
import os
import platform
import tkinter as tk
from tkinter.ttk import *
from tkinter import messagebox as msg
from tkinter.ttk import Notebook
from tkinter import ttk
import tkinter.messagebox as tkmsg
import subprocess
import threading

class Server_Client():

    def __init__(self, master):
        self.parent = master
        self.SERVER_USER = tk.StringVar()
        self.SERVER_USER.set('')
        self.CLIENT_USER = tk.StringVar()
        self.CLIENT_USER.set('')
        self.SERVER_ADDRESS = tk.StringVar()
        self.SERVER_ADDRESS.set('')
        self.CLIENT_ADDRESS = tk.StringVar()
        self.CLIENT_ADDRESS.set('')
        self.SERVER_PASSWD = tk.StringVar()
        self.SERVER_PASSWD.set('')
        self.CLIENT_PASSWD = tk.StringVar()
        self.CLIENT_PASSWD.set('')


        self.ServerClientPanel = tk.LabelFrame(self.parent, text="Server and Client",font=('Courier', 10))
        self.ServerClientPanel.pack(side=tk.LEFT, expand=tk.YES, fill = tk.BOTH)        
        self.init_runServerAndClient_tab()
        
    def init_runServerAndClient_tab(self):
        self.runServerAndClient_tab = tk.Frame(self.ServerClientPanel)
        self.runServerAndClient_tab.pack(side = tk.LEFT, expand=tk.YES, fill=tk.BOTH)

        self.runServerFrame = tk.LabelFrame(self.runServerAndClient_tab , text="Run Server Terminal",font=('Courier', 10))
        self.runServerFrame.pack(side=tk.TOP, expand=tk.NO, fill = tk.BOTH)
        
        self.ServerCtrFrame = tk.LabelFrame(self.runServerFrame , text="Control Server",font=('Courier', 10))
        self.ServerCtrFrame.pack(side=tk.TOP, expand=tk.NO, fill = tk.BOTH)
        
        self.runClientFrame = tk.LabelFrame(self.runServerAndClient_tab , text="Run Client Terminal",font=('Courier', 10))
        self.runClientFrame.pack(side=tk.TOP, expand=tk.NO, fill = tk.BOTH)        
        
        self.ClientCtrFrame = tk.LabelFrame(self.runClientFrame , text="Control Client",font=('Courier', 10))
        self.ClientCtrFrame.pack(side=tk.TOP, expand=tk.NO, fill = tk.BOTH)        
        
        self.runServerButton = tk.Button(self.ServerCtrFrame, text = "Run Server",font=('Courier', 10), command = self.runServer)
        self.runServerButton.pack(side=tk.LEFT, expand=tk.NO, fill = tk.X)
        
        self.ServerConfButton = tk.Button(self.ServerCtrFrame, text = "Server Config",font=('Courier', 10), command= self.serverConf)
        self.ServerConfButton.pack(side=tk.LEFT, expand=tk.NO, fill = tk.X)
        
        tk.Label(self.ServerCtrFrame, text='IP Address', font=('Courier', 10),width=15, height=2).pack(side=tk.LEFT, expand=tk.NO, fill = tk.X)
        
        self.serverIP = tk.Entry(self.ServerCtrFrame, textvariable=self.SERVER_ADDRESS)
        self.serverIP.pack(side=tk.LEFT, expand=tk.NO, fill = tk.X)
        
        tk.Label(self.ServerCtrFrame, text='User', font=('Courier', 10),width=15, height=2).pack(side=tk.LEFT, expand=tk.NO, fill = tk.X)
        self.serverUser = tk.Entry(self.ServerCtrFrame, textvariable=self.SERVER_USER)
        self.serverUser.pack(side=tk.LEFT, expand=tk.NO, fill = tk.X)
        
        tk.Label(self.ServerCtrFrame, text='Password', font=('Courier', 10),width=15, height=2).pack(side=tk.LEFT, expand=tk.NO, fill = tk.X)
        self.serverPasswd = tk.Entry(self.ServerCtrFrame, textvariable=self.SERVER_PASSWD, show = "*")
        self.serverPasswd.pack(side=tk.LEFT, expand=tk.NO, fill = tk.X)        
        
        self.ServerTerminal = tk.Frame(self.runServerFrame, height = 350)
        self.ServerTerminal.pack(side=tk.BOTTOM, expand=tk.YES, fill = tk.BOTH)  
        
        self.runClientButton = tk.Button(self.ClientCtrFrame, text = "Run Client",font=('Courier', 10),command = self.runClient)
        self.runClientButton.pack(side=tk.LEFT, expand=tk.NO, fill = tk.X)

        self.ClientConfButton = tk.Button(self.ClientCtrFrame, text = "Client Config",font=('Courier', 10), command= self.ClientConf)
        self.ClientConfButton.pack(side=tk.LEFT, expand=tk.NO, fill = tk.X) 
        
        tk.Label(self.ClientCtrFrame, text='IP Address', font=('Courier', 10),width=15, height=2).pack(side=tk.LEFT, expand=tk.NO, fill = tk.X)
        
        self.ClientIP = tk.Entry(self.ClientCtrFrame,textvariable=self.CLIENT_ADDRESS)
        self.ClientIP.pack(side=tk.LEFT, expand=tk.NO, fill = tk.X) 
        
        tk.Label(self.ClientCtrFrame, text='User', font=('Courier', 10),width=15, height=2).pack(side=tk.LEFT, expand=tk.NO, fill = tk.X)
        
        self.ClientUser = tk.Entry(self.ClientCtrFrame, textvariable=self.CLIENT_USER)
        self.ClientUser.pack(side=tk.LEFT, expand=tk.NO, fill = tk.X)       
        
        tk.Label(self.ClientCtrFrame, text='Password', font=('Courier', 10),width=15, height=2).pack(side=tk.LEFT, expand=tk.NO, fill = tk.X)
        
        self.ClientPasswd = tk.Entry(self.ClientCtrFrame, textvariable=self.CLIENT_PASSWD, show = "*")
        self.ClientPasswd.pack(side=tk.LEFT, expand=tk.NO, fill = tk.X)        
        
        self.ClientTerminal = tk.Frame(self.runClientFrame, height = 350)
        self.ClientTerminal.pack(side=tk.TOP, expand=tk.YES, fill = tk.BOTH)
            
    def runServer(self, event = None):
        Serverframe_id = self.ServerTerminal.winfo_id()
        subprocess.Popen(["xterm","-into", str(Serverframe_id), "-geometry", "200x30", "-e", "python3","runServer1.py", self.SERVER_ADDRESS, self.SERVER_USER, self.SERVER_PASSWD])
      
    def runClient(self, event = None):
        Clientframe_id = self.ClientTerminal.winfo_id()
        subprocess.Popen(["xterm","-into", str(Clientframe_id), "-geometry", "200x30", "-e", "python3","runClient1.py", self.CLIENT_ADDRESS, self.CLIENT_USER, self.CLIENT_PASSWD])

    def serverConf(self, event = None):
        self.SERVER_ADDRESS = self.serverIP.get()
        self.SERVER_USER = self.serverUser.get()
        self.SERVER_PASSWD = self.serverPasswd.get()
        tkmsg.showinfo("Information","IP Address:"+self.SERVER_ADDRESS+" User:"+self.SERVER_USER+" Pass Word:"+self.SERVER_PASSWD)
        #print(self.SERVER_ADDRESS+self.SERVER_USER+self.SERVER_PASSWD)
        
    def ClientConf(self, event = None):
        self.CLIENT_ADDRESS = self.ClientIP.get()
        self.CLIENT_USER = self.ClientUser.get()
        self.CLIENT_PASSWD = self.ClientPasswd.get()
        tkmsg.showinfo("Information","IP Address:"+self.CLIENT_ADDRESS+" User:"+self.CLIENT_USER+" Pass Word:"+self.CLIENT_PASSWD)


#--------------------------------------------------------
# main
#--------------------------------------------------------
if __name__ == '__main__':
    root = tk.Tk()
    Server_Client(root)
    #root.resizable(width=True, height=True)
    #root.geometry(MAIN_DISPLAY_SIZE)
    root.mainloop()

