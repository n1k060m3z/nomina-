from departamento import Departamento
from rich import print

class Empresa:
    def __init__(self, nombre, departamentos):
        self.nombre = nombre
        self.departamentos = departamentos

    def calcular_nomina(self):
        total_nomina = sum(departamento.calcular_nomina() for departamento in self.departamentos)
        return total_nomina

    def mostrar(self):
        print(f"[bold red]Empresa: {self.nombre}[/bold red]")
        for departamento in self.departamentos:
            departamento.mostrar()
        print(f"\n[bold green]{self.calcular_nomina():,}[/bold green]")
