#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 22 12:39:57 2021

@author: macbook
"""

from tkinter import *
from PIL import ImageTk, Image
from datetime import datetime
import pytz
import time
root=Tk()
root.geometry("700x900")

india_image= ImageTk.PhotoImage(Image.open ("clock.jpg"))
usa_image= ImageTk.PhotoImage(Image.open ("clock.jpg"))
australia_image= ImageTk.PhotoImage(Image.open ("clock.jpg"))
japan_image= ImageTk.PhotoImage(Image.open ("clock.jpg"))
#-----------------India-----------------
india_label = Label(root,text="India")
india_label.place(relx=0.25,rely=0.02, anchor= CENTER)
india_map=Label(root)
india_map["image"]=india_image
india_map.place(relx=0.25,rely=0.21, anchor= CENTER)

india_time = Label(root)
india_time.place(relx=0.25,rely=0.4, anchor= CENTER)
#-----------------------US---------------
usa_label = Label(root,text="USA")
usa_label.place(relx=0.75,rely=0.02,anchor= CENTER)
usa_map=Label(root)
usa_map["image"]=usa_image
usa_map.place(relx=0.75,rely=0.21, anchor= CENTER)

usa_time = Label(root)
usa_time.place(relx=0.75,rely=0.4, anchor= CENTER)
#-----------------------Australia---------------
australia_label = Label(root,text="Australia")
australia_label.place(relx=0.25,rely=0.5,anchor= CENTER)
australia_map=Label(root)
australia_map["image"]=australia_image
australia_map.place(relx=0.25,rely=0.69, anchor= CENTER)

australia_time = Label(root)
australia_time.place(relx=0.25,rely=0.88, anchor= CENTER)
#-----------------------Japan---------------
japan_label = Label(root,text="Japan")
japan_label.place(relx=0.75,rely=0.5,anchor= CENTER)
japan_clock=Label(root)
japan_clock["image"]=japan_image
japan_clock.place(relx=0.75,rely=0.69, anchor= CENTER)

japan_time = Label(root)
japan_time.place(relx=0.75,rely=0.88, anchor= CENTER)
class India():
    def times(self):
        home=pytz.timezone('Asia/Kolkata')
        local_time=datetime.now(home)
        current_time=local_time.strftime("%H:%M:%S")
        india_time["text"]="Time :"+ current_time
        india_time.after(200,self.times)
class USA():
    def times(self):
        home=pytz.timezone('US/Central')
        local_time=datetime.now(home)
        current_time=local_time.strftime("%H:%M:%S")
        usa_time["text"]="Time :"+ current_time
        usa_time.after(200,self.times)  
class Australia():
    def times(self):
        home=pytz.timezone('Australia/ACT')
        local_time=datetime.now(home)
        current_time=local_time.strftime("%H:%M:%S")
        australia_time["text"]="Time :"+ current_time
        australia_time.after(200,self.times)
class Japan():
    def times(self):
        home=pytz.timezone('Japan')
        local_time=datetime.now(home)
        current_time=local_time.strftime("%H:%M:%S")
        japan_time["text"]="Time : "+ current_time
        japan_time.after(200,self.times)
obj_india=India()
obj_usa=USA()
obj_australia=Australia()
obj_japan=Japan()
india_btn=Button(root,text="Show Time",command=obj_india.times)
india_btn.place(relx=0.25,rely=0.44, anchor= CENTER)
usa_btn=Button(root,text="Show Time",command=obj_usa.times)
usa_btn.place(relx=0.75,rely=0.44, anchor= CENTER)
australia_btn=Button(root,text="Show Time",command=obj_australia.times)
australia_btn.place(relx=0.25,rely=0.92, anchor= CENTER)
japan_btn=Button(root,text="Show Time",command=obj_japan.times)
japan_btn.place(relx=0.75,rely=0.92, anchor= CENTER)
root.mainloop()