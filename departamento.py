from gerente import Gerente
from empleado import Empleado
from rich import print
class Departamento:
    def __init__(self, nombre, gerente: Gerente, empleados=None):
        self.nombre = nombre
        self.gerente = gerente
        self.empleados = empleados if empleados is not None else []

    def agregar_empleado(self, empleado: Empleado):
        self.empleados.append(empleado)

    def agregar_empleados(self, empleados: list):
        self.empleados.extend(empleados)

    def calcular_nomina(self):
        total_nomina = self.gerente.calcular_salario() + sum(empleado.calcular_salario() for empleado in self.empleados)
        return total_nomina

    def mostrar(self):
        
        print(f"[bold yellow]- {self.nombre}[/bold yellow] : [bold green]${self.calcular_nomina():,}[/bold green]")
