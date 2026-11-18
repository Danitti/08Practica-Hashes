"""Ejercicio 3: trie de a..z, basado en 06_trie_resuelta.cpp.

Completar insertar, _bajar, buscar, empieza_por y _recoger, en ese orden.
Las palabras y consultas tienen longitud como máximo 100.
"""


class Nodo:
    def __init__(self):
        self.hijos = {}
        self.fin_de_palabra = False


class Trie:
    def __init__(self):
        self.raiz = Nodo()
        self._nodos = 1

    @staticmethod
    def _valida(cadena):
        return all('a' <= c <= 'z' for c in cadena)

    def nodos(self):
        return self._nodos

    def insertar(self, palabra):
        """Conjunto: repetir una palabra no crea nodos ni duplicados.

        Se permite ''. Si contiene algo fuera de a..z, ValueError sin cambios.
        Tiempo O(?); nodos nuevos como máximo O(?).
        """
        if not self._valida(palabra):
            raise ValueError("Solo se admiten letras a..z")
        
        actual = self.raiz
        
        
        for caracter in palabra:
            if caracter not in actual.hijos:
                nuevo = Nodo()
                actual.hijos[caracter] = nuevo
                self._nodos += 1
                
            actual = actual.hijos[caracter]
        
        actual.fin_de_palabra = True
                
                

    def _bajar(self, cadena):
        """Nodo del prefijo o None. No insertar ni modificar nada. O(?)."""
        if not self._valida(cadena):
            return None
        
        actual = self.raiz
        
        for caracter in cadena:
            if caracter not in actual.hijos:
                return None
            
            actual = actual.hijos[caracter]
        
        return actual

    def buscar(self, palabra):
        """True solo si es una palabra insertada, no un mero prefijo. O(?)."""
        
        nodo_final = self._bajar(palabra)
        
        if nodo_final is None:
            return False
        
        if nodo_final.fin_de_palabra:
            return True
        else:
            return False

    def empieza_por(self, prefijo):
        """True si existe ese camino. '' -> True, incluso en trie vacío. O(?)."""
        if prefijo == '':
            return True
        
        if self.raiz is None:
            return True
        
        nodo_final = self._bajar(prefijo)
        
        if nodo_final is not None:
            return True
        
        return False

    def autocompletar(self, prefijo):
        """Dado: devuelve palabras únicas en orden alfabético; no modifica trie.

        Prefijo ausente/inválido -> []; '' -> todas las palabras.
        Completar su coste en RESPUESTAS, contando las cadenas de salida.
        """
        nodo = self._bajar(prefijo)
        salida = []
        if nodo is not None:
            camino = list(prefijo)
            self._recoger(nodo, camino, salida)
        return salida

    @staticmethod
    def _recoger(nodo: Nodo, camino: list[str], salida: list[str]):
        """Preorden: camino es lista de letras; restaurarla antes de volver.

        Añadir una COPIA de la palabra si es terminal; recorrer hijos en orden.
        No ordenar la salida al final. Se puede usar sorted(nodo.hijos).
        """
        
        if nodo.fin_de_palabra:
            salida.append("".join(camino))
            
        for letra, nodo_hijo in sorted(nodo.hijos.items()):
            if nodo_hijo is not None:
                camino.append(letra)
                Trie._recoger(nodo_hijo, camino, salida)
                camino.pop()
        
                
        