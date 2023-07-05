from tkinter import *

class BackGround:
    def __init__(self, calculator):
        self.calculator = calculator

    def dark_background(self, *args):
        self.calculator.style_frame.configure('mainFrame.TFrame', background = "#010924")
        self.calculator.style_label_1.configure('label1.TLabel', background = "#010924", foreground = "white")
        self.calculator.style_label_2.configure('label2.TLabel', background = "#010924", foreground = "white")
        
        self.calculator.numeric_buttons.configure('botones_numericos.TButton', background = "#00044A", foreground = "white")
        self.calculator.numeric_buttons.map('botones_numericos.TButton', background = [("active", "#020A90")])
        
        self.calculator.style_del_buttons.configure('botones_borrar.TButton', background = "#010924", foreground = "white")
        self.calculator.style_del_buttons.map('botones_borrar.TButton', background = [("active", "#000AB1")])
        
        self.calculator.restant_buttons.configure('botones_restantes.TButton', background = "#010924", foreground = "white")
        self.calculator.restant_buttons.map('botones_restantes.TButton', background = [("active", "#000AB1")])
        
        self.calculator.style_equal_button.configure('boton_igual.TButton', background = "#010924", foreground = "white")
        self.calculator.style_equal_button.map('boton_igual.TButton', background = [("active", "#000AB1")])

    def light_background(self, *args):
        self.calculator.style_frame.configure('mainFrame.TFrame', background = "#DBDBDB", foreground = "black")
        self.calculator.style_label_1.configure('label1.TLabel', background = "#DBDBDB", foreground = "black")
        self.calculator.style_label_2.configure('label2.TLabel', background = "#DBDBDB", foreground = "black")

        self.calculator.numeric_buttons.configure('botones_numericos.TButton', background = "#FFFFFF", foreground = "black")
        self.calculator.numeric_buttons.map('botones_numericos.TButton', background = [("active","#EAEEE0")])

        self.calculator.style_del_buttons.configure('botones_borrar.TButton', background = "#CECECE", foreground = "black")
        self.calculator.style_del_buttons.map('botones_borrar.TButton', background = [("active","#858585")])

        self.calculator.restant_buttons.configure('botones_restantes.TButton', background = "#CECECE", foreground = "black")
        self.calculator.restant_buttons.map('botones_restantes.TButton', background = [("active", "#858585")])

        self.calculator.style_equal_button.configure('boton_igual.TButton', background = "#CECECE", foreground = "black")
        self.calculator.style_equal_button.map('boton_igual.TButton', background = [("active", "#DADADC")])



