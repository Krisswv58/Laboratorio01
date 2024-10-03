from typing import List, Union
from Problema02.PreguntaAbierta import PreguntaAbierta
from Problema02.PreguntasCerradas import PreguntasCerradas

class InstrumentoEvaluacion:
    def __init__(self):
        self.preguntas: List[Union[PreguntasCerradas, PreguntaAbierta]] = []

    def agregar_pregunta(self, pregunta: Union[PreguntasCerradas, PreguntaAbierta]):
        self.preguntas.append(pregunta)

    def eliminar_pregunta(self, indice: int):
        if 0 <= indice < len(self.preguntas):
            del self.preguntas[indice]

