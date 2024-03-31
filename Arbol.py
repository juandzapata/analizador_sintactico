from Nodo import Nodo

class Arbol:

    def __init__(self, dato):
        self.raiz = Nodo(dato)

    def agregar(self, dato):
        self.__agregar_recursivo(self.raiz, dato)
    
    def agregarAbajo(self, dato, nodo):
        self.__agregar_recursivo(nodo, dato)
    
    def __agregar_recursivo(self, nodo, dato):
        if nodo.izquierda is None and nodo.derecha is None:
            nodo.izquierda = Nodo(dato)
        elif nodo.izquierda is not None and nodo.derecha is None:
            nodo.derecha = Nodo(dato)

    def __preorden_recursivo(self, nodo: Nodo):
        if nodo is not None:
            print(nodo.valor, end=", ")
            self.__preorden_recursivo(nodo.izquierda)
            self.__preorden_recursivo(nodo.derecha)
    
    def preorden(self):
        print("Imprimiendo árbol preorden: ")
        self.__preorden_recursivo(self.raiz)
        print("")
    
    def __buscar(self, nodo, busqueda):
        if nodo is None:
            return None
        if nodo.valor == busqueda:
            return nodo
        if busqueda < nodo.valor:
            return self.__buscar(nodo.izquierda, busqueda)
        else:
            return self.__buscar(nodo.derecha, busqueda)
    
    def buscar(self, busqueda):
        return self.__buscar(self.raiz, busqueda)