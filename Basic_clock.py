###---             A basic python3 clock                  ---###
###---           using Tkinter for the gui                ---###
###---    using threading as a non blocking timer         ---###
###---                                                    ---###

from tkinter import * 
import threading
import time

global current_time

def get_time():
    global current_time
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    
def time_update():
    global current_time
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    Label(root, text=str(current_time), bg='#000000', font=('arial', 35, 'normal')).place(x=17, y=13)
    trigger_time()

def trigger_time():
    timer = threading.Timer(1.0, time_update)
    timer.start()

## non blocking thread
t = threading.Thread(target=trigger_time)
t.setDaemon(True)
t.start()

root = Tk()

Label(root, text=str('  upating     '), background='#000000', font=('arial', 12, 'normal')).place(x=17, y=23)

root.geometry('180x70'), root.configure(background='#000000', ), root.title('Basic Clock')
root.geometry("+0+0"), root.resizable(width=False, height=False)
root.mainloop()
