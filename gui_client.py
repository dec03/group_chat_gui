import socket
import _tkinter
import time
import threading
import tkinter.font as font
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.ttk import Combobox
from tkinter import filedialog
from tkinter.filedialog import askopenfile


#insert timed loop that will check for msg every 2 seconds
host = socket.gethostname()
port = 12345
quit = False

c_s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
con = c_s.connect((host, port))

host_ip = socket.gethostbyname(host)

client_name = input('Username: ')
c_s.send(client_name.encode())

while quit != True:
    #functions for gui
    def recieve_message(*args):
        #data = str(f'{c_s.getsockname()}: ')
        message = c_s.recv(1024).decode()  # receive response
        new_pos = chat_window.size()
        chat_window.insert(new_pos,message)
        #print(message)
        return

    def send_message(*args):
        new_pos = chat_window.size()
        msg = str(entry_box.get())
        entry_box.delete(0,END)
        if msg == '':
            return
        #chat_window.insert(new_pos,msg)
        c_s.sendall(msg.encode())  # send message
        if msg.strip() == 'bye':
            new_pos = chat_window.size()
            msg = str(entry_box.get())
            entry_box.delete(0,END)
            quit = True
            connection = Label(chat_frame,
            width = 25,
            height = 1,
            relief = SUNKEN,
            text = 'No Connection',
            bg = 'red')
            connection.place(y=52, x=196)
            c_s.close()
        return


    def open_file():
        file_path = askopenfile(mode='r', filetypes=[('Image Files', '*jpeg')])
        new_pos = chat_window.size()
        chat_window.insert(new_pos,'''''')
        if file_path is not None:
            pass

    def connection_status(*args):

        if con == None:
            #info for connection
            connection = Label(chat_frame,
            width = 25,
            height = 1,
            relief = SUNKEN,
            text = 'Connected',
            bg = 'lightgreen')
            connection.place(y=52, x=196)
            return
        else:
            #info for connection
            connection = Label(chat_frame,
            width = 25,
            height = 1,
            relief = SUNKEN,
            text = 'No Connection',
            bg = 'red')
            connection.place(y=52, x=196)
            return

    def main():
        threading.Timer(1, main).start()
        #print('here')
        recieve_message()


#-----------------------------------

    #main window
    root = Tk()
    #sets window background colour
    root.configure(bg='black')
    #sets window size but is still resizable
    root.geometry('500x600')

    #-----------------------------------------

    #------------------------------------------
    #frames
    mainFrame = Frame(root,
    width=500,
    height=600,
    background='#1d3868')
    mainFrame.pack()

    chat_frame = Frame(mainFrame,
    width=500,
    height=600,
    background='#1d3868')
    chat_frame.place(y=100, x=50)

    #-----------------------------------------


    #widgets
    chat_window = Listbox(chat_frame,
    relief=SUNKEN,
    width=59,
    height=20,
    font=("Arial", 8))
    chat_window.place(x=18,y=102 )

    msg = StringVar()
    entry_box = Entry(chat_frame,
    width=45,
    relief=SUNKEN,
    text=msg)
    entry_box.bind("<Return>", send_message)
    entry_box.place(x=18,y=433, height=55)



    #button to send image
    send = Button(chat_frame,
    relief=RAISED,
    width=8,
    height=1,
    text='Send',
    activebackground='white',
    command=send_message)
    send.place(x=310,y=463)

    #button to upload
    upload = Button(chat_frame,
    relief=RAISED,
    width=8,
    height=1,
    text='Upload',
    activebackground='white',
    command=open_file)
    upload.place(x=310,y=433)


    #info for ip address
    ip_title = Label(chat_frame,
    width = 25,
    height = 1,
    relief = SUNKEN,
    text = 'IP Address:')
    ip_title.place(y=10, x=16)

    #info for ip address
    ip = Label(chat_frame,
    width = 25,
    height = 1,
    relief = SUNKEN,
    text = host_ip)
    ip.place(y=10, x=196)

    #info for port
    port_title = Label(chat_frame,
    width = 25,
    height = 1,
    relief = SUNKEN,
    text = 'Port Number:')
    port_title.place(y=31, x=16)

    #info for port
    port = Label(chat_frame,
    width = 25,
    height = 1,
    relief = SUNKEN,
    text = port)
    port.place(y=31, x=196)

    #info for connection
    connection_title = Label(chat_frame,
    width = 25,
    height = 1,
    relief = SUNKEN,
    text = 'Connection Status:')
    connection_title.place(y=52, x=16)
    '''
    #info for connected
    server_title = Label(chat_frame,
    width = 25,
    height = 1,
    relief = SUNKEN,
    text = f'Connected to: ')
    server_title.place(y=73, x=16)

    #info for connected
    server = Label(chat_frame,
    width = 25,
    height = 1,
    relief = SUNKEN,
    text=server_address)
    #text)
    server.place(y=73, x=196)
    '''
    connection_status()
    main()


    #-------------------------------------------
    root.mainloop()
