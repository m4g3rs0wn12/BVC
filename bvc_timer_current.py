import tkinter as tk
import datetime as datetime
import time
import math
import threading
from screeninfo import get_monitors, enumerators
from screeninfo.enumerators import windows

class Countdown(tk.Frame):
    def __init__(self,master):
        super().__init__(master)
        self._timer_on = False
        self.create_widgets()
        self.place_widgets()
        self.n = 0
        self.OT = 0
        self.tog = bool(False)
        top.bind('<F11>', func=self.toggle_fullscreen)

    def create_widgets(self):
#tk variables
        self.output = tk.StringVar()
        self.output.set("0:00:00")

        self.colorvar = tk.StringVar()
        self.choices = { "white", "black", "red", "green2", "blue", "cyan", "yellow", "magenta", "misty rose",}
        self.colorvar.set("green2")

        self.button_on = tk.IntVar()
        self.button_on.set(1)

        self.msg_on = tk.IntVar()
        self.msg_on.set(1)

        self.title = tk.StringVar()
        self.title.set("*title goes here")

        self.msg = tk.StringVar()
        self.msg.set("*message goes here")

        self.OTmsg = tk.StringVar()

#frame_a
        self.lb1 = tk.Label(frame_a, text="Hours:", height=1, background="black", fg="white", font="none 12 bold")
        self.lb2 = tk.Label(frame_a, text="Minutes:", height=1, background="black", fg="white", font="none 12 bold")
        self.lb3 = tk.Label(frame_a, text="Seconds:", height=1, background="black", fg="white", font="none 12 bold")
        self.lb4 = tk.Label(frame_a, text="Title:", height=1, background="black", fg="white", font="none 12 bold")
        self.lb5 = tk.Label(frame_a, text="Message:", height=1, background="black", fg="white", font="none 12 bold")
        self.bt1 = tk.Button(frame_a, width=50, image=reset_img, command=self.clear_timer)
        self.bt2 = tk.Button(frame_a, width=50, image=play_img, command=self.start_button)
        self.bt3 = tk.Button(frame_a, width=50, image=pause_img, command=self.stop_button)

##
        self.bt4 = tk.Button(frame_a, height=1, width=5, text=">>", command=self.send_to_screen2)
        self.bt5 = tk.Button(frame_a, height=1, width=5, text=">>", command=self.send_to_screen1)
##

        self.bt7 = tk.Button(frame_a, width=5, text="+1", command=self.plus_one)                      
        self.bt8 = tk.Button(frame_a, width=5, text="+5", command=self.plus_five)             
        self.bt9 = tk.Button(frame_a, width=5, text="+10", command=self.plus_ten)
        self.bt10 = tk.Button(frame_a, width=5, text="-1", command=self.minus_one)                      
        self.bt11 = tk.Button(frame_a, width=5, text="-5", command=self.minus_five)             
        self.bt12 = tk.Button(frame_a, width=5, text="-10", command=self.minus_ten)
        self.entry1 = tk.Entry(frame_a, bd=2, justify='center', relief="sunken")
        self.entry2 = tk.Entry(frame_a, bd=2, justify='center', relief="sunken")
        self.entry3 = tk.Entry(frame_a, bd=2, justify='center', relief="sunken")
        self.entry4 = tk.Entry(frame_a, bd=2, justify='center', relief="sunken")
        self.entry4.insert(0, "*title goes here")
        self.entry5 = tk.Entry(frame_a, bd=2, justify='center', relief="sunken")
        self.entry5.insert(0, "*message goes here")
        self.bt14 = tk.Button(frame_a, width=5, text="Set", command=self.set_values)

        self.bt17 = tk.Button(frame_a, text='Clear', height=1, width=5, command=self.msg_clear)
        self.bt15 = tk.Checkbutton(frame_a, height=1, width=5, text="On/Off", variable=self.msg_on, command=self.send_to_screen)
        self.bt16 = tk.Button(frame_a, height=1, width=5, text="Flash", command=self.flash_msg)

