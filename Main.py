# Importamos la librería tkinter para crear interfaces gráficas
import tkinter as tk
from Interfaz import Calculadora

if __name__ == "__main__":
    ventana = tk.Tk() #ventana principal 
    app = Calculadora(ventana) #crea instancia
    ventana.mainloop() #ejecuta el bucle principal de la ventana


#INTERFAZ
# Importamos las funciones basicas y la excepcion 
import tkinter as tk
from Logica import sumar, restar, multiplicar, dividir
from Logica import NumeroNegativoError

# Definimos una clase llamada 'Calculadora'
class Calculadora:
    def __init__(self, ventana):  # Guarda la ventana 
        self.ventana = ventana
        self.ventana.title("Calculadora")
        self.ventana.configure(bg="black")

        # Creamos el campo de entrada para mostrar los números y resultados
        self.entrada = tk.Entry(
            self.ventana,          # Ventana donde va colocado
            width=20,              # Ancho del campo
            font=("Arial", 18),    # Fuente y tamaño
            bd=5,                  # Borde
            relief="flat",         # Borde plano (sin relieve)
            bg="black",            # Fondo negro
            fg="white",            # Texto blanco
            insertbackground="white"  # Cursor blanco
        )
        # Posicionamos el campo de entrada en la primera fila  ocupando 4 columnas
        self.entrada.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        # Variable para guardar la operación actual 
        self.operacion = ""

        # Llamamos al método que crea los botones
        self.crear_botones()

        # Iniciamos el bucle principal de la ventana (para que se mantenga abierta)
        self.ventana.mainloop()

    # Método que crea los botones de la calculadora
    def crear_botones(self):
        # Lista de botones: (texto, fila, columna, [opcional: columnas a ocupar])
        botones = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('C', 4, 2), ('+', 4, 3),
            ('=', 5, 0, 4)  # Este botón ocupa 4 columnas
        ]

        # Creamos cada botón con sus propiedades y lo colocamos en la ventana
        #Extraer los datos de la tupla 
        for btn in botones:
            texto = btn[0]
            fila = btn[1]
            columna = btn[2]
            ancho = btn[3] if len(btn) == 4 else 1

            # Creamos el botón
            b = tk.Button(
                self.ventana,
                text=texto,
                width=5 * ancho,
                height=2,
                font=("Arial", 16),
                bg="gray15",
                fg="white",
                activebackground="gray30",
                activeforeground="white",
                command=lambda t=texto: self.pulsar_boton(t) #Cuando el botón se presiona, se llama a pulsar_boton(t) donde t es el texto del botón.
            )
            b.grid(row=fila, column=columna, columnspan=ancho, padx=2, pady=2) #Coloca el botón en la cuadrícula (grid) de la ventan

    # Método que se ejecuta cuando se presiona un botón
    def pulsar_boton(self, valor):
        if valor == "C":
            # Limpiar entrada
            self.entrada.delete(0, tk.END)
            self.operacion = ""
            #Si se presiona "=" se resuelve con validaciones y manejo de errores
        elif valor == "=":
            try:
                expresion = self.entrada.get() # Obtiene el texto de la entrada separa la cadena en dos y realiza la operacion 
                if '+' in expresion:
                    a, b = expresion.split('+')
                    resultado = str(sumar(a.strip(), b.strip()))
                elif '-' in expresion:
                    a, b = expresion.split('-')
                    resultado = str(restar(a.strip(), b.strip()))
                elif '*' in expresion:
                    a, b = expresion.split('*')
                    resultado = str(multiplicar(a.strip(), b.strip()))
                elif '/' in expresion:
                    a, b = expresion.split('/')
                    resultado = str(dividir(a.strip(), b.strip()))
                else:
                    raise ValueError("Operación no válida") #Lanza un error si la operación no tiene un operador válido.

                self.entrada.delete(0, tk.END) # Borra la expresión original
                self.entrada.insert(tk.END, resultado) # Muestra el resultado 

            except NumeroNegativoError: #muestra error si se ingresa un numero negativo
                self.entrada.delete(0, tk.END)
                self.entrada.insert(tk.END, "No Negativos")

            except ZeroDivisionError: #muestra error si se intenta dividir por cero
                self.entrada.delete(0, tk.END)
                self.entrada.insert(tk.END, "No Division entre 0")

            except Exception: # Captura cualquier otro error
                self.entrada.delete(0, tk.END)
                self.entrada.insert(tk.END, "Error")
        else:
            # Si no, solo agrega el carácter a la entrada
            self.entrada.insert(tk.END, valor)


#EXCEPCIONES
            # Definimos una nueva clase personalizada
class NumeroNegativoError(Exception):

    def __init__(self, mensaje="No se permiten números negativos."):
        # Guardamos el mensaje de error que se mostrará cuando se lance esta excepción
        self.mensaje = mensaje
    # Llamamos al constructor para inicializarla con el mensaje
        super().__init__(self.mensaje)


#LOGICA


# importamos la excepción personalizada 
from excepciones import NumeroNegativoError

# Funcion que verifica si los numeros son negativo
def validar_numeros(*args):  # *args recibe múltiples argumentos ej(5, -3, 2)
    for num in args:  # Recorremos cada número recibido
        if float(num) < 0:  # Convertimos a decimal y verificamos si es negativo
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
