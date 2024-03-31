from collections import defaultdict
from Produccion import Produccion


class Gramatica():
    def __init__(self, terminales: list, noTerminales: list, producciones: list[Produccion], inicial: str):
        self.terminales = terminales
        self.noTerminales = noTerminales
        self.producciones = producciones
        self.inicial = inicial
    
    def determinarRecursion(self) -> bool:
        for produccion in self.producciones:
            indice = len(produccion.nombre)
            for valor in produccion.valores:
                if len(valor) >= indice:
                    if valor[:indice] == produccion.nombre:
                        self.eliminarRecursion(produccion)

    
    def eliminarRecursion(self, produccion: Produccion):
        if len(produccion.valores) >= 1:
            beta = produccion.valores[1]
        else:
            beta = ""
        alpha = produccion.valores[0][len(produccion.nombre)+1:]
        nuevoValor = [beta + produccion.nombre + "'"]
        posicionProduccion = self.posicionProduccion(produccion.nombre)
        self.producciones[posicionProduccion].setValores(nuevoValor)
        nuevaProduccion = Produccion(produccion.nombre + "'", [alpha + produccion.nombre + "'", "λ"])
        self.producciones.append(nuevaProduccion)

    def posicionProduccion(self, nombre: str) -> int:
        for i in range(len(self.producciones)):
            if self.producciones[i].nombre == nombre:
                return i
        return -1
    
    def mostrarProducciones(self):
        for produccion in self.producciones:
            print(produccion.nombre, " -> ", " | ".join(produccion.valores))


    def es_terminal(self, simbolo: str) -> bool:
        return simbolo in self.terminales

    def es_no_terminal(self, simbolo: str) -> bool:
        return simbolo in self.noTerminales