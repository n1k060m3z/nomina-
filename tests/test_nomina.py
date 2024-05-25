import unittest
import sys
import os

# Agrega la ruta del proyecto al sys.path para importar módulos correctamente
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from departamento import Departamento
from gerente import Gerente
from empleado import Empleado

class TestEmpresa(unittest.TestCase):

    def test_depto_calcular_nomina(self):
        dpto = Departamento('A', Gerente('gA', 'gA', 100), [
            Empleado('a0', 'a0', 'a0', 1),
            Empleado('a1', 'a1', 'a1', 1),
        ])
        self.assertEqual(dpto.calcular_nomina(), 102, "Incorrecto! nómina del departamento")

if __name__ == '__main__':
    unittest.main()
