"""
Problemática: Sistema de Gestión Escolar

Imagina que estás desarrollando un sistema de gestión escolar. Debes diseñar clases que permitan gestionar 
información sobre estudiantes, profesores y cursos. Además,
el sistema debe ser capaz de realizar acciones como matricular estudiantes en cursos, 
asignar profesores a cursos, y generar reportes

Requisitos:

Crea una clase Estudiante que tenga atributos como nombre, edad, número de identificación y una lista de cursos en los que está matriculado.

Implementa una clase Profesor con atributos como nombre, edad, número de identificación y la lista de cursos que enseña.

Diseña una clase Curso que tenga un nombre, un código único y una lista de estudiantes matriculados.

La clase Estudiante debe tener un método para matricularse en un curso.

La clase Profesor debe tener un método para asignarse a un curso.

Crea una clase GestorEscolar que actúe como el sistema central. Esta clase debe almacenar listas de estudiantes, profesores y cursos, y debe tener métodos para matricular estudiantes, asignar profesores a cursos y generar un reporte de cursos con sus estudiantes.

Implementa la lógica para evitar que un estudiante se matricule dos veces en el mismo curso.

Asegúrate de que un profesor no pueda enseñar el mismo curso en más de una instancia.

Agrega la capacidad de generar un reporte que muestre la lista de cursos con sus respectivos estudiantes y profesores asignados.

Crea instancias de las clases y realiza pruebas para demostrar que tu sistema funciona correctamente.
"""

class Estudiante:
    #creamos un constructor para estudiante
    def __init__(self,nombre,edad,NumId):
        self.nombre = nombre
        self.edad = edad
        self.NumId = NumId
        self.cursos = []
    
    #metodo para agregar un cursito    
    def addCourse(self,curso):
        if curso not in self.cursos:
            self.cursos.append(curso)
            #no nos olvide agregar el estudiante
            #agregamos la referencia del objeto
            curso.addStudent(self)
            
            
#clase para curso

class Curso:
    def __init__(self,nombre,idKey):
        self.nombre = nombre
        self.idKey = idKey
        self.listEst = []
    def addStudent(self,estudiante):
        #agregamos al estudiante al arreglo
        self.listEst.append(estudiante) 
        
           
class Profesor:
    def __init__(self, nombre, edad, identificacion):
        self.nombre = nombre
        self.edad = edad
        self.identificacion = identificacion
        self.cursos_asignados = []

    def asignar_curso(self, curso):
        if curso not in self.cursos_asignados:
            self.cursos_asignados.append(curso)
            curso.asignar_profesor(self)
            print(f"{self.nombre} ha sido asignado a enseñar {curso.nombre}")
        else:
            print(f"{self.nombre} ya está asignado a enseñar {curso.nombre}")                  