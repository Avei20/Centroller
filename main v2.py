#!/usr/bin/python3

from base64 import decode
from cProfile import label
from turtle import title
import serial 
import serial.tools.list_ports as listPort 
import re
import tkinter 
from tkinter import PhotoImage, ttk
from tkinter.messagebox import showinfo
import time

decoder = 'UTF-8'

def connect (event) : 
    port = combo_port.get()
    print(port)
    console.port = port
    print(console.isOpen)
    console.open()
    if console.isOpen() :
        msg = f'Connection Start at {port}'
        showinfo(title='Change Port', message=msg)
        update_lamp(lampStat)

def update_lamp(lampList) :
    for i in range(3) : 
        temp = console.readline()
        result = temp.decode('UTF-8')
        lampStat[i] = result[0]
        # print(type(result[0]))
    print(lampStat)

def white() :
    stat = lampStat[0]
    # print (stat)
    if stat == '0' : 
        white_status.set('White On')
        console.write(bytes('H', decoder))
        lampStat[0] = '1'
    if stat == '1' : 
        white_status.set('White Off')
        console.write(bytes('L', decoder))
        lampStat[0] = '0'

def blue () :
    stat = lampStat[1]
    if stat == '0' : 
        blue_status.set('Blue On')
        console.write(bytes('K', decoder))
        lampStat[1] = '1'
    if stat == '1' : 
        blue_status.set('Blue Off')
        console.write(bytes('I', decoder))
        lampStat[1] = '0'

def table() :
    stat = lampStat[2]
    if stat == '0' : 
        table_status.set('Table On')
        console.write(bytes('B', decoder))
        lampStat[2] = '1'
    if stat == '1' : 
        table_status.set('Table Off')
        console.write(bytes('A', decoder))
        lampStat[2] = '0'

def sleeping() : 
    white_status.set('White Off') 
    blue_status.set('Blue Off')
    table_status.set('Table Off')
    console.write(bytes('A', decoder))
    console.write(bytes('L', decoder))
    console.write(bytes('I', decoder))

console = serial.Serial()
console.baudrate = 9600


ports = listPort.comports()
portList = []

for port, _, _ in sorted(ports) : 
    portList.append(port)
    # print ()
    
# print(portList[0])
# def_port = '/dev/ttyUSB9'
# print(type(def_port))
# console.port = portList[0]
# console.open()
# print(console.isOpen())

# Init TK Design
tk = tkinter.Tk()
tk.geometry('300x450')
tk.title('LED Room Controller')

icon = PhotoImage(file= 'led-icon-25.png')
tk.iconphoto(False, icon)

# Port Selection
label_port = tkinter.Label(text='Port List : ')
label_port.pack()

avail_port = tkinter.StringVar()

combo_port = ttk.Combobox(tk, textvariable=avail_port)
combo_port['values'] = portList
combo_port['state'] = 'readonly'
combo_port.pack()

combo_port.bind('<<ComboboxSelected>>', connect)

lampStat = [0, 0, 0]
# if console.isOpen() :
# Read Lamp Stat 


status_title_label = tkinter.Label(text = 'LED Status :')
status_title_label.pack()

white_status = tkinter.IntVar()
if lampStat[0] == 0 :
    white_status.set('White: Off')
else : 
    white_status.set('White: On')
white_status_label = tkinter.Label(textvariable=white_status)
white_status_label.pack()

blue_status = tkinter.IntVar()
if lampStat[1] == 0 :
    blue_status.set('Blue: Off')
else : 
    blue_status.set('Blue: On')
blue_status_label = tkinter.Label(textvariable=blue_status)
blue_status_label.pack()

table_status = tkinter.IntVar()
if lampStat[2] == 0 :
    table_status.set('Table: Off')
else : 
    table_status.set('Table: On')
table_status_label = tkinter.Label(textvariable=table_status)
table_status_label.pack()

# Button 
button1 = tkinter.IntVar()
button1state = tkinter.Button(tk, 
    text="White", 
    command=white, 
    height=2, 
    width=5,
)
button1state.pack(side='top', ipadx=10, padx=10, pady=15)

button2 = tkinter.IntVar()
button2state = tkinter.Button(tk, 
    text = 'Blue',
    command = blue, 
    height = 2, 
    width = 5, 
)

button2state.pack (side='top', ipadx=10, padx=10, pady=15)

button3 = tkinter.IntVar()
button3state = tkinter.Button(tk, 
    text = 'Table',
    command = table, 
    height = 2, 
    width = 5, 
)

button3state.pack (side='top', ipadx=10, padx=10, pady=15)

button4 = tkinter.IntVar()
button4state = tkinter.Button(tk, 
    text = 'Sleep',
    command = sleeping, 
    height = 2, 
    width = 5, 
)

button4state.pack (side='top', ipadx=10, padx=10, pady=15)


tkinter.mainloop()