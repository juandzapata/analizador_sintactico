from Gramatica import Gramatica
from Nodo import Nodo

class Nodizador():
    def __init__(self, gramatica: Gramatica):
        self.gramatica = gramatica
        self.nodos = []
        self.ultimo = None
    
    def convertirANodos(self):
        for produccion in self.gramatica.producciones:
            self.agregarNodo(produccion.nombre)
            for nodo in self.nodos:
                if nodo.valor == produccion.nombre:
                    for valor in produccion.valores:
                        nodo.agregarHijo(Nodo(valor))               

    def agregarNodo(self, valor):
        nodo = Nodo(valor)
        self.nodos.append(nodo)
        self.ultimo = nodo
    
    #def generarPalabras(self, nodo: Nodo):
        
    
    def mostrarNodos(self):
        for nodo in self.nodos:
            print(nodo)
            for hijo in nodo.hijos:
                print("  ", hijo)