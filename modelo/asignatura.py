class Asignatura: 

    def __init__(self, codigo, nombre):
        self._codigo = codigo
        self._nombre = nombre

    @property
    def codigo(self):
        return self._codigo

    @property
    def nombre(self):
        return self._nombre 

    def __str__(self):
        return f"{self._codigo} - {self._nombre}"