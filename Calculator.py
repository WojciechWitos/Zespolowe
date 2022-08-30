import tkinter as tk


#czcionka
LARGE_FONT_STYLE = ("Arial", 40, "bold")
SMALL_FONT_STYLE = ("Arial", 16)
DIGITS_FONT_STYLE = ("Arial", 24, "bold")
DEFAULT_FONT_STYLE = ("Arial", 20)


#kolorki :)
OFF_GRAY = "#272727"
DISPLAY_GRAY = "#515151"
GRAY_BLUE = "#7C9979"
LIGHT_GRAY = "#303030"
GRAY_RED = "#B97777"
LABEL_COLOR = "#C5C5C5"


class Calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("400x700")                                     #wymiary
        self.window.attributes('-alpha',0.9)                                #przezroczystosc
        self.window.resizable(0, 0)                                         #brak mozliwosci zmiany rozmiarow okna
        self.window.title("Calculator")                                     #tytul

        self.total_expression = ""                                          #dzialanie
        self.current_expression = ""                                        #wynik // biezaca liczba
        
        self.display_frame = self.create_display_frame()
        self.buttons_frame = self.create_buttons_frame()

        self.total_label, self.label = self.create_display_labels()

        
        
        #tablica przyciskow numerycznych
        self.digits = {
            7: (1, 1), 8: (1, 2), 9: (1, 3),
            4: (2, 1), 5: (2, 2), 6: (2, 3),
            1: (3, 1), 2: (3, 2), 3: (3, 3),
            0: (4, 2), '.': (4, 1)
        }
        
        #tablica przyciskow operacyjnych
        self.operations = {"/": "\u00F7", "*": "\u00D7", "-": "-", "+": "+"}
        


        self.buttons_frame.rowconfigure(0, weight=1)
        for x in range(1, 5):
            #zmiana rozmiaru przyciskow
            self.buttons_frame.rowconfigure(x, weight=1)
            self.buttons_frame.columnconfigure(x, weight=1)
            
            
        self.create_digit_buttons()
        self.create_operator_buttons()
        self.create_special_buttons()
        
        
        
        
    def create_display_frame(self):
        frame = tk.Frame(self.window, height=221, bg=LIGHT_GRAY)
        frame.pack(expand=True, fill="both")
        return frame
        
    def create_buttons_frame(self):
        frame = tk.Frame(self.window)
        frame.pack(expand=True, fill="both")
        return frame
        
 
 
 
    def create_display_labels(self):
        total_label = tk.Label(self.display_frame, text=self.total_expression, anchor=tk.E, bg=DISPLAY_GRAY,
                               fg=LABEL_COLOR, padx=24, font=SMALL_FONT_STYLE)
        total_label.pack(expand=True, fill='both')

        label = tk.Label(self.display_frame, text=self.current_expression, anchor=tk.E, bg=DISPLAY_GRAY,
                         fg=LABEL_COLOR, padx=24, font=LARGE_FONT_STYLE)
        label.pack(expand=True, fill='both')

        return total_label, label
        
        
        
        
       
    def create_digit_buttons(self):
        for digit, grid_value in self.digits.items():
            button = tk.Button(self.buttons_frame, text=str(digit), bg=LIGHT_GRAY, fg=LABEL_COLOR, font=DIGITS_FONT_STYLE,
                               borderwidth=0, command=lambda x=digit: self.add_to_expression(x))
            button.grid(row=grid_value[0], column=grid_value[1], sticky=tk.NSEW)    
        
    def create_special_buttons(self):
        self.create_clear_button()
        self.create_equals_button()

    def create_operator_buttons(self):
        i = 0
        for operator, symbol in self.operations.items():
            button = tk.Button(self.buttons_frame, text=symbol, bg=OFF_GRAY, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                               borderwidth=0, command=lambda x=operator: self.append_operator(x))
            button.grid(row=i, column=4, sticky=tk.NSEW)
            i += 1

    def create_clear_button(self):
        button = tk.Button(self.buttons_frame, text="C", bg=GRAY_RED, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                           borderwidth=0, command=self.clear)
        button.grid(row=0, column=1, columnspan=3, sticky=tk.NSEW)

    def create_equals_button(self):
        button = tk.Button(self.buttons_frame, text="=", bg=GRAY_BLUE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                           borderwidth=0, command=self.validate_expresion)
        button.grid(row=4, column=3, columnspan=2, sticky=tk.NSEW)

    


    def add_to_expression(self, value):
        self.current_expression += str(value)
        self.update_label()
    
    def append_operator(self, operator):
        self.current_expression += operator
        self.total_expression += self.current_expression
        self.current_expression = ""
        self.update_total_label()
        self.update_label()

    def clear(self):
        self.current_expression = ""
        self.total_expression = ""
        self.update_label()
        self.update_total_label()




    def update_total_label(self):
        expression = self.total_expression
        for operator, symbol in self.operations.items():
            expression = expression.replace(operator, f' {symbol} ')
        self.total_label.config(text=expression)

    def update_label(self):
        #ograniczenie ilosci cyfr na wyswietlaczu
        self.label.config(text=self.current_expression[:12]) 





    def validate_expresion(self):
        #walidacje obliczen
        self.total_expression += self.current_expression
        self.update_total_label()
        try:
            self.current_expression = str(eval(self.total_expression))

            self.total_expression = ""
        except Exception as e:
            self.current_expression = "Error"
        finally:
            self.update_label()

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    calc = Calculator()
    calc.run()