from modelo.registro_notas import RegistroNotas

registro = RegistroNotas()

# Agregar estudiantes
registro.agregar_estudiante("01", "Juan Pérez")
registro.agregar_estudiante("02", "María Gómez")  
registro.agregar_estudiante("03", "Carlos López")     

# Agregar asignaturas
registro.registrar_asignatura("POO", "Programacion Orientada a Objetos")
registro.registrar_asignatura("BD", "Base de Datos")
registro.registrar_asignatura("SP", "Sistemas Opertivos")

# Registrar notas
registro.registrar_nota("01", "POO", 85)
registro.registrar_nota("01", "BD", 90)    
registro.registrar_nota("02", "POO", 78)

# Mostrar promedio 
promedio = registro.promedio_estudiante("01")

print(f"El promedio del estudiante '01' es: {promedio}")
