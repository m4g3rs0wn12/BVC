import tkinter as tk
from tkinter import BOTH
import time
import datetime as datetime
import math
from screeninfo import get_monitors, enumerators
from screeninfo.enumerators import windows
import webbrowser

class Countdown(tk.Frame):
    def __init__(self,master):
        super().__init__(master)
        self._timer_on = False
        self.n = 0
        self.OT = 0
        self.tog = bool(False)

        self.top = tk.Toplevel()
        self.top.title("Countdown")
        self.top.geometry("225x70+0+0")                      
        self.top.wm_iconbitmap("logo.ico")
        self.frame_b = tk.Frame(self.top)
        self.frame_b.config(bg='black')
        self.frame_c = tk.Frame(self.top)
        self.frame_c.config(bg='black')
        self.frame_d = tk.Frame(self.top)
        self.frame_d.config(bg='black')
        self.frame_b.pack(fill=BOTH, expand=1)
        self.frame_c.pack(fill=BOTH, expand=1)
        self.frame_d.pack(fill=BOTH, expand=1)   
        self.create_widgets()
##        self.top.bind('<F11>', func=self.start_button)
        
        menubar = tk.Menu(root)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="New Countdown", command=self.reopen)
        filemenu.add_checkbutton(label="Overtime", variable=self.OT_on, command=self.toggle_ot)
        filemenu.add_checkbutton(label="Lock", variable=self.lock_on, command=self.toggle_lock)
        filemenu.add_command(label="Reset All", command=self.reset_all)
        filemenu.add_command(label="Advanced", command=self.more_options)
        filemenu.add_separator()
        filemenu.add_command(label="Help", command=lambda:webbrowser.open("README.txt"))
        filemenu.add_command(label="Quit", command=lambda:root.destroy())
        menubar.add_cascade(label="Options", menu=filemenu)
        root.config(menu=menubar)

##  more options  ##
    def more_options(self):##
        self.more_options = tk.Toplevel()
        self.frame_f = tk.Frame(self.more_options)
        self.frame_f.pack()

        self.lb11 = tk.Label(self.frame_f, text="Title Font Size:", justify='center')
        self.lb11.grid(row=0, column=0, padx=5)
        self.lb12 = tk.Label(self.frame_f, text="Countdown Font Size:", justify='center')
        self.lb12.grid(row=1, column=0, padx=5)
        self.lb13 = tk.Label(self.frame_f, text="Message Font Size:", justify='center')
        self.lb13.grid(row=2, column=0, padx=5)
        
        self.entry8 = tk.Entry(self.frame_f, bd=2, relief='sunken', width=5)
        self.entry8.grid(row=0, column=1, padx=5)
        self.entry9 = tk.Entry(self.frame_f, bd=2, relief='sunken', width=5)
        self.entry9.grid(row=1, column=1, padx=5)
        self.entry10 = tk.Entry(self.frame_f, bd=2, relief='sunken', width=5)
        self.entry10.grid(row=2, column=1, padx=5)

        font1= self.title_label.cget("font")
        font2= self.lb.cget("font")
        font3= self.msg_box.cget("font")
        self.entry8.insert(0,font1[5:8])
        self.entry9.insert(0,font2[5:8])
        self.entry10.insert(0,font3[5:8])

        self.bt23 = tk.Button(self.frame_f, text=">>", width=5, command=self.change_font4)
        self.bt23.grid(row=0, column=2, padx=(5,0))
        self.bt24 = tk.Button(self.frame_f, text=">>", width=5, command=self.change_font5)
        self.bt24.grid(row=1, column=2, padx=(5,0))
        self.bt25 = tk.Button(self.frame_f, text=">>", width=5, command=self.change_font6)
        self.bt25.grid(row=2, column=2, padx=(5,0)) 

    def toggle_lock(self):
        self.widgets = [self.bt1,self.bt2,self.bt3,self.bt4,self.bt5,self.bt6,self.bt7,self.bt8,self.bt9,self.bt10,
                        self.bt11,self.bt12, self.bt13,self.bt14,self.bt15,self.bt16,self.bt17,self.bt18,self.bt19,self.bt20,
                        self.bt21,self.bt22,self.entry1,self.entry2,self.entry3,self.entry4,self.entry5,self.entry6,self.entry7,self.toggle,self.toggle1,self.dropdown]
        if int(self.lock_on.get()) == 1:
            root.wm_iconbitmap("locked.ico")
            for x in self.widgets:
                x.config(state = 'disabled')
        if int(self.lock_on.get()) == 0:
            root.wm_iconbitmap("logo.ico")
            for x in self.widgets:
                x.config(state = 'normal')

    def reset_all(self):
        self.clear_timer()
        self.msg_clear()
        self.send_to_screen1()
        self.send_to_screen2()
        self.change_font2()
        self.colorvar.set("green2")
        
        self.entry6.delete(0, tk.END)
        self.entry6.insert(0, "5")
        
        self.entry7.delete(0, tk.END)
        self.entry7.insert(0, "1")
        
        self.lock_on.set(0)
        self.toggle_lock()
        
        self.OT_on.set(1)
        self.toggle_ot()
        
        self.msg_on.set(1)
        self.send_to_screen()
        
        self.button_on.set(1)
        self.toggle_time()
        
        self.update()

    def create_widgets(self):
