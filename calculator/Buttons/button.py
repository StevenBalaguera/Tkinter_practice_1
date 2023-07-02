from tkinter import *
from tkinter import ttk

from calculator.Buttons.grid_buttons import GridButtons

class Calculator:
    def __init__(self):
        self.root = self.root()
        self.main_frame = self.frame_configure()
        self.style_frame = self.frame_style()
        self.entrada_1 = StringVar()
        self.entrada_2 = StringVar()
        self.grid_buttons = GridButtons(self)
        self.button_0 = self.grid_buttons.button_0()
        self.button_1 = self.grid_buttons.button_1()
        self.button_2 = self.grid_buttons.button_2()
        self.button_3 = self.grid_buttons.button_3()
        self.button_4 = self.grid_buttons.button_4()
        self.button_5 = self.grid_buttons.button_5()
        self.button_6 = self.grid_buttons.button_6()
        self.button_7 = self.grid_buttons.button_7()
        self.button_8 = self.grid_buttons.button_8()
        self.button_9 = self.grid_buttons.button_9()
        self.del_button = self.grid_buttons.del_button()
        self.del_all_button = self.grid_buttons.del_all_button()
        self.bracket_button_1 = self.grid_buttons.bracket_button_1()
        self.bracket_button_2 = self.grid_buttons.bracket_button_2()
        self.point_button = self.grid_buttons.point_button()
        self.sum_button = self.grid_buttons.sum_button()
        self.rest_button = self.grid_buttons.rest_button()
        self.mult_button = self.grid_buttons.mult_button()
        self.divition_button = self.grid_buttons.divition_button()
        self.square_root_button = self.grid_buttons.square_root_button()
        self.resoult_button = self.grid_buttons.resoult_button()

    def root(self):
        root = Tk()
        root.title("calculadora")
        root.geometry("+500+80")
        root.columnconfigure(0, weight = 1)
        root.rowconfigure(0, weight = 1)
        return root
    
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
    
    def style_button_equal(self):
        boton_igual = ttk.Style()
        boton_igual.configure('boton_igual.TButton',width = 5, font = "arial 22", relief = "flat", background = "#CECECE")
        boton_igual.map('boton_igual.TButton', foreground = [("active", "#70FF8B")], background = [("active", "#DADADC")])
        return boton_igual
    
    def style_restant_buttons(self):
        botones_restantes = ttk.Style()
        botones_restantes.configure('botones_restantes.TButton', width = 5, font = "arial 22", relief = "flat", background = "#CECECE")
        botones_restantes.map('botones_restantes.TButton', background = [("active", "#858585")])
        return botones_restantes
    
    def configure_buttons(self):
        self.point_button.config(state = "disabled")
        self.resoult_button.config(state = "disabled")
        self.square_root_button.config(state = "disabled")
        self.sum_button.config(state = "disabled")
        self.mult_button.config(state = "disabled")
        self.divition_button.config(state = "disabled")

    def main_buttons(self):
        self.style_numeric_button()
        self.style_del_button()
        self.style_restant_buttons()
        self.style_button_equal()
        self.label()

        self.configure_buttons()
        self.grid_buttons.firts_row_buttons(self)
        self.grid_buttons.second_row_buttons(self)
        self.grid_buttons.third_row_buttons(self)
        self.grid_buttons.four_row_buttons(self)
        self.grid_buttons.five_row_buttons(self)

    def button_configure(self):
        for child in self.main_frame.winfo_children():
            child.grid_configure(ipady= 10, padx = 1, pady = 1) 
        self.root.mainloop() 
