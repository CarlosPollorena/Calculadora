# Definimos una nueva clase llamada NumeroNegativoError es una excepción personalizada)
class NumeroNegativoError(Exception):

    # Método constructor que se ejecuta al crear una instancia de esta excepción
    def __init__(self, mensaje="No se permiten números negativos."):
        # Guardamos el mensaje de error que se mostrará cuando se lance esta excepción
        self.mensaje = mensaje

        # Llamamos al constructor de la clase padre (Exception) pasando el mensaje como argumento
        # Esto asegura que el mensaje también sea accesible mediante los mecanismos estándar de excepciones
        super().__init__(self.mensaje)