#frame b, top level window
        self.title_label = tk.Label(frame_b, textvariable=self.title)
        self.OTlb1 = tk.Label(frame_b, textvariable=self.OTmsg)
        self.lb = tk.Label(frame_b, textvariable=self.output)
        self.msg_box = tk.Label(frame_b, textvariable=self.msg)

#frame_c, preview window 
        self.title_label_dupe = tk.Label(frame_c, textvariable=self.title)
        self.OTlb_dupe = tk.Label(frame_c, textvariable=self.OTmsg)
        self.lb_dupe = tk.Label(frame_c, textvariable=self.output)
        self.msg_box_dupe = tk.Label(frame_c, textvariable=self.msg)

#frame_d, font editing
        self.dropdown = tk.OptionMenu(frame_d, self.colorvar, *self.choices)
        self.bt6 = tk.Button(frame_d, height=1, width=5, text=">>", command=self.change_color)
        self.bt13 = tk.Button(frame_d, height=1, width=5, text=">>", command=self.change_font)
        self.colorlist = tk.Label(frame_d, text="Color:")
        self.fontsize = tk.Label(frame_d, text="Font Size:")
        self.entry6 = tk.Entry(frame_d, bd=2, justify='center', relief="sunken")
        self.toggle = tk.Radiobutton(frame_d, text = "Timer", variable=self.button_on, value=1, command=self.toggle_time)
        self.toggle1 = tk.Radiobutton(frame_d, text = "Current Time", variable=self.button_on, value=0, command=self.toggle_time)
        self.lb99 = tk.Label(frame_d, text=("*F11 For" + "\n" + "Fullscreen"))
        
    def place_widgets(self):
#frame_a
        self.lb1.grid(row=0,column=0, pady=5)
        self.lb2.grid(row=1,column=0, pady=5)
        self.lb3.grid(row=2,column=0, pady=5)
        self.lb4.grid(row=6,column=0, pady=5)
        self.lb5.grid(row=7, column=0, pady=5)
        self.bt1.grid(row=3,column=0, pady=10)
        self.bt2.grid(row=3,column=1, pady=10)
        self.bt3.grid(row=3,column=2, pady=10)

##
        self.bt4.grid(row=7,column=2, padx=10, pady=5)
        self.bt5.grid(row=6,column=2,padx=10, pady=5)
##

        self.bt7.grid(row=4,column=0, pady=10)
        self.bt8.grid(row=4,column=1, pady=10)
        self.bt9.grid(row=4,column=2, pady=10)
        self.bt10.grid(row=5,column=0, pady=10)
        self.bt11.grid(row=5,column=1, pady=10)
        self.bt12.grid(row=5,column=2, pady=10)
        self.entry1.grid(row=0,column=1)
        self.entry2.grid(row=1,column=1)
        self.entry3.grid(row=2,column=1)
        self.entry4.grid(row=6, column=1)
        self.entry5.grid(row=7, column=1)
        self.bt14.config(height=1)
        self.bt14.grid(row=0,column=2, rowspan=3,padx=15, pady=5, sticky="N"+"S")
        
        self.bt15.grid(row=8,column=0, padx=10, pady=5)
        self.bt16.grid(row=8,column=2, padx=10, pady=5)
        self.bt15.configure(bg="black", fg="red")
        self.bt17.grid(row=8, column=1, padx=10, pady=5)

#frame_b, top level window
        self.title_label.configure(bg="black", fg="white", font="none 40 bold", height=3, wrap=True, wraplength=1075)
        self.title_label.grid(row=0, column=0, sticky="N")

        self.OTlb1.configure(bg="black", fg="white", font="none 45 bold")
        self.OTlb1.grid(row=0, column=0, pady=(150,0), sticky="S")

        self.lb.config(background="black", fg="red", font=("none 200 bold"))
        self.lb.grid(row=1, column=0, pady=(0,175), sticky="N")
        
        self.msg_box.configure(bg="black", fg="white", font="none 40 bold", height=3, wrap=True, wraplength=1075)
        self.msg_box.grid(row=1, column=0, pady=(25,0), sticky="S")

