from typing import List
from Problema02.Preguntas import Preguntas

class PreguntasCerradas(Preguntas):
    def __init__(self, texto: str, categoria: str, opciones: List[str], valores: List[int]):
        super().__init__(texto, categoria)
        if len(opciones) != len(valores):
            raise ValueError("Las opciones y los valores deben tener la misma longitud")
        self.opciones = opciones
        self.valores = valores

    def validar_respuesta(self, respuesta: int) -> bool:
        return 0 <= respuesta < len(self.opciones)

    def mostrar(self):
        super().mostrar()
        for i, opcion in enumerate(self.opciones):
            print(f"  {i + 1}. {opcion}")