class Preguntas:
    def __init__(self, texto: str, categoria: str):
        self._texto = texto
        self._categoria = categoria

    @property
    def texto(self):
        return self._texto

    @texto.setter
    def texto(self, valor):
        self._texto = valor

    @property
    def categoria(self):
        return self._categoria

    @categoria.setter
    def categoria(self, valor):
        self._categoria = valor

    def mostrar(self):
        print(f"Pregunta: {self.texto}")
