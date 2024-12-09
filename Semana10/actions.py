students = [
    {'Nombre': 'Will', 'Sección': '33B', 'Español': 45, 'Inglés': 78, 'Sociales': 90, 'Ciencias': 67, 'Promedio': 90.0},
    {'Nombre': 'Sonia', 'Sección': '12D', 'Español': 56, 'Inglés': 90, 'Sociales': 90, 'Ciencias': 89, 'Promedio': 30.0},
    {'Nombre': 'Esteban', 'Sección': '12D', 'Español': 56, 'Inglés': 90, 'Sociales': 90, 'Ciencias': 89, 'Promedio': 100.0}
]

def ingresarEstudiante():
    studentName = input("Ingrese el nombre del estudiante: ")
    subjectsList = ["Español","Inglés", "Sociales", "Ciencias"]
    student = {}
    
    student['Nombre'] = studentName
    
    try:
        studentSection = input("Ingrese la sección: ")
        if(len(studentSection) > 3):
            raise ValueError
        student['Sección'] = studentSection
        
    except:
        print("La seccion no puede tener más de 3 caracteres.")

    totalGrades = 0
    for subject in subjectsList:
        grade = int(input(f"Ingrese la nota de {subject}: "))
        while grade > 100:
            grade = int(input(f"La nota deben ser numeros entre 0 - 100.\nIngrese de nuevo la nota de {subject}: "))
        student[subject] = grade
        totalGrades = totalGrades + grade

    student['Promedio'] = totalGrades / len(subjectsList)
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
    sortedStudents = sorted(students, key=lambda x: x['Promedio'], reverse=True)#funcionalidad para ordenar lista de diccionarios por un key especifico.
    firstStudent = f"{sortedStudents[0]['Nombre']} con nota: {sortedStudents[0]['Promedio']}"
    secondStudent = f"{sortedStudents[1]['Nombre']} con nota: {sortedStudents[1]['Promedio']}"
    thirdStudent = f"{sortedStudents[2]['Nombre']} con nota: {sortedStudents[2]['Promedio']}"
    print(f"Este es el top 3 de estudiantes\n{firstStudent}\n{secondStudent}\n{thirdStudent}")

def promedioTotal():
    averageTotal = 0
    for student in students:
        averageTotal += student['Promedio']
    averageTotal = round(averageTotal/len(students),2)
    print(f'El promedio total entre los estudiantes es: {averageTotal}')
