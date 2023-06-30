class Operation:
    def __init__(self):
        self.cont = 0
        self.point_cont = 0

    def inactive_button_operation(self, boton_suma, boton_resta, boton_multiplicacion, boton_division, boton_raiz_cuadrada):
        boton_suma.config(state = "disabled")
        boton_resta.config(state = "disabled")
        boton_multiplicacion.config(state = "disabled")
        boton_division.config(state = "disabled")
        boton_raiz_cuadrada.config(state = "disaled")

    def operation_button(self, boton_suma, boton_resta, boton_multiplicacion, boton_division):
        boton_suma.config(state = "Normal")
        boton_resta.config(state = "Normal")
        boton_multiplicacion.config(state = "Normal")
        boton_division.config(state = "Normal")

    def insert_values(self, tecla, entrada_1, entrada_2, boton_suma, boton_resta, boton_multiplicacion, boton_division, boton_raiz_cuadrada, boton_punto, boton_resultado):
        boton_punto.config(state = "Normal")
        boton_resultado.config(state = "Normal")
        if tecla.isdigit():
            self.cont += 1

        if self.cont >= 1 or tecla == "(" or tecla == ")":
            self.operation_button(boton_suma, boton_resta, boton_multiplicacion, boton_division)
            boton_raiz_cuadrada.config(state = "Normal")
            entrada_2.set(entrada_2.get() + tecla)

        for point in range(0, len(entrada_2.get())):
            if entrada_2.get()[point] == ".":
                self.point_cont += 1
        if self.point_cont == 1:
            self.inactive_button_operation(boton_suma, boton_resta, boton_multiplicacion, boton_division, boton_raiz_cuadrada)
            boton_punto.config(state = "disabled")
        self.point_cont = 0
        self.cont = 0 
        if tecla == ".":
            entrada_2.set(entrada_2.get() + tecla)
            boton_punto.config(state = "disabled")
            self.inactive_button_operation(boton_suma, boton_resta, boton_multiplicacion, boton_division, boton_raiz_cuadrada)
        
        if tecla == "*" or tecla == "/" or tecla == "+" or tecla == "-":
            boton_resultado.config(state = "disabled")
            self.inactive_button_operation(boton_suma, boton_resta, boton_multiplicacion, boton_division, boton_raiz_cuadrada)
            if tecla == "*":
                entrada_1.set(entrada_1.get() + entrada_2.get() + "*")
            elif tecla == "/":
                entrada_1.set(entrada_1.get() + entrada_2.get() + "/")
            elif tecla == "+":
                entrada_1.set(entrada_1.get() + entrada_2.get() + "+")
            elif tecla == "-":
                entrada_1.set(entrada_1.get() + entrada_2.get() + "-")
            entrada_2.set('')
