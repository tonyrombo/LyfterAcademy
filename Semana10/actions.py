students = [
    {'name': 'Will', 'section': '33B', 'Español': 45, 'Inglés': 78, 'Sociales': 90, 'Ciencias': 67, 'promedio': 90.0},
    {'name': 'Sonia', 'section': '12D', 'Español': 56, 'Inglés': 90, 'Sociales': 90, 'Ciencias': 89, 'promedio': 30.0},
    {'name': 'Esteban', 'section': '12D', 'Español': 56, 'Inglés': 90, 'Sociales': 90, 'Ciencias': 89, 'promedio': 100.0}
]

def ingresarEstudiante():
    studentName = input("Ingrese el nombre del estudiante: ")
    subjectsList = ["Español","Inglés", "Sociales", "Ciencias"]
    student = {}
    
    student['name'] = studentName
    
    try:
        studentSection = input("Ingrese la sección: ")
        if(len(studentSection) > 3):
            raise ValueError
        student['section'] = studentSection
        
    except:
        print("La seccion no puede tener más de 3 caracteres.")

    totalNotas = 0
    for subject in subjectsList:
        grade = int(input(f"Ingrese la nota de {subject}: "))
        while grade > 100:
            grade = int(input(f"La nota deben ser numeros entre 0 - 100.\nIngrese de nuevo la nota de {subject}: "))
        student[subject] = grade
        totalNotas = totalNotas + grade

    student['promedio'] = totalNotas / len(subjectsList)
    students.append(student)
    print(students)


def informacionEstudiantes():
    text = ""
    for student in range(len(students)):
        text += f"\nEstudiante {student + 1}\n"
        for key, value in students[student].items():
            text += f"{key}: {value}\n"
    print(text)


def topTresEstudiantes():
    estudiantesPorOrden = sorted(students, key=lambda x: x['promedio'], reverse=True)#funcionalidad para ordenar lista de diccionarios por un key especifico.
    primerEstudiante = f"{estudiantesPorOrden[0]['name']} con nota: {estudiantesPorOrden[0]['promedio']}"
    segundoEstudiante = f"{estudiantesPorOrden[1]['name']} con nota: {estudiantesPorOrden[1]['promedio']}"
    tercerEstudiante = f"{estudiantesPorOrden[2]['name']} con nota: {estudiantesPorOrden[2]['promedio']}"
    print(f"Este es el top 3 de estudiantes\n{primerEstudiante}\n{segundoEstudiante}\n{tercerEstudiante}")

def promedioTotal():
    promedioTotal = 0
    for student in students:
        promedioTotal += student['promedio']
    promedioTotal = round(promedioTotal/len(students),2)
    print(f'El promedio total entre los estudiantes es: {promedioTotal}')
