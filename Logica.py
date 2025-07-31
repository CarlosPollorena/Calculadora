# Importamos una excepción personalizada llamada NumeroNegativoError desde el archivo excepciones.py 
from excepciones import NumeroNegativoError

# Función auxiliar que valida si los números recibidos son negativos
def validar_numeros(*args):  # *args permite pasar múltiples argumentos a la función
    for num in args:  # Recorremos cada número recibido
        if float(num) < 0:  # Convertimos a float y verificamos si es negativo
            raise NumeroNegativoError()  # Si es negativo, lanzamos una excepción personalizada

# Función que realiza una suma
def sumar(a, b):
    validar_numeros(a, b)  # Validamos que ambos números no sean negativos
    return float(a) + float(b)  # Convertimos a float por seguridad y devolvemos el resultado

# Función que realiza una resta
def restar(a, b):
    validar_numeros(a, b)  # Validamos que ambos números no sean negativos
    return float(a) - float(b)  # Realizamos la resta y devolvemos el resultado

# Función que realiza una multiplicación
def multiplicar(a, b):
    validar_numeros(a, b)  # Validamos que ambos números no sean negativos
    return float(a) * float(b)  # Realizamos la multiplicación y devolvemos el resultado

# Función que realiza una división
def dividir(a, b):
    validar_numeros(a, b)  # Validamos que ambos números no sean negativos
    if float(b) == 0:  # Verificamos que el divisor no sea cero
        raise ZeroDivisionError("No se puede dividir entre 0.")  # Si lo es, lanzamos un error estándar
    return float(a) / float(b)  # Realizamos la división y devolvemos el resultado
