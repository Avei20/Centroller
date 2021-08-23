import serial 
import tkinter
import time 

def quit_btn () : 
    # global tkTop
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

def ganti_port (port, new_port) : 
    port = new_port

port = 'COM4'

tkTop = tkinter.Tk()
tkTop.geometry('300x450')
tkTop.title('LED Controller Avei')

# com_label = tkinter.Label(text = 'Port berapa (default COM3)')
# com_label.pack()

# com_input =tkinter.Entry()
# com_input.insert(-1, 'COM3')
# com_input.pack()

# button0 = tkinter.IntVar()
# button0state = tkinter.Button(tkTop, 
#     text = 'Restart Serial', 
#     command = ganti_port(port, com_input.get()),
#     height = 2, 
#     width = 8,
# )
# button0state.pack(side='top', ipadx=10, padx=10, pady=15)

ser = serial.Serial(port , 9600)

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