#tk variables
        self.output = tk.StringVar()
        self.output.set("0:00:00")

        self.colorvar = tk.StringVar()
        self.choices = {"white", "plum2", "aquamarine", "darkorchid4", "light sea green", "black", "red", "green", "green2", "blue", "royal blue", "cyan", "yellow", "magenta", "misty rose",}
        self.colorvar.set("green2")

        self.button_on = tk.IntVar()
        self.button_on.set(1)

        self.OT_on = tk.IntVar()
        self.OT_on.set(1)

        self.lock_on = tk.IntVar()
        self.lock_on.set(0)

        self.msg_on = tk.IntVar()
        self.msg_on.set(1)

        self.title = tk.StringVar()
##        self.title.set("")

        self.msg = tk.StringVar()
##        self.msg.set("")

        self.OTmsg = tk.StringVar()

##  Config window  ##
        self.lb1 = tk.Label(frame_a, text="Hours:", height=1, background="black", fg="white", font="none 12 bold")
        self.lb2 = tk.Label(frame_a, text="Minutes:", height=1, background="black", fg="white", font="none 12 bold")
        self.lb3 = tk.Label(frame_a, text="Seconds:", height=1, background="black", fg="white", font="none 12 bold")
        self.lb4 = tk.Label(frame_a, text="Title:", height=1, background="black", fg="white", font="none 12 bold")
        self.lb5 = tk.Label(frame_a, text="Message:", height=1, background="black", fg="white", font="none 12 bold")

        self.lb1.grid(row=0,column=0, pady=5)
        self.lb2.grid(row=1,column=0, pady=5)
        self.lb3.grid(row=2,column=0, pady=5)
        self.lb4.grid(row=6,column=0, pady=5)
        self.lb5.grid(row=7, column=0, pady=5)

        self.entry1 = tk.Entry(frame_a, bd=2, justify='center', relief="sunken")
        self.entry2 = tk.Entry(frame_a, bd=2, justify='center', relief="sunken")
        self.entry3 = tk.Entry(frame_a, bd=2, justify='center', relief="sunken")
        self.entry4 = tk.Entry(frame_a, bd=2, justify='center', relief="sunken")
##        self.entry4.insert(0, "*title goes here")
        self.entry5 = tk.Entry(frame_a, bd=2, justify='center', relief="sunken")
