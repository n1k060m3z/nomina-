from empleado import Empleado

class Gerente(Empleado):
    def __init__(self, nombres, apellidos, salario):
        super().__init__(nombres, apellidos, "Gerente", salario)

    def calcular_salario(self):
        return self.salario