#frame_c, preview box
        self.title_label_dupe.grid(row=1, column=0, sticky="N"+"S")
        self.title_label_dupe.configure(bg="black", fg="white", wrap=True, wraplength=305)
        
        self.OTlb_dupe.configure(width="50", bg="black", fg="white")
        self.OTlb_dupe.grid(row=1, column=0, pady=(50,0), sticky="S")

        self.lb_dupe.grid(row=2, column=0, pady=(0,50), sticky="W"+"E"+"N"+"S")
        self.lb_dupe.configure(bg="black", fg="red", font="none 36 bold")

        self.msg_box_dupe.grid(row=2, column=0, sticky="S")
        self.msg_box_dupe.configure(bg="black", fg="white", wrap=True, wraplength=305)

#frame_d, font config
        self.dropdown.grid(row=0, column=2, padx=25)
        self.bt6.grid(row=0,column=3,padx=10, pady=5)
        self.bt13.grid(row=1, column=3, padx=10)
        
        self.colorlist.grid(row=0, column =0, padx=5)
        self.colorlist.config(bg="black", fg="white", font="none 12 bold")
        
        self.fontsize.config(bg="black", fg="white", font="none 12 bold")
        self.fontsize.grid(row=1, column=0, padx=5)
        self.font_size = tk.StringVar()
        self.font_size.set("200")
        
        self.entry6.insert(0, "200")
        self.entry6.grid(row=1, column=2, padx=25)
        self.toggle.config(bg="black", fg="red")
        self.toggle1.config(bg="black", fg="white")
        self.toggle.grid(row=2, column=2, columnspan=1, ipady=10)
        self.toggle1.grid(row=2, column=0, columnspan=1, padx=5, ipady=5)
        self.lb99.config(bg="black", fg="white")
        self.lb99.grid(row=2, column=3)

    def set_values(self):
        self._timer_on = False
        self.button_on.set(1)
        self.get_seconds()         
##        self.msg.set(self.entry5.get())
##        self.title.set(self.entry4.get())
        self.OT = 0
        self.OTmsg.set("")
        self.toggle.config(fg="red")
        self.toggle1.config(fg="white")
        if (self.n >= 300):
            self.lb.config(fg=self.colorvar.get())
            self.lb_dupe.config(fg=self.colorvar.get())
        if (self.n < 300 and self.n >= 60):
            self.lb.config(fg="gold2")
            self.lb_dupe.config(fg="gold2")
        if self.n < 60:
            self.lb.config(fg="red")
            self.lb_dupe.config(fg="red")
        self.output.set(datetime.timedelta(seconds = self.n))      
        return self.n

    def clear_timer(self):
        self.stop_button()
        self.n = 0
        self.OT = 0
        self.entry1.delete(0,tk.END)
        self.entry2.delete(0,tk.END)
        self.entry3.delete(0,tk.END)
##        self.entry4.delete(0,tk.END)
##        self.entry5.delete(0,tk.END)
##        self.msg.set("")
##        self.title.set("")
        if self.button_on.get() ==1 and self.n <= 60:
            self.lb.config(fg="red")
            self.lb_dupe.config(fg="red")
        if (self.button_on.get()) == 1:
            self.output.set("0:00:00")
            self.OTmsg.set("")