##        self.entry5.insert(0, "*message goes here")

        self.entry1.grid(row=0,column=1)
        self.entry2.grid(row=1,column=1)
        self.entry3.grid(row=2,column=1)
        self.entry4.grid(row=6, column=1)
        self.entry5.grid(row=7, column=1)

        self.bt1 = tk.Button(frame_a, width=5, text="Set", command=self.set_values)
        self.bt2 = tk.Button(frame_a, width=50, image=reset_img, command=self.clear_timer)
        self.bt3 = tk.Button(frame_a, width=50, image=play_img, command=self.start_button)
        self.bt4 = tk.Button(frame_a, width=50, image=pause_img, command=self.stop_button)
        self.bt5 = tk.Button(frame_a, height=1, width=5, text=">>", command=self.send_to_screen1)
        self.bt6 = tk.Button(frame_a, height=1, width=5, text=">>", command=self.send_to_screen2)
        self.bt7 = tk.Button(frame_a, width=5, text="+1", command=self.plus_one)                      
        self.bt8 = tk.Button(frame_a, width=5, text="+5", command=self.plus_five)             
        self.bt9 = tk.Button(frame_a, width=5, text="+10", command=self.plus_ten)
        self.bt10 = tk.Button(frame_a, width=5, text="-1", command=self.minus_one)                      
        self.bt11 = tk.Button(frame_a, width=5, text="-5", command=self.minus_five)             
        self.bt12 = tk.Button(frame_a, width=5, text="-10", command=self.minus_ten)
        self.bt13 = tk.Button(frame_a, text="Fullscreen", command=self.toggle_fullscreen)

        self.bt14 = tk.Button(frame_a, text="1024x768", command=self.change_font1)
        self.bt15 = tk.Button(frame_a, text="1280x720", command=self.change_font2)
        self.bt16 = tk.Button(frame_a, text="1920x1080", command=self.change_font3)
        
        self.bt1.grid(row=0,column=2, rowspan=3,padx=15, pady=5, sticky="N"+"S")
        self.bt2.grid(row=3,column=0, pady=5)
        self.bt3.grid(row=3,column=1, pady=5)
        self.bt4.grid(row=3,column=2, pady=5)
        self.bt5.grid(row=6,column=2, padx=10, pady=5)
        self.bt6.grid(row=7,column=2,padx=10, pady=5)
        self.bt7.grid(row=4,column=0, pady=10)
        self.bt8.grid(row=4,column=1, pady=10)
        self.bt9.grid(row=4,column=2, pady=10)
        self.bt10.grid(row=5,column=0, pady=10)
        self.bt11.grid(row=5,column=1, pady=10)
        self.bt12.grid(row=5,column=2, pady=10)
        self.bt13.grid(row=8, column=5)

        self.bt14.grid(row=6, column=4, sticky='W')
        self.bt15.grid(row=6, column=4, sticky='E')
        self.bt16.grid(row=6, column=5, padx=(30,10))

        self.toggle = tk.Radiobutton(frame_a, text = "Timer", variable=self.button_on, value=1, command=self.toggle_time)
        self.toggle1 = tk.Radiobutton(frame_a, text = "Current Time", variable=self.button_on, value=0, command=self.toggle_time)
        self.toggle.config(bg="black", fg="red")
        self.toggle1.config(bg="black", fg="white")
        self.toggle.grid(row=8, column=3, columnspan=1, sticky="W"+"E"+"N"+"S")
        self.toggle1.grid(row=8, column=4, columnspan=1, sticky="W"+"E"+"N"+"S")

        self.colorlist = tk.Label(frame_a, text="Color:")
        self.dropdown = tk.OptionMenu(frame_a, self.colorvar, *self.choices)
        self.bt17 = tk.Button(frame_a, height=0, width=5, text=">>", command=self.change_color)

        self.colorlist.grid(row=5, column =3, padx=5)
        self.colorlist.config(bg="black", fg="white", font="none 12 bold")
        self.dropdown.grid(row=5, column=4, ipadx=20)
        self.dropdown.config(height=1, bd=2, relief='raised')
        self.bt17.grid(row=5,column=5,padx=10, pady=5)

        self.bt18 = tk.Checkbutton(frame_a, height=1, width=5, text="On/Off", variable=self.msg_on, command=self.send_to_screen)
        self.bt19 = tk.Button(frame_a, text='Clear', height=1, width=5, command=self.msg_clear)
        self.bt20 = tk.Button(frame_a, height=1, width=5, text="Flash", command=self.flash_msg)

        self.bt18.grid(row=8,column=0, padx=10, pady=5)
        self.bt18.configure(bg="black", fg="red")
        self.bt19.grid(row=8,column=1, padx=10, pady=5)
        self.bt20.grid(row=8, column=2, padx=10, pady=5)

        self.lb6 = tk.Label(frame_a, text='Resolution: ')
        self.lb6.config(bg='black', fg='white', font='none 12 bold')
        self.lb6.grid(row=6, column=3)

        self.lb7 = tk.Label(frame_a, text='First warning:     ')
        self.lb7.config(bg='black', fg='white', font='none 12 bold')
        self.lb7.grid(row=7, column=3)

        self.entry6 = tk.Entry(frame_a, bd=2, width=2, justify='center', relief="sunken")
        self.entry6.grid(row=7, column=3, sticky='E')
        self.entry6.insert(0, "5")

        self.lb8 = tk.Label(frame_a, text='Second warning:     ')
        self.lb8.config(bg='black', fg='white', font='none 12 bold')
        self.lb8.grid(row=7, column=4)

        self.entry7 = tk.Entry(frame_a, bd=2, width=2, justify='center', relief="sunken")
        self.entry7.grid(row=7, column=4, sticky='E')
        self.entry7.insert(0, "1")

        self.lb9 = tk.Label(frame_a, text='(minutes)')
        self.lb9.config(bg='black', fg='white', font='none 12 bold')
        self.lb9.grid(row=7, column=5)

        self.bt21 = tk.Button(frame_a, height=1, width=50, text="Re-open", command=self.reopen)
