import csv
import os.path
from actions import students

def exportData():
    students_file = open('Semana10/students.csv', 'w')

    csv_writer = csv.writer(students_file)
    
    counter = 0

    for student in students:
        if counter == 0:
            header = student.keys()
            csv_writer.writerow(header)
            counter += 1

        csv_writer.writerow(student.values())


def importData():
    file = input('Ingrese la ruta del archivo a importar: ')
    fileExists = os.path.isfile(file)

    while fileExists == False:
        file = input('Archivo no encontrado, ingrese de nuevo la ruta: ')
        fileExists = os.path.isfile(file)
    
    with open(file) as myfile:
        next(myfile) #Funcionalidad para saltar la primer iteraccion en el For Loop y asi evitar los headings del CSV.
        for line in myfile:
            studentData = line.split(',')
            data = {
                'name': studentData[0],
                'section': studentData[1],
                'Espanol': studentData[2],
                'Ingles': studentData[3],
                'Sociales': studentData[4],
                'Ciencias': studentData[5]
            }
            students.append(data)
        print("La informacion de los datos fue importada con éxito")
