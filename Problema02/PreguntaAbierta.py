from Problema02.Preguntas import Preguntas


class PreguntaAbierta(Preguntas):

    __texto = ''
    --categoria = ''

def __init__(self,__texto:str, __categoria:str):
    super().__init__(__texto,__categoria)

