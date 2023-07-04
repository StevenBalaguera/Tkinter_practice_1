from tkinter import *
from tkinter import ttk

from calculator.Operations.operation import Operation

class GridButtons:
    def __init__(self, calculator):
        self.calculator = calculator
        self.operation = Operation(calculator)

    def button_0(self):
        button_0 = ttk.Button(self.calculator.main_frame, text = "0", style = "botones_numericos.TButton", command = lambda:self.operation.insert_values("0"))
        return button_0
    
    def button_1(self):
        button_1 = ttk.Button(self.calculator.main_frame, text = "1", style = "botones_numericos.TButton", command = lambda:self.operation.insert_values("1"))
        return button_1
    
    def button_2(self):
        button_2 = ttk.Button(self.calculator.main_frame, text = "2", style = "botones_numericos.TButton", command = lambda:self.operation.insert_values("2"))
        return button_2
    
    def button_3(self):
        button_3 = ttk.Button(self.calculator.main_frame, text = "3", style = "botones_numericos.TButton", command = lambda:self.operation.insert_values("3"))
        return button_3
   
    def button_4(self):
        button_4 = ttk.Button(self.calculator.main_frame, text = "4", style = "botones_numericos.TButton", command = lambda:self.operation.insert_values("4"))
        return button_4
    
    def button_5(self):
        button_5 = ttk.Button(self.calculator.main_frame, text = "5", style = "botones_numericos.TButton", command = lambda:self.operation.insert_values("5"))
        return button_5
    
    def button_6(self):
        button_6 = ttk.Button(self.calculator.main_frame, text = "6", style = "botones_numericos.TButton", command = lambda:self.operation.insert_values("6"))
        return button_6
    
    def button_7(self):
        button_7 = ttk.Button(self.calculator.main_frame, text = "7", style = "botones_numericos.TButton", command = lambda:self.operation.insert_values("7"))
        return button_7
    
    def button_8(self):
        button_8 = ttk.Button(self.calculator.main_frame, text = "8", style = "botones_numericos.TButton", command = lambda:self.operation.insert_values("8"))
        return button_8
    
    def button_9(self):
        button_9 = ttk.Button(self.calculator.main_frame, text = "9", style = "botones_numericos.TButton", command = lambda:self.operation.insert_values("9"))
        return button_9
    
    def del_button(self):
        del_button = ttk.Button(self.calculator.main_frame, text = chr(9003), style = "botones_borrar.TButton", command = lambda:self.operation.del_button())
        return del_button
    
    def del_all_button(self):
        del_all_button = ttk.Button(self.calculator.main_frame, text = "C", style = "botones_borrar.TButton", command = lambda:self.operation.del_all_buttons())
        return del_all_button
    
    def bracket_button_1(self):
        bracket_button_1 = ttk.Button(self.calculator.main_frame, text = "(", style = "botones_restantes.TButton", command = lambda:self.operation.insert_values("("))
        return bracket_button_1
    
    def bracket_button_2(self):
        bracket_button_2 = ttk.Button(self.calculator.main_frame, text = ")", style = "botones_restantes.TButton", command = lambda:self.operation.insert_values(")"))
        return bracket_button_2
    
    def point_button(self):
        point_button = ttk.Button(self.calculator.main_frame, text = ".", style = "botones_restantes.TButton", command = lambda:self.operation.insert_values("."))
        return point_button
    
    def sum_button(self):
        sum_button = ttk.Button(self.calculator.main_frame, text = chr(43), style = "botones_restantes.TButton", command = lambda:self.operation.insert_values("+"))
        return sum_button
    
    def rest_button(self):
        rest_button = ttk.Button(self.calculator.main_frame, text = chr(8722), style = "botones_restantes.TButton", command = lambda:self.operation.insert_values("-"))
        return rest_button
    
    def mult_button(self):
        mult_button = ttk.Button(self.calculator.main_frame, text = chr(215), style = "botones_restantes.TButton", command = lambda:self.operation.insert_values("*"))
        return mult_button
    
    def divition_button(self):
        divition_button = ttk.Button(self.calculator.main_frame, text = chr(247), style = "botones_restantes.TButton", command = lambda:self.operation.insert_values("/"))
        return divition_button
    
    def square_root_button(self):
        square_root_button = ttk.Button(self.calculator.main_frame, text = chr(8730), style = "botones_restantes.TButton", command = lambda:self.operation.square_root())    
        return square_root_button
    
    def resoult_button(self):
        resoult_button = ttk.Button(self.calculator.main_frame, text = chr(61), style = "boton_igual.TButton", command = lambda:self.operation.insert_values("="))
        return resoult_button
    
    def firts_row_buttons(self, calculator):
        calculator.bracket_button_1.grid(row = 2, column = 0, sticky = (W,N,E,S))
        calculator.bracket_button_2.grid(row = 2, column = 1, sticky = (W,N,E,S))
        calculator.del_all_button.grid(row = 2, column = 2, sticky = (W,N,E,S))
        calculator.del_button.grid(row = 2, column = 3, sticky = (W,N,E,S))

    def second_row_buttons(self, calculator):
        calculator.button_7.grid(column = 0, row = 3, sticky = (W, N, E, S))
        calculator.button_8.grid(column = 1, row = 3, sticky = (W, N, E, S))
        calculator.button_9.grid(column = 2, row = 3, sticky = (W, N, E, S))
        calculator.divition_button.grid(column = 3, row = 3, sticky = (W, N, E, S))

    def third_row_buttons(self, calculator):
        calculator.button_4.grid(column = 0, row = 4, sticky = (W, N, E, S))
        calculator.button_5.grid(column = 1, row = 4, sticky = (W, N, E, S))
        calculator.button_6.grid(column = 2, row = 4, sticky = (W, N, E, S))
        calculator.mult_button.grid(column = 3, row = 4, sticky = (W, N, E, S))

    def four_row_buttons(self, calculator):
        calculator.button_1.grid(column = 0, row = 5, sticky = (W, N, E, S))
        calculator.button_2.grid(column = 1, row = 5, sticky = (W, N, E, S))
        calculator.button_3.grid(column = 2, row = 5, sticky = (W, N, E, S))
        calculator.sum_button.grid(column = 3, row = 5, sticky = (W, N, E, S))

    def five_row_buttons(self, calculator):
        calculator.button_0.grid(row = 6, column = 0, columnspan = 2, sticky = (W, N, E, S))
        calculator.point_button.grid(row = 6, column = 2, sticky = (W, N, E, S))
        calculator.rest_button.grid(row = 6,column = 3, sticky = (W, N, E, S))
        calculator.resoult_button.grid(row = 7, column = 0, columnspan = 3, sticky = (W, N, E, S))
        calculator.square_root_button.grid(row = 7, column = 3 , sticky = (W, N, E, S))