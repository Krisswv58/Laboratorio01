from gettext import textdomain

class Preguntas:

    __texto = ''
    __categoria = ''

def __init__(self, __texto: str, __categoria: str):
    self.__texto = __texto
    self.__categoria = __categoria

def gettexto(self):
    return self.__texto
def settexto(self,texto):
    self.__texto = texto

def getcategoria(self):
    return self.__categoria
def setcategoria(self,categoria):
    self.__categoria = categoria

def mostrar(self):
    print(f"Pregunta: {self.texto}")
