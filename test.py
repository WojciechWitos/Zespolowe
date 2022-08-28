import tkinter as tk                
from tkinter import CENTER, TOP, font  as tkfont 
import os
import csv
import urllib, json
import requests
from pandas.io.json import json_normalize
from tkinter import filedialog

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
        def is_a_file(self):
            if os.path.isfile("notes.csv"):
                return True
            else:
                return False
        def read_note(self):
            array = []
            if is_a_file():
        
                with open("notes.csv","r") as csvfile:
                    datareader = csv.reader(csvfile)
                    for row in datareader:
                        array = array+row
                        print(row)
                return array
            else:
                with open("notes.csv", "a+", newline='') as f:
                    header = ["Data", "Notatka"]
                    writer = csv.DictWriter(f, fieldnames=header)
                    writer.writeheader()
                with open("notes.csv","r") as csvfile:
                    datareader = csv.reader(csvfile)
                    for row in datareader:
                        array = array+row
                    if len(array)==2:
                        array +=" "
            return array
        

        def add_note(self,  date, text):
            header = ["Data", "Notatka"]
            if is_a_file() is True:
                with open("notes.csv", "a+", newline='') as f:
                    writer = csv.DictWriter(f, fieldnames=header)
                    writer.writerow({"Data": date, "Notatka": text})
            else:
                with open("notes.csv", "a+", newline='') as f:
                    writer = csv.DictWriter(f, fieldnames=header)
                    writer.writeheader()
                    writer.writerow({"Data": date, "Notatka": text})

        buttonAdd = tk.Button(self,  text="Add Note ",
                            command=add_note)
        buttonRead = tk.Button(self, text="Read Note ",
                            command=read_note)                           

        buttonAdd.place(relx=0.45, rely=0.6, anchor=CENTER)  
        buttonRead.place(relx=0.5, rely=0.6, anchor=CENTER)        



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

