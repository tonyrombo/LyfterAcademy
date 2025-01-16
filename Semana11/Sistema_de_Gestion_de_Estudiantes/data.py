import csv
import os.path

class DataHandler:
    def __init__(self, filepath = 'Semana11/Sistema_de_Gestion_de_Estudiantes/students.csv'):
        self.filepath = filepath

    def export_data(self, students):
        self.filepath = 'Semana11/Sistema_de_Gestion_de_Estudiantes/students.csv'
        with open(self.filepath, 'w', newline='') as file:
            writer = csv.writer(file)
            
            if students:
                headers = vars(students[0]).keys()
                writer.writerow(headers)

                for student in students:
                    writer.writerow(vars(student).values())

        print('¡La información de los estudiantes fue exportada con éxito!')

    def import_data(self, students):
        from actions import Student
        filepath = input('Ingrese la ruta del archivo a importar: ')
        fileExists = os.path.isfile(filepath)

        while fileExists == False:
            filepath = input('Archivo no encontrado, ingrese de nuevo la ruta: ')
            fileExists = os.path.isfile(filepath)

        with open(filepath, 'r') as myfile:
            reader = csv.DictReader(myfile)
            for row in reader:
                average = (int(row['espanol']) + int(row['ingles']) + int(row['sociales']) + int(row['ciencias'])) / 4
                student = Student(name=row['name'], section=row['section'])
                student.espanol = int(row['espanol'])
                student.ingles = int(row['ingles'])
                student.sociales = int(row['sociales'])
                student.ciencias = int(row['ciencias'])
                student.average = average
                students.append(student)
        print("¡La información de los datos fue importada con éxito!")