##        print (self.n, self.OT)

    def get_seconds(self):
        if(self.entry1.get() == ""):
            self.hours = 0
        else:
            self.hours = int(self.entry1.get())
            
        if(self.entry2.get() == ""):
            self.minutes = 0
        else:
            self.minutes = int(self.entry2.get())
            
        if(self.entry3.get() == ""):
            self.seconds = 0
        else:
            self.seconds = int(self.entry3.get())
            
        self.n = (self.hours * 3600) + (self.minutes * 60) + self.seconds
        return self.n

    def countdown(self, now=datetime.datetime.now):
        target = now()
        one_second_later = datetime.timedelta(seconds=1)
        sleeper = 0
        while self._timer_on == True:
            if(self.n > 0):
                if (self.n <= 300 and self.n > 60):
                    self.lb.config(fg="gold2")
                    self.lb_dupe.config(fg="gold2")
                if self.n <= 60:
                    self.lb.config(fg="red")
                    self.lb_dupe.config(fg="red")
                self.n -=1
                self.output.set(datetime.timedelta(seconds = self.n))
                target += one_second_later
                sleeper = (int((target-now()).total_seconds()*1000))
                for i in range(20):
                    root.after(int(sleeper/20))
                    self.update()

            if self.n <= 0:
                if self._timer_on == True:
                    self.output.set(datetime.timedelta(seconds = self.OT))
                    self.lb.config(fg="red")
                    self.lb_dupe.config(fg="red")
                    self.OTmsg.set("OVERTIME")
                    self.OT += 1
                    target += one_second_later
                    sleeper = (int((target-now()).total_seconds()*1000))
                    for i in range(20):
                        root.after(int(sleeper/20))
                        self.update()
                            
    def start_button(self):
        self._timer_on = True
        if (self.button_on.get()) == 1:
            self.countdown()
    
    def stop_button(self):
        self._timer_on = False

    def send_to_screen(self):
        if (self.msg_on.get()) == 1:
            self.title.set(self.entry4.get())
            self.msg.set(self.entry5.get())
        if (self.msg_on.get()) == 0:
            self.title.set("")
            self.msg.set("")

    def send_to_screen1(self):
        if (self.msg_on.get()) == 1:
            self.title.set(self.entry4.get())

    def send_to_screen2(self):
        if (self.msg_on.get()) == 1:
            self.msg.set(self.entry5.get())

    def flash_msg(self):
        self.msg_box.config(fg="red")
        self.msg_box_dupe.config(fg='red')
        self.update()
        self.after(100)
        self.msg_box.config(fg='white')
        self.msg_box_dupe.config(fg='white')
        self.update()

    def msg_clear(self):
        self.entry4.delete(0,tk.END)
        self.entry5.delete(0,tk.END)
    
    def change_color(self):
        self.x= self.colorvar.get()
        self.lb.config(background="black", fg=self.colorvar.get())
        self.lb_dupe.configure(bg="black", fg=self.colorvar.get(), font="none 36 bold")

    def plus_one(self):
        if (self.button_on.get()) == 1:
            for i in range(60):
                if self.OT > 0:
                    self.OTmsg.set("OVERTIME")
                    self.OT -=1
                    self.output.set(datetime.timedelta(seconds = self.OT))
                elif self.OT == 0:
                    self.n += 1
                    self.output.set(datetime.timedelta(seconds = self.n))
                    if (self.n >= 300):
                        self.lb.config(fg=self.colorvar.get())
                        self.lb_dupe.config(fg=self.colorvar.get())
                    if (self.n < 300 and self.n >= 60):
                        self.lb.config(fg="gold2")
                        self.lb_dupe.config(fg="gold2")
                    if self.n < 60:
                        self.lb.config(fg="red")
                        self.lb_dupe.config(fg="red")
                    self.OTmsg.set("")
##            print(self.n, self.OT)
##            return(self.n, self.OT)

    def plus_five(self):
        if (self.button_on.get()) == 1:
            for i in range(300):
                if self.OT > 0:
                    self.OTmsg.set("OVERTIME")
                    self.OT -=1
                    self.output.set(datetime.timedelta(seconds = self.OT))
                elif self.OT == 0:
                    self.n += 1
                    self.output.set(datetime.timedelta(seconds = self.n))
                    if (self.n >= 300):
                        self.lb.config(fg=self.colorvar.get())
                        self.lb_dupe.config(fg=self.colorvar.get())
                    if (self.n < 300 and self.n >= 60):
                        self.lb.config(fg="gold2")
                        self.lb_dupe.config(fg="gold2")
                    if self.n < 60:
                        self.lb.config(fg="red")
                        self.lb_dupe.config(fg="red")
                    self.OTmsg.set("")
