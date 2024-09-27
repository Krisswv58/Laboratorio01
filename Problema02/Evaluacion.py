from datetime import datetime
from typing import List,Union

from Problema02.PreguntasCerradas import PreguntasCerradas


class Evaluacion:

  __nombreProfesor= ''
  __nombreCurso = ''
  __periodo = ''
  __InstrumentoEvaluacion = ''
  __respuestas = ''
  __año = 0
  --fecha = datetime


def __init__(self, __nombreProfesor: str, __nombrecurso: str, __año: int, __periodo: str,__InstrumentoEvaluacion: str,__respuestas: str,__fecha: datetime):
    self.nombreProfesor = __nombreProfesor
    self.nombreCurso = __nombrecurso
    self.año = __año
    self.periodo = __periodo
    self.instrumentoEvaluacion = __InstrumentoEvaluacion
    self.respuestas: List[Union[int, str]]
    self.fecha = datetime.now()

def getnombreProfesor(self):
    return self.__nombreProfesor
def setnombreProfesor(self,nombreProfesor):
   self.__nombreProfesor = nombreProfesor

def getnombreCurso(self):
    return self.__nombreCurso
def setnombreCurso(self,nombreCurso):
   self.__nombreCurso = nombreCurso

def getperiodo(self):
    return self.__periodo
def setperiodo(self,periodo):
    self.__periodo = periodo

def getInstrumentoEvaluacion(self):
        return self.__InstrumentoEvaluacion
def setInstrumentoEvaluacion(self,InstrumentoEvaluacion):
        self.__InstrumentoEvaluacion = InstrumentoEvaluacion

def getrespuestas(self):
    return self.__respuestas
def setrespuestas(self,respuestas):
    self.__respuestas = respuestas

def responder_preguntas(self,indice: int,respuestas: Union[int,str]):
    if 0 <= indice < len(self.instrumentoEvaluacion.preguntas):
        pregunta = self.instrumentoEvaluacion.preguntas[indice]
        if isinstance(pregunta,PreguntasCerradas):
            if pregunta.validar_respuesta(respuestas):
                self.respuestas.append(respuestas)
            else:
                raise ValueError('Respuesta inavalida ')
        else:
            self.respuestas.append(respuestas)

def calcular_puntuacion(self) -> float:
    puntuacion_total = 0
    total_preguntas = 0

    for i, preguntas in enumerate(self.instrumentoEvaluacion.preguntas):
        if isinstance(preguntas,PreguntasCerradas) and i < len(self.respuestas):
          puntuacion_total += preguntas.valores[self.respuestas[i]]
          total_preguntas += 1
          return puntuacion_total / total_preguntas if total_preguntas > 0 else 0

