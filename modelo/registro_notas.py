from modelo.estudiante import Estudiante
from modelo.asignatura import Asignatura
from nota import Nota


class RegistroNotas:

    def __init__(self):
        self._estudiantes = []
        self._asignaturas = []
        self._notas = []

    def agregar_estudiante(self, matricula, nombre):
        estudiante = Estudiante(matricula, nombre)
        self._estudiantes.append(estudiante)

    def registrar_asignatura(self, codigo, nombre):
        asignatura = Asignatura(codigo, nombre)
        self._asignaturas.append(asignatura)

    agregar_asignatura = registrar_asignatura

    def buscar_estudiante(self, matricula):
        for estudiante in self._estudiantes:
            if estudiante.matricula == matricula:
                return estudiante
        return None

    def buscar_asignatura(self, codigo):
        for asignatura in self._asignaturas:
            if asignatura.codigo == codigo:
                return asignatura
        return None

    def registrar_nota(self, matricula, codigo_asignatura, calificacion):

        estudiante = self.buscar_estudiante(matricula)
        asignatura = self.buscar_asignatura(codigo_asignatura)

        if estudiante and asignatura:
            nota = Nota(estudiante, asignatura, calificacion)
            self._notas.append(nota)

    def obtener_notas_estudiante(self, matricula):

        lista = []

        for nota in self._notas:
            if nota.estudiante.matricula == matricula:
                lista.append(nota)

        return lista

    def promedio_estudiante(self, matricula):

        notas = self.obtener_notas_estudiante(matricula)

        if len(notas) == 0:
            return 0

        suma = 0

        for nota in notas:
            suma += nota.calificacion

        return suma / len(notas)
    