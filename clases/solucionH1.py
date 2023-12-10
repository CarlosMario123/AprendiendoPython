class Estudiante:
    def __init__(self, nombre, edad, identificacion):
        self.nombre = nombre
        self.edad = edad
        self.identificacion = identificacion
        self.cursos_matriculados = []

    def matricular_curso(self, curso):
        if curso not in self.cursos_matriculados:
            self.cursos_matriculados.append(curso)
            curso.agregar_estudiante(self)
            print(f"{self.nombre} se ha matriculado en {curso.nombre}")
        else:
            print(f"{self.nombre} ya está matriculado en {curso.nombre}")


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


class Curso:
    def __init__(self, nombre, codigo):
        self.nombre = nombre
        self.codigo = codigo
        self.estudiantes_matriculados = []
        self.profesor_asignado = None

    def agregar_estudiante(self, estudiante):
        self.estudiantes_matriculados.append(estudiante)

    def asignar_profesor(self, profesor):
        self.profesor_asignado = profesor


class GestorEscolar:
    def __init__(self):
        self.estudiantes = []
        self.profesores = []
        self.cursos = []

    def matricular_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)

    def contratar_profesor(self, profesor):
        self.profesores.append(profesor)

    def crear_curso(self, nombre, codigo):
        curso = Curso(nombre, codigo)
        self.cursos.append(curso)
        return curso

    def generar_reporte(self):
        print("Reporte de Cursos:")
        for curso in self.cursos:
            profesor = curso.profesor_asignado.nombre if curso.profesor_asignado else "Sin asignar"
            estudiantes = ", ".join([estudiante.nombre for estudiante in curso.estudiantes_matriculados])
            print(f"Curso: {curso.nombre} - Profesor: {profesor} - Estudiantes: {estudiantes}")


# Pruebas de funcionamiento
gestor = GestorEscolar()

estudiante1 = Estudiante("Juan", 18, "001")
estudiante2 = Estudiante("Maria", 20, "002")
gestor.matricular_estudiante(estudiante1)
gestor.matricular_estudiante(estudiante2)

profesor1 = Profesor("Carlos", 35, "P001")
profesor2 = Profesor("Laura", 30, "P002")
gestor.contratar_profesor(profesor1)
gestor.contratar_profesor(profesor2)

curso1 = gestor.crear_curso("Matemáticas", "MAT101")
curso2 = gestor.crear_curso("Historia", "HIS101")

estudiante1.matricular_curso(curso1)
estudiante2.matricular_curso(curso1)
estudiante2.matricular_curso(curso2)

profesor1.asignar_curso(curso1)
profesor2.asignar_curso(curso2)

gestor.generar_reporte()
