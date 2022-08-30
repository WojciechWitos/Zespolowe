import tkinter as tk           
from tkinter import ANCHOR, CENTER, RIGHT, LEFT, BOTH, END, Entry, Listbox, Scrollbar, font as tkfont
import os
import urllib, json
from click import command
from numpy import pad
import requests
from pandas.io.json import json_normalize


class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        

        self.frames = {}
        for F in (StartPage, Calculator, ToDoList, Weather):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame


            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):

        frame = self.frames[page_name]
        frame.tkraise()
        


class StartPage(tk.Frame):
    

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.controller.title('API')
        self.controller.state('zoomed')
        label = tk.Label(self, text="Main page", font=controller.title_font)
        label.place(relx=0.5, rely=0.05, anchor=CENTER)
        
        button1 = tk.Button(self, text="Go to To Do List",
                            command=lambda: controller.show_frame("ToDoList"))
        button2 = tk.Button(self, text="Go to Weather Page ",
                           command=lambda: controller.show_frame("Weather"))
        button3 = tk.Button(self, text="Go to Calculator",
                            command=lambda: controller.show_frame("Calculator"))
        button1.place(relx=0.45, rely=0.1, anchor=CENTER)
        button2.place(relx=0.5, rely=0.1, anchor=CENTER)
        button3.place(relx=0.55, rely=0.1, anchor=CENTER)


class Calculator(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is calculator page", font=controller.title_font)
        label.place(relx=0.5, rely=0.05, anchor=CENTER)
        def open_calculator():
            os.system('E:\Programowanie\Zespolowe\dist\Calculator.exe')
        
           
        button4 = tk.Button(self, text ='Open caluclator',
                            command = open_calculator)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button2 = tk.Button(self, text="Go to To Do List",
                            command=lambda: controller.show_frame("ToDoList"))
        button3 = tk.Button(self, text="Go to Weather Page ",
                            command=lambda: controller.show_frame("Weather"))
        button.place(relx=0.45, rely=0.1, anchor=CENTER)
        button2.place(relx=0.5, rely=0.1, anchor=CENTER)
        button3.place(relx=0.55, rely=0.1, anchor=CENTER)
        button4.place(relx=0.5, rely=0.2, anchor=CENTER)


class ToDoList(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        frame = tk.Frame(self)
        frame.pack(pady = 300)
        list = Listbox(frame, width=25, height=5, bd=0, fg="#000000")
        list.pack(side=LEFT, fill=BOTH)

        def delete_item():
            list.delete(ANCHOR)
        def add_item():
            list.insert(END, entry.get())
            entry.delete(0, END)
        def cross_item():
            list.itemconfig(
                list.curselection(),
                fg="#c2c2c2")
            list.selection_clear(0, END)
        def uncross_item():
            list.itemconfig(
                list.curselection(),
                fg="#000000")
            list.selection_clear(0, END)


        stuff=[]
        for item in stuff:
            list.insert(END, item)
        scrollbar = Scrollbar(frame)
        scrollbar.pack(side=RIGHT, fill=BOTH)
        list.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=list.yview)
        entry = Entry(frame)
        entry.pack(pady=20) 
        button_frame = tk.Frame(frame)
        button_frame.pack(pady=20)

        delete_button=tk.Button(button_frame, text="Delete", command=delete_item)
        add_button=tk.Button(button_frame, text="Add", command=add_item)
        cross_button=tk.Button(button_frame, text="Cross item", command=cross_item)
        uncross_button=tk.Button(button_frame, text="Uncross item", command=uncross_item)

        delete_button.grid(row=0, column=0)
        add_button.grid(row=0, column=1)
        cross_button.grid(row=0, column=2)
        uncross_button.grid(row=0, column=3)


     
        label = tk.Label(self, text="This is To Do page", font=controller.title_font)
        label.place(relx=0.5, rely=0.05, anchor=CENTER)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button1 = tk.Button(self, text="Go to Calculator",
                            command=lambda: controller.show_frame("Calculator"))
        button3 = tk.Button(self, text="Go to Weather Page ",
                            command=lambda: controller.show_frame("Weather"))
                      

        button.place(relx=0.45, rely=0.1, anchor=CENTER)
        button1.place(relx=0.5, rely=0.1, anchor=CENTER)
        button3.place(relx=0.55, rely=0.1, anchor=CENTER)

    
class Weather(tk.Frame):

    def __init__(self, parent, controller):
        url = "https://dor-error-1234.herokuapp.com/weather/Katowice?fbclid=IwAR2Rm6w1OOh6a7_ULdHhHjpbpZzYKnDiBZAwUQiB4njM-4a94JvBu4CcjFw"
        response = urllib.request.urlopen(url)
        data = json.loads(response.read())
        reg = json_normalize(data)
        reg = reg.to_string(index=False)

        tk.Frame.__init__(self, parent)

        final = tk.Label(self, text=reg, font=controller.title_font)
        final.place(relx=0.5, rely=0.2, anchor=CENTER)
        self.controller = controller
        label = tk.Label(self, text="Weather in Katowice", font=controller.title_font)

        label.place(relx=0.5, rely=0.05, anchor=CENTER)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button1 = tk.Button(self, text="Go to Calculator",
                            command=lambda: controller.show_frame("Calculator"))
        button2 = tk.Button(self, text="Go to To Do List",
                            command=lambda: controller.show_frame("ToDoList"))
        button.place(relx=0.45, rely=0.1, anchor=CENTER)
        button1.place(relx=0.5, rely=0.1, anchor=CENTER)
        button2.place(relx=0.55, rely=0.1, anchor=CENTER)



if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()

