from tkinter import *
from tkinter import ttk

class Button:
    def __init__(self):
        self.root = Tk()
        self.root.title("calculadora")
        self.root.geometry("+500+80")
        self.root.columnconfigure(0, weight = 1)
        self.root.rowconfigure(0, weight = 1)
        self.estilos_frame = ttk.Style()
        self.estilos_frame.theme_use("clam")
        self.estilos_frame.configure('mainFrame.TFrame', background = "#DBDBDB")
        self.main_frame = ttk.Frame(self.root, style = "mainFrame.TFrame")
        self.main_frame.grid(row = 0, column = 0, sticky = (W, N, E, S ))
        self.main_frame.config(cursor = "hand2")
        self.main_frame.columnconfigure(0, weight = 1)
        self.main_frame.columnconfigure(1, weight = 1)
        self.main_frame.columnconfigure(2, weight = 1)
        self.main_frame.columnconfigure(3, weight = 1)

        self.main_frame.rowconfigure(0, weight = 1)
        self.main_frame.rowconfigure(1, weight = 1)
        self.main_frame.rowconfigure(2, weight = 1)
        self.main_frame.rowconfigure(3, weight = 1)
        self.main_frame.rowconfigure(4, weight = 1)
        self.main_frame.rowconfigure(5, weight = 1)
        self.main_frame.rowconfigure(6, weight = 1)
        self.main_frame.rowconfigure(7, weight = 1)

        self.entrada_1 = StringVar()
        self.entrada_2 = StringVar()
                
    def label(self):
        estilo_label_1 = ttk.Style()
        estilo_label_1.configure('label1.TLabel', font = "arial 15", anchor = "e")

        estilos_label_2 = ttk.Style()
        estilos_label_2.configure('label2.TLabel', font = "arial 40", anchor = "e")

        label_entrada_1 = ttk.Label(self.main_frame, textvariable = self.entrada_1, style = "label1.TLabel")
        label_entrada_1.grid(row = 0, column = 0, columnspan = 4, sticky = (W, N, E, S))
        label_entrada_2 = ttk.Label(self.main_frame, textvariable = self.entrada_2, style = "label2.TLabel")
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

    def buttons_numbers(self):
        botones_numericos = self.style_numeric_button()
        botones_borrar = self.style_del_button()
        botones_restantes = self.style_restant_buttons()
        boton_igual = self.style_button_equal()

        
        boton_0 = ttk.Button(self.main_frame, text = "0", style = "botones_numericos.TButton")
        boton_1 = ttk.Button(self.main_frame, text = "1", style = "botones_numericos.TButton")
        boton_2 = ttk.Button(self.main_frame, text = "2", style = "botones_numericos.TButton")
        boton_3 = ttk.Button(self.main_frame, text = "3", style = "botones_numericos.TButton")
        boton_4 = ttk.Button(self.main_frame, text = "4", style = "botones_numericos.TButton")
        boton_5 = ttk.Button(self.main_frame, text = "5", style = "botones_numericos.TButton")
        boton_6 = ttk.Button(self.main_frame, text = "6", style = "botones_numericos.TButton")
        boton_7 = ttk.Button(self.main_frame, text = "7", style = "botones_numericos.TButton")
        boton_8 = ttk.Button(self.main_frame, text = "8", style = "botones_numericos.TButton")
        boton_9 = ttk.Button(self.main_frame, text = "9", style = "botones_numericos.TButton")

        del_buttons = ttk.Button(self.main_frame, text = chr(9003), style = "botones_borrar.TButton")
        boton_borrar_todo = ttk.Button(self.main_frame, text = "C", style = "botones_borrar.TButton")
        boton_parentesis_1 = ttk.Button(self.main_frame, text = "(", style = "botones_restantes.TButton")
        boton_parentesis_2 = ttk.Button(self.main_frame, text = ")", style = "botones_restantes.TButton")
        boton_punto = ttk.Button(self.main_frame, text = ".", style = "botones_restantes.TButton")
        boton_punto.config(state = "disabled")

        boton_raiz_cuadrada = ttk.Button(self.main_frame, text = chr(8730), style = "botones_restantes.TButton")
        boton_raiz_cuadrada.config(state = "disabled")
        boton_resultado = ttk.Button(self.main_frame, text = chr(61), style = "boton_igual.TButton")
        boton_resultado.config(state = "disabled")

        botones_restantes = self.style_restant_buttons()
        boton_suma = ttk.Button(self.main_frame, text = chr(43), style = "botones_restantes.TButton")
        boton_suma.config(state = "disabled")
        boton_resta = ttk.Button(self.main_frame, text = chr(8722), style = "botones_restantes.TButton")
        boton_resta.config(state = "Normal")
        boton_multiplicacion = ttk.Button(self.main_frame, text = chr(215), style = "botones_restantes.TButton")
        boton_multiplicacion.config(state = "disabled")
        boton_division = ttk.Button(self.main_frame, text = chr(247), style = "botones_restantes.TButton")
        boton_division.config(state = "disabled")

        self.firts_row_button(boton_parentesis_1, boton_parentesis_2, boton_borrar_todo, del_buttons)
        self.second_row_button(boton_7, boton_8, boton_9, boton_division)
        self.third_row_button(boton_4, boton_5, boton_6, boton_multiplicacion)
        self.four_row_button(boton_1, boton_2, boton_3, boton_suma)
        self.five_row_button( boton_0, boton_punto, boton_resta, boton_resultado, boton_raiz_cuadrada)
        
    def firts_row_button(self, boton_parentesis_1, boton_parentesis_2, boton_borrar_todo, del_buttons):
        boton_parentesis_1.grid(row = 2, column = 0, sticky = (W,N,E,S))
        boton_parentesis_2.grid(row = 2, column = 1, sticky = (W,N,E,S))
        boton_borrar_todo.grid(row = 2, column = 2, sticky = (W,N,E,S))
        del_buttons.grid(row = 2, column = 3, sticky = (W,N,E,S))

    def second_row_button(self, boton_7, boton_8, boton_9, boton_division):
        boton_7.grid(column = 0, row = 3, sticky = (W, N, E, S))
        boton_8.grid(column = 1, row = 3, sticky = (W, N, E, S))
        boton_9.grid(column = 2, row = 3, sticky = (W, N, E, S))
        boton_division.grid(column = 3, row = 3, sticky = (W, N, E, S))

    def third_row_button(self, boton_4, boton_5, boton_6, boton_multiplicacion):
        boton_4.grid(column = 0, row = 4, sticky = (W, N, E, S))
        boton_5.grid(column = 1, row = 4, sticky = (W, N, E, S))
        boton_6.grid(column = 2, row = 4, sticky = (W, N, E, S))
        boton_multiplicacion.grid(column = 3, row = 4, sticky = (W, N, E, S))

    def four_row_button(self, boton_1, boton_2, boton_3, boton_suma):
        boton_1.grid(column = 0, row = 5, sticky = (W, N, E, S))
        boton_2.grid(column = 1, row = 5, sticky = (W, N, E, S))
        boton_3.grid(column = 2, row = 5, sticky = (W, N, E, S))
        boton_suma.grid(column = 3, row = 5, sticky = (W, N, E, S))

    def five_row_button(self, boton_0, boton_punto, boton_resta, boton_resultado, boton_raiz_cuadrada):
        boton_0.grid(row = 6, column = 0, columnspan = 2, sticky = (W, N, E, S))
        boton_punto.grid(row = 6, column = 2, sticky = (W, N, E, S))
        boton_resta.grid(row = 6,column = 3, sticky = (W, N, E, S))
        boton_resultado.grid(row = 7, column = 0, columnspan = 3, sticky = (W, N, E, S))
        boton_raiz_cuadrada.grid(row = 7, column = 3 , sticky = (W, N, E, S))

    def button_configure(self):
        for child in self.main_frame.winfo_children():
            child.grid_configure(ipady= 10, padx = 1, pady = 1) 
        self.root.mainloop() 



button = Button()
button.buttons_numbers()
button.label()
button.button_configure()