##            print(self.n, self.OT)
##            return(self.n, self.OT)
        
    def plus_ten(self):
        if (self.button_on.get()) == 1:
            for i in range(600):
                if self.OT > 0:
                    self.OTmsg.set("OVERTIME")
                    self.OT -=1
                    self.output.set(datetime.timedelta(seconds = self.OT))
                elif self.OT == 0:
                    self.n += 1
                    self.output.set(datetime.timedelta(seconds = self.n))
                    if (self.n >= 300):
                        self.lb.config(fg=self.colorvar.get())
                        self.lb_dupe.config(fg=self.colorvar.get())
                    if (self.n < 300 and self.n >= 60):
                        self.lb.config(fg="gold2")
                        self.lb_dupe.config(fg="gold2")
                    if self.n < 60:
                        self.lb.config(fg="red")
                        self.lb_dupe.config(fg="red")
                    self.OTmsg.set("")
##            print(self.n, self.OT)
##            return(self.n, self.OT)

    def minus_one(self):
        if (self.button_on.get()) == 1:
            for i in range(60):
                if self.n > 0:
                    self.OT = 0
                    self.OTmsg.set("")
                    if (self.n >= 300):
                        self.lb.config(fg=self.colorvar.get())
                        self.lb_dupe.config(fg=self.colorvar.get())
                    if (self.n < 300 and self.n >= 60):
                        self.lb.config(fg="gold2")
                        self.lb_dupe.config(fg="gold2")
                    if self.n < 60:
                        self.lb.config(fg="red")
                        self.lb_dupe.config(fg="red")
                    self.n -=1
                    self.output.set(datetime.timedelta(seconds = self.n))
                elif self.n == 0:
                    self.OT += 1
                    self.output.set(datetime.timedelta(seconds = self.OT))
                    self.OTmsg.set("OVERTIME")
                    self.lb.config(fg="red")
                    self.lb_dupe.config(fg="red")
##            print(self.n, self.OT)
##            return(self.n, self.OT)

    def minus_five(self):
        if (self.button_on.get()) == 1:
            for i in range(300):
                if self.n > 0:
                    self.OT = 0
                    self.OTmsg.set("")
                    if (self.n >= 300):
                        self.lb.config(fg=self.colorvar.get())
                        self.lb_dupe.config(fg=self.colorvar.get())
                    if (self.n < 300 and self.n >= 60):
                        self.lb.config(fg="gold2")
                        self.lb_dupe.config(fg="gold2")
                    if self.n < 60:
                        self.lb.config(fg="red")
                        self.lb_dupe.config(fg="red")
                    self.n -=1
                    self.output.set(datetime.timedelta(seconds = self.n))
                elif self.n == 0:
                    self.OT += 1
                    self.output.set(datetime.timedelta(seconds = self.OT))
                    self.OTmsg.set("OVERTIME")
                    self.lb.config(fg="red")
                    self.lb_dupe.config(fg="red")
##            print(self.n, self.OT)
##            return(self.n, self.OT)

    def minus_ten(self):
        if (self.button_on.get()) == 1:
            for i in range(600):
                if self.n > 0:
                    self.OT = 0
                    self.OTmsg.set("")
                    if (self.n >= 300):
                        self.lb.config(fg=self.colorvar.get())
                        self.lb_dupe.config(fg=self.colorvar.get())
                    if (self.n < 300 and self.n >= 60):
                        self.lb.config(fg="gold2")
                        self.lb_dupe.config(fg="gold2")
                    if self.n < 60:
                        self.lb.config(fg="red")
                        self.lb_dupe.config(fg="red")
                    self.n -=1
                    self.output.set(datetime.timedelta(seconds = self.n))
                elif self.n == 0:
                    self.OT += 1
                    self.output.set(datetime.timedelta(seconds = self.OT))
                    self.OTmsg.set("OVERTIME")
                    self.lb.config(fg="red")
                    self.lb_dupe.config(fg="red")
