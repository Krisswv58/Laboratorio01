from typing import List
from Problema02.Evaluacion import Evaluacion
from Problema02.InstrumentoEvaluacion import InstrumentoEvaluacion
from Problema02.PreguntasCerradas import PreguntasCerradas
from Problema02.PreguntaAbierta import PreguntaAbierta

class SistemaEvaluacion:
    def __init__(self):
        self.evaluaciones: List[Evaluacion] = []
        self.profesores = ["Juan Pérez", "María González", "Carlos Rodríguez"]
        self.cursos = ["Matemáticas", "Literatura", "Física"]

    def agregar_evaluacion(self, evaluacion: Evaluacion):
        self.evaluaciones.append(evaluacion)

    def obtener_rendimiento(self, nombre_profesor: str, año: int, periodo: str) -> float:
        evaluaciones = [e for e in self.evaluaciones if
                        e.nombre_profesor == nombre_profesor and e.año == año and e.periodo == periodo]
        if not evaluaciones:
            return 0
        return sum(e.calcular_puntuacion() for e in evaluaciones) / len(evaluaciones)

    def imprimir_resultado_evaluacion(self, nombre_profesor: str, nombre_curso: str):
        evaluacion = next(
            (e for e in self.evaluaciones if e.nombre_profesor == nombre_profesor and e.nombre_curso == nombre_curso),
            None)
        if evaluacion:
            print(f"\nResultados de la evaluación:")
            print(f"Docente: {evaluacion.nombre_profesor}")
            print(f"Curso: {evaluacion.nombre_curso}")
            print(f"Puntuación: {evaluacion.calcular_puntuacion():.2f}")
            print("\nRespuestas a las preguntas:")
            for i, pregunta in enumerate(evaluacion.instrumento_evaluacion.preguntas):
                print(f"P: {pregunta.texto}")
                if isinstance(pregunta, PreguntasCerradas):
                    print(f"R: {pregunta.opciones[evaluacion.respuestas[i]]}")
                else:
                    print(f"R: {evaluacion.respuestas[i]}")
        else:
            print("Evaluación no encontrada.")

    def menu_principal(self):
        while True:
            print("\n--- Sistema de Evaluación ---")
            print("1. Realizar evaluación")
            print("2. Ver resultados de evaluación")
            print("3. Salir")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.realizar_evaluacion()
            elif opcion == "2":
                self.ver_resultados()
            elif opcion == "3":
                print("Gracias por usar el Sistema de Evaluación. ¡Hasta luego!")
                break
            else:
                print("Opción no válida. Por favor, intente de nuevo.")

    def realizar_evaluacion(self):
        print("\n--- Realizar Evaluación ---")
        print("Profesores disponibles:")
        for i, profesor in enumerate(self.profesores, 1):
            print(f"{i}. {profesor}")

        profesor_idx = int(input("Seleccione el número del profesor a evaluar: ")) - 1
        if profesor_idx < 0 or profesor_idx >= len(self.profesores):
            print("Selección inválida.")
            return

        nombre_profesor = self.profesores[profesor_idx]
        nombre_curso = self.cursos[profesor_idx]

        evaluacion = Evaluacion(nombre_profesor, nombre_curso, 2024, "Q3")
        instrumento = self.crear_instrumento_evaluacion()
        evaluacion.instrumento_evaluacion = instrumento

        print(f"\nEvaluando a {nombre_profesor} en el curso {nombre_curso}")
        for i, pregunta in enumerate(instrumento.preguntas):
            print(f"\n{pregunta.texto}")
            if isinstance(pregunta, PreguntasCerradas):
                for j, opcion in enumerate(pregunta.opciones):
                    print(f"{j + 1}. {opcion}")
                respuesta = int(input("Seleccione su respuesta: ")) - 1
                evaluacion.responder_pregunta(i, respuesta)
            else:
                respuesta = input("Su respuesta: ")
                evaluacion.responder_pregunta(i, respuesta)

        self.agregar_evaluacion(evaluacion)
        print("\nEvaluación completada. ¡Gracias por su participación!")

    def ver_resultados(self):
        print("\n--- Ver Resultados de Evaluación ---")
        print("Profesores disponibles:")
        for i, profesor in enumerate(self.profesores, 1):
            print(f"{i}. {profesor}")

        profesor_idx = int(input("Seleccione el número del profesor para ver resultados: ")) - 1
        if profesor_idx < 0 or profesor_idx >= len(self.profesores):
            print("Selección inválida.")
            return

        nombre_profesor = self.profesores[profesor_idx]
        nombre_curso = self.cursos[profesor_idx]
        self.imprimir_resultado_evaluacion(nombre_profesor, nombre_curso)

    def crear_instrumento_evaluacion(self):
        instrumento = InstrumentoEvaluacion()
        instrumento.agregar_pregunta(PreguntasCerradas("El profesor explica con claridad", "Profesional",
                                                       ["Muy de acuerdo", "De acuerdo", "Poco de acuerdo",
                                                        "En desacuerdo"],
                                                       [3, 2, 1, 0]))
        instrumento.agregar_pregunta(PreguntasCerradas("El profesor es puntual", "Profesional",
                                                       ["Siempre", "Usualmente", "A veces", "Nunca"],
                                                       [3, 2, 1, 0]))
        instrumento.agregar_pregunta(PreguntaAbierta("¿Qué aspectos del curso le gustaron más?", "General"))
        instrumento.agregar_pregunta(PreguntaAbierta("¿Qué sugerencias tiene para mejorar el curso?", "General"))
        return instrumento

if __name__ == "__main__":
    sistema = SistemaEvaluacion()
    sistema.menu_principal()