##        self.bt21.grid(row=10, column=0, columnspan=8, pady=15)
        
        self.lb9 = tk.Label(frame_a, text='Copyright © 2019 Boitnott Visual Communications. All rights reserved.', anchor='w')
        self.lb9.config(font='none 8 normal', width=117)
        self.lb9.grid(row=11, column=0, columnspan=8, padx=1)

        self.lb10 = tk.Label(frame_a, text='https://boitnottvisual.com/', anchor='e')
        self.lb10.config(font='none 8 normal')
        self.lb10.grid(row=11, column=5)

        self.bt22 = tk.Checkbutton(frame_a, height=1, width=5, text="Overtime", variable=self.OT_on, command=self.toggle_ot)
        self.bt22.configure(bg="black", fg="red")
##        self.bt22.grid(row=8, column=5, ipadx=25)

## Preview window  ##
        self.preview_title = tk.Text(frame_e)
        self.preview_OT = tk.Label(frame_e, textvariable=self.OTmsg)
        self.preview_output = tk.Label(frame_e, textvariable=self.output)
        self.preview_msg = tk.Text(frame_e)

        self.preview_title.pack(fill='x', expand=1)
        self.preview_title.configure(bd=0, width=42, bg="black", fg="white", font="none 12 normal", height=2, wrap='word')

        self.preview_OT.pack(fill=BOTH, expand=1, anchor='s')
        self.preview_OT.configure(bg="black", fg="red", font='none 12 normal', height=1)
        
        self.preview_output.pack(fill=BOTH, expand=1, anchor='center')
        self.preview_output.configure(bg="black", fg="red", font="none 36 bold")

        self.preview_msg.pack(fill='x', expand=1, anchor='s')
        self.preview_msg.configure(bd=0, width=42, bg="black", fg="yellow", font="none 12 normal", height=3, wrap='word')  ####

##  Top level window  ##
        self.title_label = tk.Text(self.frame_b)
        self.title_label.configure(height=2, bd=0, bg="black", fg="white", font="none 40 normal", wrap='word')
        self.title_label.pack(fill='x', expand=1, anchor='s')

        self.OTlb = tk.Label(self.frame_b, textvariable=self.OTmsg)
        self.OTlb.configure(bg="black", fg="red", font="none 35 bold", height=1)
        self.OTlb.pack(fill='x', expand=1, anchor='s')

        self.lb = tk.Label(self.frame_c, textvariable=self.output)
        self.lb.pack(fill=BOTH, expand=1, anchor='center')
        self.lb.configure(bg="black", fg="red", font="none 215 bold")

        self.msg_box = tk.Text(self.frame_d)
        self.msg_box.pack(fill='x', expand=1, anchor='s')
        self.msg_box.configure(height=3, bd=0, bg="black", fg="yellow", font="none 40 normal", wrap='word')
        
