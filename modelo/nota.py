class Nota:

   def __init__(self, estudiante, asignatura, calificacion):
      self._estudiante = estudiante 
      self._asignatura = asignatura
      self._calificacion = calificacion 

   @property
   def estudiante(self):
       return self._estudiante 

   @property
   def asignatura(self):
      return self._asignatura

   @property
   def calificacion(self):
      return self._calificacion