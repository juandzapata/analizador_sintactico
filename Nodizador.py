from Arbol import Arbol
from Gramatica import Gramatica
from Nodo import Nodo


class Nodizador:
    def __init__(self, gramatica: Gramatica):
        self.gramatica = gramatica
        self.arbol: Arbol = Arbol(self.gramatica.inicial)
    
    def crearArbol(self):
        for produccion in self.gramatica.producciones:
            if produccion.nombre == self.arbol.raiz.valor:
                for valor in produccion.valores:
                    self.arbol.agregar(valor)
            else:
                banderaIzquierda = False
                banderaDerecha = False
                for letra in self.arbol.raiz.izquierda.valor:
                    if produccion.nombre == letra:
                        banderaIzquierda = True
                for letra in self.arbol.raiz.derecha.valor:
                    if produccion.nombre == letra:
                        banderaDerecha = True
                
                if banderaIzquierda:
                    print("Se encontró " + produccion.nombre + " en: " + self.arbol.raiz.izquierda.valor)
                    for valor in produccion.valores:
                        self.arbol.agregarAbajo(valor, self.arbol.raiz.izquierda)
                elif banderaDerecha:
                    print("Se encontró " + produccion.nombre + " en: " + self.arbol.raiz.izquierda.valor)
                    for valor in produccion.valores:
                        self.arbol.agregarAbajo(valor, self.arbol.raiz.derecha)

                        
    def mostrarArbol(self):
        self.arbol.preorden()

        
        
        