##  Functions  ##
    def reopen(self):
        self.top.destroy()
        self.top = tk.Toplevel()
        self.top.title("Countdown")
        self.top.geometry("225x70+0+0")                     
        self.top.wm_iconbitmap("logo.ico")
        self.frame_b = tk.Frame(self.top)
        self.frame_b.config(bg='black')
        self.frame_c = tk.Frame(self.top)
        self.frame_c.config(bg='black')
        self.frame_d = tk.Frame(self.top)
        self.frame_d.config(bg='black')
        self.frame_b.pack(fill=BOTH, expand=1)
        self.frame_c.pack(fill=BOTH, expand=1)
        self.frame_d.pack(fill=BOTH, expand=1)

        self.title_label = tk.Text(self.frame_b)
        self.title_label.configure(height=2, bd=0, bg="black", fg="white", font="none 40 normal", wrap='word')
        self.title_label.pack(fill='x', expand=1, anchor='s')

        self.OTlb = tk.Label(self.frame_b, textvariable=self.OTmsg)
        self.OTlb.configure(bg="black", fg="red", font="none 35 bold", height=1)
        self.OTlb.pack(fill='x', expand=1, anchor='s')

        self.lb = tk.Label(self.frame_c, textvariable=self.output)
        self.lb.pack(fill=BOTH, expand=1, anchor='center')
        self.lb.configure(bg="black", fg="red", font="none 215 bold")

        self.msg_box = tk.Text(self.frame_d)
        self.msg_box.pack(fill='x', expand=1, anchor='s')
        self.msg_box.configure(height=3, bd=0, bg="black", fg="white", font="none 40 normal", wrap='word')

    def set_values(self):
        self._timer_on = False
        self.button_on.set(1)
        self.get_seconds()         
        self.OT = 0
        self.OTmsg.set("")
        self.toggle.config(fg="red")
        self.toggle1.config(fg="white")
        if (self.n >= ((int(self.entry6.get()))*60)):
            self.lb.config(fg=self.colorvar.get())
            self.preview_output.config(fg=self.colorvar.get())
        if (self.n <= ((int(self.entry6.get()))*60) and self.n > ((int(self.entry7.get()))*60)):
            self.lb.config(fg="gold2")
            self.preview_output.config(fg="gold2")
        if self.n < ((int(self.entry7.get()))*60):
            self.lb.config(fg="red")
            self.preview_output.config(fg="red")
        self.output.set(datetime.timedelta(seconds = self.n))      
        return self.n
    
    def clear_timer(self):
        self.stop_button()
        self.n = 0
        self.OT = 0
        self.update
        self.entry1.delete(0,tk.END)
        self.entry2.delete(0,tk.END)
        self.entry3.delete(0,tk.END)
        if self.button_on.get() ==1:
            try:
                self.lb.config(fg="red")
            except:
                pass
            self.preview_output.config(fg="red")
            self.output.set("0:00:00")
            self.OTmsg.set("")
    
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
                if self.n > ((int(self.entry6.get()))*60):
                    try:
                        self.lb.config(fg=self.colorvar.get())
                    except:
                        pass
                    self.preview_output.config(fg=self.colorvar.get())
                if (self.n <= ((int(self.entry6.get()))*60) and self.n > ((int(self.entry7.get()))*60)):
                    try:
                        self.lb.config(fg="gold2")
                    except:
                        pass
                    self.preview_output.config(fg="gold2")
                if self.n <= ((int(self.entry7.get()))*60):
                    try:
                        self.lb.config(fg="red")
                    except:
                        pass
                    self.preview_output.config(fg="red")
                self.n -=1
                if self.button_on.get() == 1:
                    self.output.set(datetime.timedelta(seconds = self.n))
                target += one_second_later
                sleeper = (int((target-now()).total_seconds()*1000))
                for i in range(20):
                    root.after(int(sleeper/20))
                    self.update()
            if self.n == 0 and self.OT_on.get() == 0:
                self.stop_button()
                for i in range(4):
                    try:
                        self.lb.config(fg="black")
                    except:
                        pass
                    self.preview_output.config(fg="black")
                    self.update()
                    root.after(150)
                    try:
                        self.lb.config(fg="red")
                    except:
                        pass
                    self.preview_output.config(fg="red")
                    self.update()
                    root.after(150)
                return
            else:
                if self.n <= 0:
                    if self._timer_on == True:
                        if self.button_on.get() == 1:
                            self.output.set(datetime.timedelta(seconds = self.OT))
                            try:
                                self.lb.config(fg="red")
                            except:
                                pass
                            self.preview_output.config(fg="red")
                            self.OTmsg.set("OVERTIME")
                        self.OT += 1
                        target += one_second_later
                        sleeper = (int((target-now()).total_seconds()*1000))
                        for i in range(20):
                            root.after(int(sleeper/20))
                            self.update()

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
                    if (self.n >= ((int(self.entry6.get()))*60)):
                        try:
                            self.lb.config(fg=self.colorvar.get())
                        except:
                            pass
                        self.preview_output.config(fg=self.colorvar.get())
                    if (self.n < ((int(self.entry6.get()))*60) and self.n >= ((int(self.entry7.get()))*60)):
                        try:
                            self.lb.config(fg="gold2")
                        except:
                            pass
                        self.preview_output.config(fg="gold2")
                    if self.n < ((int(self.entry7.get()))*60):
                        try:
                            self.lb.config(fg="red")
                        except:
                            pass
                        self.preview_output.config(fg="red")
                    self.OTmsg.set("")

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
                    if (self.n >= ((int(self.entry6.get()))*60)):
                        try:
                            self.lb.config(fg=self.colorvar.get())
                        except:
                            pass
                        self.preview_output.config(fg=self.colorvar.get())
                    if (self.n < ((int(self.entry6.get()))*60) and self.n >= ((int(self.entry7.get()))*60)):
                        try:
                            self.lb.config(fg="gold2")
                        except:
                            pass
                        self.preview_output.config(fg="gold2")
                    if self.n < ((int(self.entry7.get()))*60):
                        try:
                            self.lb.config(fg="red")
                        except:
                            pass
                        self.preview_output.config(fg="red")
                    self.OTmsg.set("")
        
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
                    if (self.n >= ((int(self.entry6.get()))*60)):
                        try:
                            self.lb.config(fg=self.colorvar.get())
                        except:
                            pass
                        self.preview_output.config(fg=self.colorvar.get())
                    if (self.n < ((int(self.entry6.get()))*60) and self.n >= ((int(self.entry7.get()))*60)):
                        try:
                            self.lb.config(fg="gold2")
                        except:
                            pass
                        self.preview_output.config(fg="gold2")
                    if self.n < ((int(self.entry7.get()))*60):
                        try:
                            self.lb.config(fg="red")
                        except:
                            pass
                        self.preview_output.config(fg="red")
                    self.OTmsg.set("")

    def minus_one(self):
        if (self.button_on.get()) == 1:
            for i in range(60):
                if self.n > 0:
                    self.OT = 0
                    self.OTmsg.set("")
                    if (self.n >= ((int(self.entry6.get()))*60)):
                        try:
                            self.lb.config(fg=self.colorvar.get())
                        except:
                            pass
                        self.preview_output.config(fg=self.colorvar.get())
                    if (self.n < ((int(self.entry6.get()))*60) and self.n >= ((int(self.entry7.get()))*60)):
                        try:
                            self.lb.config(fg="gold2")
                        except:
                            pass
                        self.preview_output.config(fg="gold2")
                    if self.n < ((int(self.entry7.get()))*60):
                        try:
                            self.lb.config(fg="red")
                        except:
                            pass
                        self.preview_output.config(fg="red")
                    self.n -=1
                    self.output.set(datetime.timedelta(seconds = self.n))
                elif self.n == 0:
                    if self.OT_on.get() == 0:
                        return
                    self.OT += 1
                    self.output.set(datetime.timedelta(seconds = self.OT))
                    self.OTmsg.set("OVERTIME")
                    try:
                        self.lb.config(fg="red")
                    except:
                        pass
                    self.preview_output.config(fg="red")

    def minus_five(self):
        if (self.button_on.get()) == 1:
            for i in range(300):
                if self.n > 0:
                    self.OT = 0
                    self.OTmsg.set("")
                    if (self.n >= ((int(self.entry6.get()))*60)):
                        try:
                            self.lb.config(fg=self.colorvar.get())
                        except:
                            pass
                        self.preview_output.config(fg=self.colorvar.get())
                    if (self.n < ((int(self.entry6.get()))*60) and self.n >= ((int(self.entry7.get()))*60)):
                        try:
                            self.lb.config(fg="gold2")
                        except:
                            pass
                        self.preview_output.config(fg="gold2")
                    if self.n < ((int(self.entry7.get()))*60):
                        try:
                            self.lb.config(fg="red")
                        except:
                            pass
                        self.preview_output.config(fg="red")
                    self.n -=1
                    self.output.set(datetime.timedelta(seconds = self.n))
                elif self.n == 0:
                    if self.OT_on.get() == 0:
                        return
                    self.OT += 1
                    self.output.set(datetime.timedelta(seconds = self.OT))
                    self.OTmsg.set("OVERTIME")
                    try:
                        self.lb.config(fg="red")
                    except:
                        pass
                    self.preview_output.config(fg="red")

    def minus_ten(self):
        if (self.button_on.get()) == 1:
            for i in range(600):
                if self.n > 0:
                    self.OT = 0
                    self.OTmsg.set("")
                    if (self.n >= ((int(self.entry6.get()))*60)):
                        try:
                            self.lb.config(fg=self.colorvar.get())
                        except:
                            pass
                        self.preview_output.config(fg=self.colorvar.get())
                    if (self.n < ((int(self.entry6.get()))*60) and self.n >= ((int(self.entry7.get()))*60)):
                        try:
                            self.lb.config(fg="gold2")
                        except:
                            pass
                        self.preview_output.config(fg="gold2")
                    if self.n < ((int(self.entry7.get()))*60):
                        try:
                            self.lb.config(fg="red")
                        except:
                            pass
                        self.preview_output.config(fg="red")
                    self.n -=1
                    self.output.set(datetime.timedelta(seconds = self.n))
                elif self.n == 0:
                    if self.OT_on.get() == 0:
                        return
                    self.OT += 1
                    self.output.set(datetime.timedelta(seconds = self.OT))
                    self.OTmsg.set("OVERTIME")
                    try:
                        self.lb.config(fg="red")
                    except:
                        pass
                    self.preview_output.config(fg="red")
                            
    def start_button(self):
        self._timer_on = True
        if (self.button_on.get()) == 1:
            self.countdown()
    
    def stop_button(self):
        self._timer_on = False

    def send_to_screen(self):
        if (self.msg_on.get()) == 1:
            self.preview_title.configure(state='normal')
            self.preview_title.delete(0.0, tk.END)
            self.preview_title.insert(0.0, self.entry4.get(), "center")
            self.preview_title.tag_configure("center", justify='center')
            self.preview_title.configure(state='disabled')

            try:
                self.title_label.configure(state='normal')
                self.title_label.delete(0.0, tk.END)
                self.title_label.insert(0.0, self.entry4.get(), "center")
                self.title_label.tag_configure("center", justify='center')
                self.title_label.configure(state='disabled')
            except:
                pass

            self.preview_msg.configure(state='normal')
            self.preview_msg.delete(0.0, tk.END)
            self.preview_msg.insert(0.0, self.entry5.get(), "center")
            self.preview_msg.tag_configure("center", justify='center')
            self.preview_msg.configure(state='disabled')

            try:
                self.msg_box.configure(state='normal')
                self.msg_box.delete(0.0, tk.END)
                self.msg_box.insert(0.0, self.entry5.get(), "center")
                self.msg_box.tag_configure("center", justify='center')
                self.msg_box.configure(state='disabled')
            except:
                pass
            
            root.update()
            self.top.update()

        if (self.msg_on.get()) == 0:
            self.preview_title.configure(state='normal')
            self.preview_title.delete(0.0, tk.END)
            self.preview_title.configure(state='disabled')

            try:
                self.title_label.configure(state='normal')
                self.title_label.delete(0.0, tk.END)
                self.title_label.configure(state='disabled')
            except:
                pass
            
            self.preview_msg.configure(state='normal')
            self.preview_msg.delete(0.0, tk.END)
            self.preview_msg.configure(state='disabled')

            try:
                self.msg_box.configure(state='normal')
                self.msg_box.delete(0.0, tk.END)
                self.msg_box.configure(state='disabled')
            except:
                pass
            
            root.update()
            self.top.update()

    def send_to_screen1(self):
        if (self.msg_on.get()) == 1:
            self.preview_title.configure(state='normal')
            self.preview_title.delete(0.0, tk.END)
            self.preview_title.insert(0.0, self.entry4.get(), "center")
            self.preview_title.tag_configure("center", justify='center')
            self.preview_title.configure(state='disabled')

            try:
                self.title_label.configure(state='normal')
                self.title_label.delete(0.0, tk.END)
                self.title_label.insert(0.0, self.entry4.get(), "center")
                self.title_label.tag_configure("center", justify='center')
                self.title_label.configure(state='disabled')
            except:
                pass

    def send_to_screen2(self):
        if (self.msg_on.get()) == 1:
            self.preview_msg.configure(state='normal')
            self.preview_msg.delete(0.0, tk.END)
            self.preview_msg.insert(0.0, self.entry5.get(), "center")
            self.preview_msg.tag_configure("center", justify='center')
            self.preview_msg.configure(state='disabled')

            try:
                self.msg_box.configure(state='normal')
                self.msg_box.delete(0.0, tk.END)
                self.msg_box.insert(0.0, self.entry5.get(), "center")
                self.msg_box.tag_configure("center", justify='center')
                self.msg_box.configure(state='disabled')
            except:
                pass

    def flash_msg(self):
