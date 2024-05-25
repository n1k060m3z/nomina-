class Empleado:
    def __init__(self, nombres, apellidos, cargo, salario):
        self.nombres = nombres
        self.apellidos = apellidos
        self.cargo = cargo
        self.salario = salario

    def calcular_salario(self):
        return self.salario
