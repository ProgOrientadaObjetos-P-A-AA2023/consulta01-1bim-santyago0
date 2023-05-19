"""

"""
from mis_clases import PromedioNota

# Crear dos objetos de la clase 02

# objeto 01

# crear
pro = PromedioNota("Santiago Riofrío", 9.55, 8.25, 9.1)
pro.calcularPromedio()

# Presentar objeto; usar el método __st__
cadena = str(pro)
print(cadena)

# objeto 02

# crear ingresando valores por teclado
nombre = input("Ingrese su nombre: ")
nota1 = float(input("Ingrese la primera nota: "))
nota2 = float(input("Ingrese la segunda nota: "))
nota3 = float(input("Ingrese la tercera nota: "))
pro2 = PromedioNota(nombre, nota1, nota2, nota3)
pro2.calcularPromedio()

# Presentar objeto; usar el método __st__
cadena = str(pro2)
print("\n"+cadena)
