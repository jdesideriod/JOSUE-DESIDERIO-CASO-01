class Estudiante:
    
    
    def __init__(self, matricula, nombre, ):
        self._matricula = matricula
        self._nombre = nombre

    @property
    def matricula(self):
        return self._matricula

    @property
    def nombre(self):
        return self._nombre 

    def __str__(self):
        return f"{self._matricula} - {self._nombre}"