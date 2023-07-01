from tkinter import *
from tkinter import ttk

from calculator.Operations.operation import Operation

class Calculator:
    def __init__(self):
        self.root = self.root()
        self.main_frame = self.frame_configure()
        self.style_frame = self.frame_style()
        self.button_0, self.button_1, self.button_2, self.button_3, self.button_4 = self.number_buttons_1()
        self.button_5, self.button_6, self.button_7, self.button_8, self.button_9 = self.number_buttons_2()
        self.del_button, self.del_all_button, self.bracket_button_1, self.bracket_button_2, self.point_button = self.extra_buttons()
        self.sum_button, self.rest_button, self.mult_button, self.divition_button = self.operation_buttons()
        self.square_root_button, self.resoult_button = self.resoult_buttons()

        self.entrada_1 = StringVar()
        self.entrada_2 = StringVar()
        self.operation = Operation()  

    def root(self):
        root = Tk()
        root.title("calculadora")
        root.geometry("+500+80")
        root.columnconfigure(0, weight = 1)
        root.rowconfigure(0, weight = 1)
        return root
    
    def number_buttons_1(self):
        button_0 = ttk.Button(self.main_frame, text = "0", style = "botones_numericos.TButton", command = lambda:self.operation.insert_values("0", self))
        button_1 = ttk.Button(self.main_frame, text = "1", style = "botones_numericos.TButton", command = lambda:self.operation.insert_values("1", self))
        button_2 = ttk.Button(self.main_frame, text = "2", style = "botones_numericos.TButton", command = lambda:self.operation.insert_values("2", self))
        button_3 = ttk.Button(self.main_frame, text = "3", style = "botones_numericos.TButton", command = lambda:self.operation.insert_values("3", self))
        button_4 = ttk.Button(self.main_frame, text = "4", style = "botones_numericos.TButton",command =  lambda:self.operation.insert_values("4", self))
        return button_0, button_1, button_2, button_3, button_4
    
    def number_buttons_2(self):
        button_5 = ttk.Button(self.main_frame, text = "5", style = "botones_numericos.TButton", command = lambda:self.operation.insert_values("5", self))
        button_6 = ttk.Button(self.main_frame, text = "6", style = "botones_numericos.TButton", command = lambda:self.operation.insert_values("6", self))
        button_7 = ttk.Button(self.main_frame, text = "7", style = "botones_numericos.TButton", command = lambda:self.operation.insert_values("7", self))
        button_8 = ttk.Button(self.main_frame, text = "8", style = "botones_numericos.TButton", command = lambda:self.operation.insert_values("8", self))
        button_9 = ttk.Button(self.main_frame, text = "9", style = "botones_numericos.TButton", command = lambda:self.operation.insert_values("9", self))
        return button_5, button_6, button_7, button_8, button_9
    
    def extra_buttons(self):
        del_button = ttk.Button(self.main_frame, text = chr(9003), style = "botones_borrar.TButton")
        del_all_button = ttk.Button(self.main_frame, text = "C", style = "botones_borrar.TButton")
        bracket_button_1 = ttk.Button(self.main_frame, text = "(", style = "botones_restantes.TButton")
        bracket_button_2 = ttk.Button(self.main_frame, text = ")", style = "botones_restantes.TButton")
        point_button = ttk.Button(self.main_frame, text = ".", style = "botones_restantes.TButton", command = lambda:self.operation.insert_values(".", self))
        return del_button, del_all_button, bracket_button_1, bracket_button_2, point_button
    
    def resoult_buttons(self):
        square_root_button = ttk.Button(self.main_frame, text = chr(8730), style = "botones_restantes.TButton")
        resoult_button = ttk.Button(self.main_frame, text = chr(61), style = "boton_igual.TButton", command = lambda:self.operation.insert_values("=", self))
        return square_root_button, resoult_button
    
    def operation_buttons(self):
        sum_button = ttk.Button(self.main_frame, text = chr(43), style = "botones_restantes.TButton", command = lambda:self.operation.insert_values("+", self))
        rest_button = ttk.Button(self.main_frame, text = chr(8722), style = "botones_restantes.TButton", command = lambda:self.operation.insert_values("-", self))
        mult_button = ttk.Button(self.main_frame, text = chr(215), style = "botones_restantes.TButton", command = lambda:self.operation.insert_values("*", self))
        divition_button = ttk.Button(self.main_frame, text = chr(247), style = "botones_restantes.TButton", command = lambda:self.operation.insert_values("/", self))
        return sum_button, rest_button, mult_button, divition_button

    def frame_configure(self):
        main_frame = ttk.Frame(self.root, style = "mainFrame.TFrame")
        main_frame.grid(row = 0, column = 0, sticky = (W, N, E, S ))
        main_frame.config(cursor = "hand2")
        main_frame.columnconfigure(0, weight = 1)
        main_frame.columnconfigure(1, weight = 1)
        main_frame.columnconfigure(2, weight = 1)
        main_frame.columnconfigure(3, weight = 1)

        main_frame.rowconfigure(0, weight = 1)
        main_frame.rowconfigure(1, weight = 1)
        main_frame.rowconfigure(2, weight = 1)
        main_frame.rowconfigure(3, weight = 1)
        main_frame.rowconfigure(4, weight = 1)
        main_frame.rowconfigure(5, weight = 1)
        main_frame.rowconfigure(6, weight = 1)
        main_frame.rowconfigure(7, weight = 1)
        return main_frame

    def frame_style(self):
        estilos_frame = ttk.Style()
        estilos_frame.theme_use("clam")
        estilos_frame.configure('mainFrame.TFrame', background = "#DBDBDB")
        return estilos_frame
                
    def label(self):
        estilo_label_1 = ttk.Style()
        estilos_label_2 = ttk.Style()
        estilo_label_1.configure('label1.TLabel', font = "arial 15", anchor = "e")
        estilos_label_2.configure('label2.TLabel', font = "arial 40", anchor = "e")

        label_entrada_1 = ttk.Label(self.main_frame, textvariable = self.entrada_1, style = "label1.TLabel")
        label_entrada_2 = ttk.Label(self.main_frame, textvariable = self.entrada_2, style = "label2.TLabel")
        
        label_entrada_1.grid(row = 0, column = 0, columnspan = 4, sticky = (W, N, E, S))
        label_entrada_2.grid(row = 1, column = 0, columnspan = 4, sticky = (W, N, E, S))
    
    def style_numeric_button(self):
        botones_numericos = ttk.Style()
        botones_numericos.configure('botones_numericos.TButton', width = 5, font = "arial 22", relief = "flat", background = "#FFFFFF")
        botones_numericos.map('botones_numericos.TButton', background = [("active","#EAEEE0")])
        return botones_numericos
    
    def style_del_button(self):
        botones_borrar = ttk.Style()
        botones_borrar.configure('botones_borrar.TButton', width = 5, font = "arial 22", relief = "flat", background = "#CECECE")
        botones_borrar.map('botones_borrar.TButton', foreground = [("active","#FF0000")], background =[("active","#858585")])
        return botones_borrar
    
    def style_restant_buttons(self):
        botones_restantes = ttk.Style()
        botones_restantes.configure('botones_restantes.TButton', width = 5, font = "arial 22", relief = "flat", background = "#CECECE")
        botones_restantes.map('botones_restantes.TButton', background = [("active", "#858585")])
        return botones_restantes
    
    def style_button_equal(self):
        boton_igual = ttk.Style()
        boton_igual.configure('boton_igual.TButton',width = 5, font = "arial 22", relief = "flat", background = "#CECECE")
        boton_igual.map('boton_igual.TButton', foreground = [("active", "#70FF8B")], background = [("active", "#DADADC")])
        return boton_igual
    
    def firts_row_buttons(self):
        self.bracket_button_1.grid(row = 2, column = 0, sticky = (W,N,E,S))
        self.bracket_button_2.grid(row = 2, column = 1, sticky = (W,N,E,S))
        self.del_all_button.grid(row = 2, column = 2, sticky = (W,N,E,S))
        self.del_button.grid(row = 2, column = 3, sticky = (W,N,E,S))

    def second_row_buttons(self):
        self.button_7.grid(column = 0, row = 3, sticky = (W, N, E, S))
        self.button_8.grid(column = 1, row = 3, sticky = (W, N, E, S))
        self.button_9.grid(column = 2, row = 3, sticky = (W, N, E, S))
        self.divition_button.grid(column = 3, row = 3, sticky = (W, N, E, S))

    def third_row_buttons(self):
        self.button_4.grid(column = 0, row = 4, sticky = (W, N, E, S))
        self.button_5.grid(column = 1, row = 4, sticky = (W, N, E, S))
        self.button_6.grid(column = 2, row = 4, sticky = (W, N, E, S))
        self.mult_button.grid(column = 3, row = 4, sticky = (W, N, E, S))

    def four_row_buttons(self):
        self.button_1.grid(column = 0, row = 5, sticky = (W, N, E, S))
        self.button_2.grid(column = 1, row = 5, sticky = (W, N, E, S))
        self.button_3.grid(column = 2, row = 5, sticky = (W, N, E, S))
        self.sum_button.grid(column = 3, row = 5, sticky = (W, N, E, S))

    def five_row_buttons(self):
        self.button_0.grid(row = 6, column = 0, columnspan = 2, sticky = (W, N, E, S))
        self.point_button.grid(row = 6, column = 2, sticky = (W, N, E, S))
        self.rest_button.grid(row = 6,column = 3, sticky = (W, N, E, S))
        self.resoult_button.grid(row = 7, column = 0, columnspan = 3, sticky = (W, N, E, S))
        self.square_root_button.grid(row = 7, column = 3 , sticky = (W, N, E, S))
    
    def configure_buttons(self):
        self.point_button.config(state = "disabled")
        self.resoult_button.config(state = "disabled")
        self.square_root_button.config(state = "disabled")
        self.sum_button.config(state = "disabled")
        self.mult_button.config(state = "disabled")
        self.divition_button.config(state = "disabled")

    def main_buttons(self):
        botones_numericos = self.style_numeric_button()
        botones_borrar = self.style_del_button()
        botones_restantes = self.style_restant_buttons()
        boton_igual = self.style_button_equal()
        self.label()

        self.configure_buttons()
        self.firts_row_buttons()
        self.second_row_buttons()
        self.third_row_buttons()
        self.four_row_buttons()
        self.five_row_buttons()

    def button_configure(self):
        for child in self.main_frame.winfo_children():
            child.grid_configure(ipady= 10, padx = 1, pady = 1) 
        self.root.mainloop() 
