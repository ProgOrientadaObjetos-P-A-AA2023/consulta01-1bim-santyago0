"""

"""
from mis_clases import FacturaTelefonica

# Crear dos objetos de la clase 01

# objeto 01

# crear
fac = FacturaTelefonica("Santiago Riofrío", "0982447695", 20, 0.25)
fac.calcularValor_factura()

# Presentar objeto; usar el método __st__
cadena = str(fac)
print(cadena)

# objeto 02

# crear ingresando valores por teclado
nombre = input("Ingrese su nombre: ")
telefono = input("Ingrese su teléfono: ")
minutos = float(input("Ingrese los minutos consumidos: "))
valor_minuto = float(input("Ingrese el valor por minuto: "))

fac2 = FacturaTelefonica(nombre, telefono, minutos, valor_minuto)
fac2.calcularValor_factura()

# Presentar objeto; usar el método __st__
cadena = str(fac2)
print("\n"+cadena)
