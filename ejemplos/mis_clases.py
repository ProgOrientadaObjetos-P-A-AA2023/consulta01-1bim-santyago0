"""

"""

# Crear dos clases en Python
# Usted defina el nombre y los atributos
# Puede usar las mismas clases usadas en Java en los ejemplos estudiados

# clase 01
class FacturaTelefonica:
    pass
    def __init__(self, nombre_cliente, numero_telefono, minutos_mes,
                 valor_minuto):
        self.nombre_cliente = nombre_cliente
        self.numero_telefono = numero_telefono
        self.minutos_mes = minutos_mes
        self.valor_minuto = valor_minuto

    def establecerNombre_cliente(self, x):
        self.nombre_cliente = x

    def establecerNumero_telefono(self, x):
        self.numero_telefono = x

    def establecerMinutos_mes(self, x):
        self.minutos_mes = x

    def establecerValor_minuto(self, x):
        self.valor_minuto = x

    def calcularValor_factura(self):
        self.valor_factura = self.minutos_mes * self.valor_minuto

    def obtenerNombre_cliente(self):
        return self.nombre_cliente

    def obtenerNumero_telefono(self):
        return self.numero_telefono

    def obtenerMinutos_mes(self):
        return self.minutos_mes

    def obtenerValor_minuto(self):
        return self.valor_minuto

    def obtenerValor_factura(self):
        return self.valor_factura

    def __str__(self):
        return f"""Factura telefónica del cliente {self.nombre_cliente}:
Número: {self.numero_telefono}
Minutos consumidos en el mes:{self.minutos_mes}
Valor del minuto: ${self.valor_minuto}
Valor de la factura: ${self.valor_factura}\n"""


# clase 02
class PromedioNota:
    pass
    def __init__(self, nombre_estudiante, nota1, nota2, nota3):
        self.nombre_estudiante = nombre_estudiante
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3

    def establecerNombre_estudiante(self, x):
        self.nombre_estudiante = x

    def establecerNota1(self, x):
        self.nota1 = x

    def establecerNota2(self, x):
        self.nota2 = x

    def establecerNota3(self, x):
        self.nota3 = x

    def calcularPromedio(self):
        self.promedio = (self.nota1 + self.nota2 + self.nota3)/3

    def obtenerNombre_estudiante(self):
        return self.nombre_estudiante

    def obtenerNota1(self):
        return self.nota1

    def obtenerNota2(self):
        return self.nota2

    def obtenerNota3(self):
        return self.nota3

    def obtenerPromedio(self):
        return self.promedio

    def __str__(self):
        return f"""Promedio de notas del estudiante: {self.nombre_estudiante}:
Nota materia 1: {self.nota1}
Nota materia 2: {self.nota2}
Nota materia 3: {self.nota3}
Promedio: {self.promedio}\n"""
