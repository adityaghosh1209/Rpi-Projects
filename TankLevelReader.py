import tkinter as tk
from tkinter import ttk
from tkinter import * 
import Ultrasonic_sensor


US = Ultrasonic_sensor.Run


# This is a function which increases the progress bar value by the given increment amount
def makeProgress():
	progessBarOne['value']=progessBarOne['value'] + 1
	root.update_idletasks()

# This is a function which increases the progress bar value by the given increment amount
def tankupdate(Value):
	progessBarOne['value']= Value 
	root.update_idletasks()



root = Tk()

# This is the section of code which creates the main window
root.geometry('691x480')
root.configure(background='#F0F8FF')
root.title('Tank Level Reader')


# This is the section of code which creates a color style to be used with the progress bar
progessBarOne_style = ttk.Style()
progessBarOne_style.theme_use('clam')
progessBarOne_style.configure('progessBarOne.Horizontal.TProgressbar', foreground='#838B8B', background='#838B8B')


# This is the section of code which creates a progress bar
progessBarOne=ttk.Progressbar(root, style='progessBarOne.Horizontal.TProgressbar', orient='horizontal', length=540, mode='determinate', maximum=100, value=1)
progessBarOne.place(x=72, y=328)


# This is the section of code which creates the a label
Label(root, text='Tank Level', bg='#F0F8FF', font=('arial', 12, 'normal')).place(x=289, y=289)



root.mainloop()
while True:
    tankupdate(US.distance(18, 24))