from Problema02.Preguntas import Preguntas

class PreguntaAbierta(Preguntas):
    def __init__(self, texto: str, categoria: str):
        super().__init__(texto, categoria)
