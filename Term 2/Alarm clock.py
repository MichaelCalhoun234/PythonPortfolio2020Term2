import time
import calendar
from tkinter import*
from tkinter import ttk
from tkinter import font
    
def current_time():
    
    totalSeconds = calendar.timegm(time.gmtime())
    currentSecond = totalSeconds%60
    if currentSecond < 10:
       currentSecond ="0"+str(currentSecond)

    totalMinutes = totalSeconds//60
    currentMinute = totalMinutes%60
    if currentMinute < 10:
       currentMinute ="0"+str(currentMinute)

    totalHours = totalMinutes//60
    currentHour = (totalHours%24)-6
    
   

    am_pm = ""
    if currentHour>=12:
        am_pm = "PM"
    if currentHour==0:
        currentHour= currentHour+12
    else:
        am_pm = "AM"
        if currentHour==0:
            currentHour= currentHour+12

    timex= str(currentHour)+":"+str(currentMinute)+":"+str(currentSecond)+" "+am_pm
    return timex
def show_time():
    time = current_time()
    txt.set(time)
    root.after(1000, show_time)
    
root = Tk()
#set window size
root.geometry("500x200")

#set up font
root.after(1000, show_time)
fnt= font.Font(family='Times New Roman', size=60, weight ='bold')
txt = StringVar()


#display time and set up the colors of text & background
root.title("Clock")
root.configure(background='Black')
lbl=ttk.Label(root, textvariable=txt, font=fnt, foreground="Red",background='Black')
#place the time in the center of the screen
lbl.place(relx=0.5, rely=0.5, anchor = CENTER)

#start main loop
root.mainloop()
