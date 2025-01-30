from data import DataHandler

class Student:
    def __init__(self, name, section):
        self.name = name
        self.section = section
        self.espanol = 0
        self.ingles = 0
        self.sociales = 0
        self.ciencias = 0
        self.average = 0

class Actions:
    
    def __init__(self):
        self.students = []
        self.data = DataHandler()

    def ingresar_notas(self, student):
        subjectsList = ["espanol","ingles", "Sociales", "Ciencias"]

        totalGrades = 0
        for subject in subjectsList:
            grade = int(input(f"Ingrese la nota de {subject}: "))
            while grade > 100:
                grade = int(input(f"La nota deben ser numeros entre 0 - 100.\nIngrese de nuevo la nota de {subject}: "))
            setattr(student, subject.lower(), grade)
            totalGrades = totalGrades + grade
        
        studentAverage = totalGrades / len(subjectsList)
        setattr(student, "average", studentAverage)

    def add_student(self):
        studentName = input(f"Ingrese el nombre del estudiante: ")

        try:
            studentSection = input("Ingrese la sección: ")
            if(len(studentSection) > 3):
                raise ValueError
            
        except:
            print("La seccion no puede tener más de 3 caracteres.")

        student = Student(studentName, studentSection)
        self.ingresar_notas(student)
        self.students.append(student)

    def show_students(self):
        text = ""
        for index, student in enumerate(self.students):
            text += f"\nEstudiante {index + 1}\n"
            currentStudent = vars(student)
            for key, value in currentStudent.items():
                text += f"{key}: {value}\n"
        print(text)

    def top_three_students(self):
        sortedStudents = sorted(self.students, key=lambda e: e.average, reverse=True)
        print("\nTop 3 Estudiantes:")
        for index, student in enumerate(sortedStudents[:3], start=1):
            print(f"{index}. {student.name} - Promedio: {student.average:.2f}")

    def total_average(self):
        total = sum(student.average for student in self.students)
        total_average = round(total / len(self.students), 2)
        print(f'El promedio total entre los estudiantes es: {total_average}')

    def export_data(self):
        self.data.export_data(self.students)

    def import_data(self):
        self.data.import_data(self.students)