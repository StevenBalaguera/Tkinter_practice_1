from tkinter import *

class GridButtons:
    def __init__(self, calculator):
        self.calculator = calculator
    
    def firts_row_buttons(self):
        self.calculator.bracket_button_1.grid(row = 2, column = 0, sticky = (W,N,E,S))
        self.calculator.bracket_button_2.grid(row = 2, column = 1, sticky = (W,N,E,S))
        self.calculator.del_all_button.grid(row = 2, column = 2, sticky = (W,N,E,S))
        self.calculator.del_button.grid(row = 2, column = 3, sticky = (W,N,E,S))

    def second_row_buttons(self):
        self.calculator.button_7.grid(column = 0, row = 3, sticky = (W, N, E, S))
        self.calculator.button_8.grid(column = 1, row = 3, sticky = (W, N, E, S))
        self.calculator.button_9.grid(column = 2, row = 3, sticky = (W, N, E, S))
        self.calculator.divition_button.grid(column = 3, row = 3, sticky = (W, N, E, S))

    def third_row_buttons(self):
        self.calculator.button_4.grid(column = 0, row = 4, sticky = (W, N, E, S))
        self.calculator.button_5.grid(column = 1, row = 4, sticky = (W, N, E, S))
        self.calculator.button_6.grid(column = 2, row = 4, sticky = (W, N, E, S))
        self.calculator.mult_button.grid(column = 3, row = 4, sticky = (W, N, E, S))

    def four_row_buttons(self):
        self.calculator.button_1.grid(column = 0, row = 5, sticky = (W, N, E, S))
        self.calculator.button_2.grid(column = 1, row = 5, sticky = (W, N, E, S))
        self.calculator.button_3.grid(column = 2, row = 5, sticky = (W, N, E, S))
        self.calculator.sum_button.grid(column = 3, row = 5, sticky = (W, N, E, S))

    def five_row_buttons(self):
        self.calculator.button_0.grid(row = 6, column = 0, columnspan = 2, sticky = (W, N, E, S))
        self.calculator.point_button.grid(row = 6, column = 2, sticky = (W, N, E, S))
        self.calculator.rest_button.grid(row = 6,column = 3, sticky = (W, N, E, S))
        self.calculator.resoult_button.grid(row = 7, column = 0, columnspan = 3, sticky = (W, N, E, S))
        self.calculator.square_root_button.grid(row = 7, column = 3 , sticky = (W, N, E, S))