##        for i in range(3):
        try:
            self.msg_box.config(fg='black')  #self.lb.cget('fg'))
        except:
            pass
        self.preview_msg.config(fg='black')  #self.lb.cget('fg'))
        self.update()
        self.after(150)
        try:
            self.msg_box.config(fg='yellow')
        except:
            pass
        self.preview_msg.config(fg='yellow')
        self.update()
        self.after(150)
    
    def msg_clear(self):
        self.entry4.delete(0,tk.END)
        self.entry5.delete(0,tk.END)
        self.send_to_screen1()
        self.send_to_screen2()
    
    def change_color(self):
        try:
            self.lb.config(background="black", fg=self.colorvar.get())
        except:
            pass
        self.preview_output.configure(bg="black", fg=self.colorvar.get())

    def toggle_time(self):
        if int(self.button_on.get()) == 1:
            self.toggle.config(fg="red")
            self.toggle1.config(fg="white")
            try:
                self.OTlb.configure(bg="black", fg="red")
            except:
                pass
            self.preview_OT.configure(bg="black", fg="red")
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
        if int(self.button_on.get()) == 0:
            while int(self.button_on.get()) == 0:
                self.toggle1.config(fg="red")
                self.toggle.config(fg="white")
                self.t = time.localtime()
                self.current_time = time.strftime("%I:%M %p", self.t)
                self.OTmsg.set("The current time:")
                try:
                    self.OTlb.configure(bg="black", fg="white")
                except:
                    pass
                self.preview_OT.configure(bg="black", fg="white")
                self.output.set(self.current_time)
                self.update()

    def toggle_ot(self):
        if int(self.OT_on.get()) == 1:
            self.bt22.configure(bg="black", fg="red")
            
        if int(self.OT_on.get()) == 0:
            self.bt22.configure(bg="black", fg="white")
            if self.n <= 0:
                self.stop_button()
                self.clear_timer()
    
    def change_font1(self):
