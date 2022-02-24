from math import pi 
import unittest
from formas import Circulo, Cuadrado, Forma, RadioError

class Test_formas(unittest.TestCase):

    def test_existencia(self):
        f = Forma()
        self.assertIsNotNone(f)
    
    def test_nombre_forma(self):
        f = Forma()
        self.assertEqual(f.__str__(),'Forma')

class Test_Circulo(unittest.TestCase):

    def test_existencia(self):
        c = Circulo(1)
        self.assertIsNotNone(c)

    def test_circulo_radio1_perimetro_2pi(self):
        c = Circulo(1)
        peri = c.perimetro()
        self.assertEqual(peri,2*pi)

    def test_radio_negativo_da_error(self):
        with self.assertRaises(RadioError):
            c = Circulo(-1)
            peri = c.perimetro()

class Test_Rectangulo(unittest.TestCase):

    def test_existencia(self):
        pass


class Test_Cuadrado(unittest.TestCase):

    def test_lado_1_perimetro_4(self):
        c = Cuadrado(1)
        peri = c.perimetro()
        self.assertEqual(peri,4)

    def test_area_lado_1__1(self):
        c = Cuadrado(1)
        a = c.area()
        self.assertEqual(a,1)

     