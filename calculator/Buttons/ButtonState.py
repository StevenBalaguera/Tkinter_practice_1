from tkinter import *

class ButtonState:
    def __init__(self, calculator):
        self.calculator = calculator

    def inactive_buttons(self):
        self.inactive_button_operation()
        self.calculator.button_0.config(state = "disabled")
        self.calculator.button_1.config(state = "disabled")        
        self.calculator.button_2.config(state = "disabled")
        self.calculator.button_3.config(state = "disabled")
        self.calculator.button_4.config(state = "disabled")
        self.calculator.button_5.config(state = "disabled")
        self.calculator.button_6.config(state = "disabled")
        self.calculator.button_7.config(state = "disabled")
        self.calculator.button_8.config(state = "disabled")
        self.calculator.button_9.config(state = "disabled")
        self.calculator.del_button.config(state = "disabled")
        self.calculator.resoult_button.config(state = "disabled")
        self.calculator.bracket_button_1.config(state = "disabled")
        self.calculator.bracket_button_2.config(state = "disabled")
        self.calculator.point_button.config(state = "disabled")
        self.calculator.rest_button.config(state = "disabled")

    def active_buttons(self):
        self.operation_button()
        self.calculator.button_0.config(state = "Normal")
        self.calculator.button_1.config(state = "Normal")        
        self.calculator.button_2.config(state = "Normal")
        self.calculator.button_3.config(state = "Normal")
        self.calculator.button_4.config(state = "Normal")
        self.calculator.button_5.config(state = "Normal")
        self.calculator.button_6.config(state = "Normal")
        self.calculator.button_7.config(state = "Normal")
        self.calculator.button_8.config(state = "Normal")
        self.calculator.button_9.config(state = "Normal")
        self.calculator.del_button.config(state = "Normal")
        self.calculator.resoult_button.config(state = "Normal")
        self.calculator.bracket_button_1.config(state = "Normal")
        self.calculator.bracket_button_2.config(state = "Normal")
        self.calculator.point_button.config(state = "Normal")
        self.calculator.rest_button.config(state = "Normal")

    def inactive_button_operation(self):
        self.calculator.sum_button.config(state = "disabled")
        self.calculator.mult_button.config(state = "disabled")
        self.calculator.divition_button.config(state = "disabled")
        self.calculator.square_root_button.config(state = "disabled")
  
    def operation_button(self):
        self.calculator.sum_button.config(state = "Normal")
        self.calculator.rest_button.config(state = "Normal")
        self.calculator.mult_button.config(state = "Normal")
        self.calculator.divition_button.config(state = "Normal")

    def inactive_point_button(self):
        self.calculator.point_button.config(state = "disabled")

    def point_button(self):
        self.calculator.point_button.config(state = "Normal")

    def resoult_button_disabled(self):
        self.calculator.resoult_button.config(state = "disabled")

    def resoult_button(self):
        self.calculator.resoult_button.config(state = "Normal")     
    
    def inactive_square_root(self):
        self.calculator.square_root_button.config(state = "disabled")

    def inactive_rest_button(self):
        self.calculator.rest_button.config(state = "disabled")

    def active_rest_button(self):
        self.calculator.rest_button.config(state = "Normal")

    def active_square_root_button(self):
        self.calculator.square_root_button.config(state = "Normal")

    def inactive_open_brackets(self):
        self.calculator.bracket_button_1.config(state = "disabled")

    def inactive_closed_brackets(self):
        self.calculator.bracket_button_2.config(state = "disabled")

    def active_open_brackets(self):
        self.calculator.bracket_button_1.config(state = "Normal")

    def active_closed_brackets(self):
      self.calculator.bracket_button_2.config(state = "Normal")  
        