##  1024x768  ##
        self.title_label.configure(font='none 35 normal')
        self.OTlb.configure(font='none 35 bold')
        self.lb.configure(font='none 175 bold')
        self.msg_box.configure(font='none 35 normal')

        self.preview_title.configure(width=38)
        self.preview_msg.configure(width=38)
        root.update()
        self.top.update()

    def change_font2(self):
##  1280x720  ##
        self.title_label.configure(font='none 40 normal')
        self.OTlb.configure(font='none 35 bold')
        self.lb.configure(font='none 215 bold')
        self.msg_box.configure(font='none 40 normal')

        self.preview_title.configure(width=42)
        self.preview_msg.configure(width=42)
        root.update()
        self.top.update()

    def change_font3(self):
##  1920x1080  ##
        self.title_label.configure(font='none 69 normal')
        self.OTlb.configure(font='none 50 bold')
        self.lb.configure(font='none 315 bold')
        self.msg_box.configure(font='none 69 normal')

        self.preview_title.configure(width=36)
        self.preview_msg.configure(width=36)
        root.update()
        self.top.update()

    def change_font4(self):
        self.temp1 = int(self.entry8.get())
        self.title_label.configure(font="none " + str(self.temp1) + " normal")

    def change_font5(self):
        self.temp2 = int(self.entry9.get())
        self.lb.configure(font="none " + str(self.temp2) + " bold")
        
    def change_font6(self):
        self.temp3 = int(self.entry10.get())
        self.msg_box.configure(font="none " + str(self.temp3) + " normal")      
    
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
        
    def buttonpress(self):
        if self.tog == False:
            self.tog = True
        elif self.tog == True:
            self.tog = False

    def toggle_fullscreen(self):
        self.get_res()
        self.buttonpress()
        if self.tog == True:
            if self.num_monitors == 1:
                self.top.overrideredirect(1)
                self.top.geometry(self.res_primary)
                    
            if self.num_monitors == 2:
                self.top.overrideredirect(1)
                self.top.geometry(self.res_secondary)
                    
        if self.tog == False:
            self.top.overrideredirect(0)
            self.top.geometry("225x70+0+0")                     ##
##                self.top.geometry("1000x650+0+0")


##  config  ##
root = tk.Tk()
play_img = tk.PhotoImage(file = r"play1.ico")
play_img.config(width=25, height=25)
pause_img = tk.PhotoImage(file = r"pause1.ico")
pause_img.config(width=25, height=25)
reset_img = tk.PhotoImage(file = r"reset.ico")
reset_img.config(width=25, height=25)

root.title("Config")
root.geometry('+50+75')
##root.geometry('500x250')
root.resizable(False, False)
root.wm_iconbitmap("logo.ico")
frame_a = tk.Frame(root)
frame_a.config(bg='black')
frame_e = tk.Frame(frame_a)
frame_e.config(bg='black', bd=10, relief="raised")
frame_a.pack(fill=BOTH, expand=1)
frame_e.grid(row=0, column=3, columnspan=3, rowspan=5, pady=10)
countdown = Countdown(root)
root.mainloop()