##            print(self.n, self.OT)
##            return(self.n, self.OT)

    def toggle_time(self):
        self.blink = True
        while int(self.button_on.get()) == 1:
            self.toggle.config(fg="red")
            self.toggle1.config(fg="white")
            if self.n > 0:
                self.output.set(datetime.timedelta(seconds = self.n))
                self.OTmsg.set("")
            elif self.OT > 0:
                self.output.set(datetime.timedelta(seconds = self.OT))
                self.OTmsg.set("OVERTIME")
            elif self.n == 0:
                self.output.set("0:00:00")
                self.OTmsg.set("")
            self.update()
        while int(self.button_on.get()) == 0:
            self.stop_button()
            self.toggle1.config(fg="red")
            self.toggle.config(fg="white")
            self.t = time.localtime()
            self.current_time = time.strftime("%I:%M %p", self.t)
            
##            if self.blink == True:
##                self.current_time = time.strftime("%I:%M %p", self.t)
##                time.sleep(1.5)
##                self.blink = False
##            elif self.blink == False:
##                self.current_time = time.strftime("%I %M %p", self.t)
##                time.sleep(1.5)
##                self.blink = True

            self.OTmsg.set("The current time:")
            self.output.set(self.current_time)
            self.update()

    def change_font(self):
        self.font_size = str(self.entry6.get())
        self.font_config = tk.StringVar()
        self.font_config.set("none " + self.font_size + " bold")
        self.lb.config(font=self.font_config.get())

    def get_res(self):
        monitors = []
        self.num_monitors = 0
        for m in get_monitors():
            self.num_monitors += 1
            monitors.append(m.name)
            monitors.append(m.width)
            monitors.append(m.height)
        if self.num_monitors == 1:
            name_primary = str(monitors[0])
            width_primary = str(monitors[1])
            height_primary = str(monitors[2])
            self.res_primary = (width_primary + "x" + height_primary + "+0+0")
        if self.num_monitors == 2:
            name_primary = str(monitors[0])
            width_primary = str(monitors[1])
            height_primary = str(monitors[2])
            name_secondary = str(monitors[3])
            width_secondary = str(monitors[4])
            height_secondary = str(monitors[5])
            self.res_secondary = (width_secondary + "x" + height_secondary + "+" + width_primary + "+0")
        return(self.num_monitors)
        
    def buttonpress(self, event):
        if self.tog == False:
            self.tog = True
        elif self.tog == True:
            self.tog = False

    def toggle_fullscreen(self, event):
        self.get_res()
        self.buttonpress(event)
        if self.tog == True:
            if self.num_monitors == 1:
                top.overrideredirect(1)
                top.geometry(self.res_primary)
            if self.num_monitors == 2:
                top.overrideredirect(1)
                top.geometry(self.res_secondary)
        if self.tog == False:
            top.overrideredirect(0)
            top.geometry("1000x650+0+0")
 
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Config")
    root.config(bg="black")
    root.resizable(False,False)
    root.wm_iconbitmap("logo.ico")
    top = tk.Toplevel()
    top.title("Countdown")
    top.config(bg="black")

    top.geometry("1025x700")
    top.wm_iconbitmap("logo.ico")
    play_img = tk.PhotoImage(file = r"play1.ico")
    play_img.config(width=25, height=25)
    pause_img = tk.PhotoImage(file = r"pause1.ico")
    pause_img.config(width=25, height=25)
    reset_img = tk.PhotoImage(file = r"reset.ico")
    reset_img.config(width=25, height=25)

    frame_a = tk.Frame(root)
    frame_a.config(bg="black")
    frame_a.grid(row=0, column=0, pady=15, rowspan=3)

    frame_b = tk.Frame(top)
    frame_b.config(bg="black")
    frame_b.pack(expand="yes")

    frame_c = tk.Frame(root)
    frame_c.config(bg="black", bd=10, relief="raised")
    frame_c.grid(row=0, column=1, columnspan=3, rowspan=2, padx=25, ipady=20, pady=15, sticky="W"+"E"+"N"+"S")

    frame_d = tk.Frame(root)
    frame_d.config(bg="black")
    frame_d.grid(row=2, column = 1, rowspan=2, padx=25, sticky="W"+"E"+"N"+"S")

    tk.Grid.rowconfigure(top, 0, weight=1)
    tk.Grid.columnconfigure(top, 0, weight=1)

    root = Countdown(root)
    root.mainloop()
