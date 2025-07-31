# Importamos la librería tkinter para crear interfaces gráficas
import tkinter as tk
from Logica import sumar, restar, multiplicar, dividir
from Logica import NumeroNegativoError

# Definimos una clase llamada 'Calculadora'
class Calculadora:
    def __init__(self, ventana):  # <-- recibe la ventana
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
        # Posicionamos el campo de entrada en la primera fila (row=0), ocupando 4 columnas
        self.entrada.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        # Variable para guardar la operación actual (aunque en esta versión no la usamos mucho)
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
        for btn in botones:
            texto = btn[0]
            fila = btn[1]
            columna = btn[2]
            ancho = btn[3] if len(btn) == 4 else 1

            # Creamos el botón con estilo oscuro
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
                command=lambda t=texto: self.pulsar_boton(t)
            )
            b.grid(row=fila, column=columna, columnspan=ancho, padx=2, pady=2)

    # Método que se ejecuta cuando se presiona un botón
    def pulsar_boton(self, valor):
        if valor == "C":
            # Limpiar entrada
            self.entrada.delete(0, tk.END)
            self.operacion = ""
        elif valor == "=":
            try:
                expresion = self.entrada.get()
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
                    raise ValueError("Operación no válida")

                self.entrada.delete(0, tk.END)
                self.entrada.insert(tk.END, resultado)

            except NumeroNegativoError:
                self.entrada.delete(0, tk.END)
                self.entrada.insert(tk.END, "Negativos NO")

            except ZeroDivisionError:
                self.entrada.delete(0, tk.END)
                self.entrada.insert(tk.END, "Div entre 0")

            except Exception:
                self.entrada.delete(0, tk.END)
                self.entrada.insert(tk.END, "Error")
        else:
            # Agregar el carácter a la entrada
            self.entrada.insert(tk.END, valor)