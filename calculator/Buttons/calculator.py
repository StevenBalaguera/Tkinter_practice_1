from tkinter import *
from tkinter import ttk

from calculator.Buttons.Button import Buttons
from calculator.Buttons.grid_buttons import GridButtons
from calculator.background.Background import BackGround

class Calculator:
    def __init__(self):
        self.root = self.root()
        self.main_frame = self.frame_configure()
        self.style_frame = self.frame_style()
        self.style_label_1 = self.label_style_1()
        self.style_label_2 = self.label_style_2() 
        self.entrada_1 = StringVar()
        self.entrada_2 = StringVar()
        self.buttons = Buttons(self) 
        self.grid_buttons = GridButtons(self)
        self.background = BackGround(self)
        self.button_0 = self.buttons.button_0()
        self.button_1 = self.buttons.button_1()
        self.button_2 = self.buttons.button_2()
        self.button_3 = self.buttons.button_3()
        self.button_4 = self.buttons.button_4()
        self.button_5 = self.buttons.button_5()
        self.button_6 = self.buttons.button_6()
        self.button_7 = self.buttons.button_7()
        self.button_8 = self.buttons.button_8()
        self.button_9 = self.buttons.button_9()
        self.del_button = self.buttons.del_button()
        self.del_all_button = self.buttons.del_all_button()
        self.bracket_button_1 = self.buttons.bracket_button_1()
        self.bracket_button_2 = self.buttons.bracket_button_2()
        self.point_button = self.buttons.point_button()
        self.sum_button = self.buttons.sum_button()
        self.rest_button = self.buttons.rest_button()
        self.mult_button = self.buttons.mult_button()
        self.divition_button = self.buttons.divition_button()
        self.square_root_button = self.buttons.square_root_button()
        self.resoult_button = self.buttons.resoult_button()
        self.numeric_buttons = self.style_numeric_button()
        self.style_del_buttons = self.style_del_button()
        self.style_equal_button = self.style_button_equal()
        self.restant_buttons = self.style_restant_buttons()

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
    
    def label_style_1(self):
        label_style_1 = ttk.Style()
        label_style_1.configure('label1.TLabel', font = "arial 15", anchor = "e")
        return label_style_1

    def label_style_2(self):
        label_style_2 = ttk.Style()
        label_style_2.configure('label2.TLabel', font = "arial 40", anchor = "e")
        return label_style_2
                
    def label(self):
        self.label_style_1()
        self.label_style_2()
        label_entrada_1 = ttk.Label(self.main_frame, textvariable = self.entrada_1, style = "label1.TLabel")
        label_entrada_2 = ttk.Label(self.main_frame, textvariable = self.entrada_2, style = "label2.TLabel")
        
        label_entrada_1.grid(row = 0, column = 0, columnspan = 4, sticky = (W, N, E, S))
        label_entrada_2.grid(row = 1, column = 0, columnspan = 4, sticky = (W, N, E, S))
    
    def style_numeric_button(self):
        numeric_buttons = ttk.Style()
        numeric_buttons.configure('botones_numericos.TButton', width = 5, font = "arial 22", relief = "flat", background = "#FFFFFF")
        numeric_buttons.map('botones_numericos.TButton', background = [("active","#EAEEE0")])
        return numeric_buttons
    
    def style_del_button(self):
        del_button = ttk.Style()
        del_button.configure('botones_borrar.TButton', width = 5, font = "arial 22", relief = "flat", background = "#CECECE")
        del_button.map('botones_borrar.TButton', foreground = [("active","#FF0000")], background =[("active","#858585")])
        return del_button
    
    def style_button_equal(self):
        equal_button = ttk.Style()
        equal_button.configure('boton_igual.TButton',width = 5, font = "arial 22", relief = "flat", background = "#CECECE")
        equal_button.map('boton_igual.TButton', foreground = [("active", "#70FF8B")], background = [("active", "#DADADC")])
        return equal_button
    
    def style_restant_buttons(self):
        restant_buttons = ttk.Style()
        restant_buttons.configure('botones_restantes.TButton', width = 5, font = "arial 22", relief = "flat", background = "#CECECE")
        restant_buttons.map('botones_restantes.TButton', background = [("active", "#858585")])
        return restant_buttons
    
    def button_state_setting(self):
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

        self.button_state_setting()
        self.grid_buttons.firts_row_buttons()
        self.grid_buttons.second_row_buttons()
        self.grid_buttons.third_row_buttons()
        self.grid_buttons.four_row_buttons()
        self.grid_buttons.five_row_buttons()

        self.bind_background()

    def bind_background(self):
        self.root.bind('<KeyPress-o>', self.background.dark_background)
        self.root.bind('<KeyPress-c>', self.background.light_background)

    def button_configure(self):
        for child in self.main_frame.winfo_children():
            child.grid_configure(ipady= 10, padx = 1, pady = 1) 
        self.root.mainloop() 
