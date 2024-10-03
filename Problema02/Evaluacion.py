from datetime import datetime
from typing import List, Union
from Problema02.InstrumentoEvaluacion import InstrumentoEvaluacion
from Problema02.PreguntasCerradas import PreguntasCerradas

class Evaluacion:
    def __init__(self, nombre_profesor: str, nombre_curso: str, año: int, periodo: str):
        self.nombre_profesor = nombre_profesor
        self.nombre_curso = nombre_curso
        self.año = año
        self.periodo = periodo
        self.instrumento_evaluacion = None
        self.respuestas: List[Union[int, str]] = []
        self.fecha = datetime.now()

    def responder_pregunta(self, indice: int, respuesta: Union[int, str]):
        if self.instrumento_evaluacion and 0 <= indice < len(self.instrumento_evaluacion.preguntas):
            pregunta = self.instrumento_evaluacion.preguntas[indice]
            if isinstance(pregunta, PreguntasCerradas):
                if pregunta.validar_respuesta(respuesta):
                    self.respuestas.append(respuesta)
                else:
                    raise ValueError('Respuesta inválida')
            else:
                self.respuestas.append(respuesta)

    def calcular_puntuacion(self) -> float:
        if not self.instrumento_evaluacion:
            return 0
        puntuacion_total = 0
        total_preguntas = 0
        for i, pregunta in enumerate(self.instrumento_evaluacion.preguntas):
            if isinstance(pregunta, PreguntasCerradas) and i < len(self.respuestas):
                puntuacion_total += pregunta.valores[self.respuestas[i]]
                total_preguntas += 1
        return puntuacion_total / total_preguntas if total_preguntas > 0 else 0

