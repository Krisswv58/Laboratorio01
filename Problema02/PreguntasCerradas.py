from optparse import Values
from typing import List
import locale

from Problema02.Preguntas import Preguntas

locale.setlocale(locale.LC_ALL, "es")
class PreguntasCerradas(Preguntas):

    __texto = ''
    __categoria = ''
    __opciones = ''
    __valores = ''

    def __init__(self,__texto: str,__categoria:str, __opciones:List[str],__valores: List[str]):
        super().__init__(__texto,__categoria)
        if len(__opciones) != len(__valores):
            raise ValueError("Las opciones y los valores deben de tener la misma longitud")
        self.__opciones = __opciones
        self.__valores = __valores


    def validar_respuesta(self,respuesta: int) -> bool:
        return 0 <= respuesta < len(self.__opciones)


def mostrar(self):
    super().mostrar()
    for i, opcion in enumerate(self.opciones):
        print(f"  {i + 1}. {opcion}")