import tkinter as tk
from tkinter import ttk
from tkinter import * 
import Ultrasonic_sensor
import ReadXMLFileData
import time


US = Ultrasonic_sensor.Run
ReadXMLdat = ReadXMLFileData.DataRead

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
progessBarOne_style.configure('progessBarOne.Horizontal.TProgressbar', foreground='#FFFFFF', background='#000000')


# This is the section of code which creates a progress bar
progessBarOne=ttk.Progressbar(root, style='progessBarOne.Horizontal.TProgressbar', orient='horizontal', length=540, mode='determinate', maximum=ReadXMLdat.findvalue("TankReadingValue.xml", "tankreadings", "High"), value=1)
progessBarOne.place(x=72, y=328)


# This is the section of code which creates the a label
Label(root, text='Tank Level', bg='#F0F8FF', font=('arial', 12, 'normal')).place(x=289, y=289)

time1 = ''
#temp = Label(root, text='Label no.1', font=('times', 20, 'bold'), bg='orange')
#temperaturelabel = Label(root, text='Label no.2', font=('times', 20, 'bold'), bg='light blue')
#temperaturelabel.pack(fill=BOTH, expand=1)
#temp.pack(fill=BOTH, expand=1)
def percentage(part, whole):
  percentage = 100 * float(part)/float(whole)
  return str(percentage) + "%"



def tick():
    readingval = ""
    
    
    global time1
    # get the current local time from the PC
    time2 = time.strftime('%S')
    # if time string has changed, update it
    if time2 != time1:
        time1 = time2
        #--------------------------- Reading and writting of temperature code
        tankupdate(round(US.distance(12, 18), 1))
        print(round(US.distance(12, 18), 1))
        #print(int(temperature))
        time.sleep(3)
        
    # calls itself every 200 milliseconds
    # to update the time display as needed
    # could use >200 ms, but display gets jerky
    progessBarOne.after(200, tick)
    
    if percentage(round(US.distance(12, 18), 1), ReadXMLdat.findvalue("TankReadingValue.xml", "tankreadings", "High")) > 10:
        print("filled")
    else if percentage(round(US.distance(12, 18), 1), ReadXMLdat.findvalue("TankReadingValue.xml", "tankreadings", "High")) > 50:
        print("half done")
    else if percentage(round(US.distance(12, 18), 1), ReadXMLdat.findvalue("TankReadingValue.xml", "tankreadings", "High")) > 90:
        print("lightly filled :(")
    
tick()
#tankupdate(US.distance(18, 24))
#print(US.distance(18, 24))
root.mainloop()