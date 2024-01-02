class _Nodo:
    def __init__(self, dato, prox=None):
        self.dato = dato
        self.prox = prox

class Pila:
    """Representa una pila con operaciones de apilar, desapilar y verificar si está vacía, para ir acumulando los trazos que realiza el usuario en el dibujo,
    para cuando el usuario quieda retroceder pueda hacerlo, y lo mismo para cuando quiera rehacer un trazo borrado"""
    def __init__(self):
        self.tope = None

    def apilar(self, dato):
        nodo = _Nodo(dato, self.tope)
        self.tope = nodo

    def desapilar(self):
        if self.esta_vacia():
            raise ValueError
        dato = self.tope.dato
        self.tope = self.tope.prox
        return dato

    def ver_tope(self):
        if self.esta_vacia():
            raise ValueError
        return self.tope.dato

    def esta_vacia(self):
        return self.tope is None