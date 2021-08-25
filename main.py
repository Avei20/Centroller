#!/usr/bin/python3

import serial 
import serial.tools.list_ports as listPort
import tkinter
from tkinter import PhotoImage, ttk
from tkinter.messagebox import showinfo
import time 

def quit_btn () : 
    # global tkTop
    white_status.set('White Off')
    biru_status.set('Biru Off')
    ser.write(bytes('L', 'UTF-8'))
    ser.write(bytes('I', 'UTF-8'))
    # tkTop.destroy()

def white_on_button() :
    white_status.set('White On')
    ser.write(bytes('H', 'UTF-8'))

def white_off_button() : 
    white_status.set('White Off')
    ser.write(bytes('L', 'UTF-8'))

def biru_on_button () : 
    biru_status.set('Biru On')
    ser.write(bytes('K', 'UTF-8'))

def biru_off_button() : 
    biru_status.set('Biru Off')
    ser.write(bytes('I', 'UTF-8'))

def ganti_port (event) : 
    port = combo_port.get()
    print (port)
    ser = serial.Serial(port, 9600)
    msg = f'Changed into {port}'
    showinfo(title='Ganti Port', message=msg)
    print (ser.isOpen())


ports = listPort.comports()

list_port = []

for port, desc, hwid in sorted(ports):
    list_port.append (port)

default_port = list_port[0]


tkTop = tkinter.Tk()
tkTop.geometry('300x500')
tkTop.title('LED Controller Avei')

icon = PhotoImage(file = 'led-icon-25.png')
tkTop.iconphoto(False, icon)

com_label = tkinter.Label(text = 'Pilih Port Arduino-nya: ')
com_label.pack()

avail_port = tkinter.StringVar()

combo_port = ttk.Combobox(tkTop, textvariable=avail_port)
combo_port['values'] = list_port
combo_port['state'] = 'readonly'
combo_port.pack()

combo_port.bind('<<ComboboxSelected>>', ganti_port)

# button0 = tkinter.IntVar()
# button0state = tkinter.Button(tkTop, 
#     text = 'Restart Serial', 
#     command = ganti_port(port, com_input.get()),
#     height = 2, 
#     width = 8,
# )
# button0state.pack(side='top', ipadx=10, padx=10, pady=15)

ser = serial.Serial(port , 9600)
print (ser.isOpen())

title_label = tkinter.Label(text = 'LED STATUS', )
title_label.pack()

white_status = tkinter.IntVar()
white_status_label = tkinter.Label(textvariable = white_status, )
white_status.set ('White Off')
white_status_label.pack()

biru_status = tkinter.IntVar()
biru_status_label = tkinter.Label(textvariable = biru_status, )
biru_status.set('Biru Off')
biru_status_label.pack()


button1 = tkinter.IntVar()
button1state = tkinter.Button(tkTop, 
    text="White On", 
    command=white_on_button, 
    height=2, 
    width=8,
)

button1state.pack(side='top', ipadx=10, padx=10, pady=15)

button2 = tkinter.IntVar()
button2state = tkinter.Button(tkTop, 
    text = 'White Off',
    command = white_off_button, 
    height = 2, 
    width = 8, 
)

button2state.pack (side='top', ipadx=10, padx=10, pady=15)

button3 = tkinter.IntVar()
button3state = tkinter.Button(tkTop, 
    text = 'Biru On',
    command = biru_on_button, 
    height = 2, 
    width = 8, 
)

button3state.pack (side='top', ipadx=10, padx=10, pady=15)

button4 = tkinter.IntVar()
button4state = tkinter.Button(tkTop, 
    text = 'Biru Off',
    command = biru_off_button, 
    height = 2, 
    width = 8, 
)

button4state.pack (side='top', ipadx=10, padx=10, pady=15)

tkButtonQuit = tkinter.Button(tkTop, 
    text = 'Tidur', 
    command = quit_btn, 
    height = 2, 
    width=8, 
    )

tkButtonQuit.pack(side='top', ipadx=10, padx=10, pady=15)
tkinter.mainloop()
