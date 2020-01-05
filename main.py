from UI import Console
from service import serviceStudents, serviceDisciplines, serviceGrades
from validators import studentValidator, disciplineValidator, gradeValidator
from repo import *
from entities import *
from undoRepo import *

with open("settings.txt", 'r') as readSettings:
    lines = readSettings.readlines()
    settings = []
    for line in lines:
        line = line.split('=')
        line[1] = line[1].replace("\n", "")
        settings.append(line[1])

setting = settings[0]
studentsFile = settings[1]
disciplinesFile = settings[2]
gradesFile = settings[3]

if setting == "inmemory":
    undo = Undo()
    serviceStudentValidator = studentValidator()
    serviceDisciplineValidator = disciplineValidator()
    serviceGradeValidator = gradeValidator()
    studentsRepo = Repo()
    disciplinesRepo = Repo()
    gradesRepo = Repo()
    gradesService = serviceGrades(undo, studentsRepo, disciplinesRepo, gradesRepo, gradeValidator)
    studentsService = serviceStudents(undo, studentsRepo, serviceStudentValidator, gradesService)
    disciplinesService = serviceDisciplines(undo, disciplinesRepo, serviceDisciplineValidator, gradesService)
    UIConsole = Console(studentsService, disciplinesService, gradesService, undo)
    UIConsole.initLists()
    UIConsole.run()

if setting == "textfiles":
    undo = Undo()
    serviceStudentValidator = studentValidator()
    serviceDisciplineValidator = disciplineValidator()
    serviceGradeValidator = gradeValidator()
    studentsRepo = FileRepo(studentsFile, Student.readFromFile, Student.writeToFile)
    disciplinesRepo = FileRepo(disciplinesFile, Discipline.readFromFile, Discipline.writeToFile)
    gradesRepo = FileRepo(gradesFile, Grade.readFromFile, Grade.writeToFile)
    gradesService = serviceGrades(undo, studentsRepo, disciplinesRepo, gradesRepo, gradeValidator)
    studentsService = serviceStudents(undo, studentsRepo, serviceStudentValidator, gradesService)
    disciplinesService = serviceDisciplines(undo, disciplinesRepo, serviceDisciplineValidator, gradesService)
    UIConsole = Console(studentsService, disciplinesService, gradesService, undo)
    UIConsole.run()

if setting == "binaryfiles":
    undo = Undo()
    serviceStudentValidator = studentValidator()
    serviceDisciplineValidator = disciplineValidator()
    serviceGradeValidator = gradeValidator()
    studentsRepo = BinaryRepo(studentsFile, Student.readFromFile, Student.writeToFile)
    disciplinesRepo = BinaryRepo(disciplinesFile, Discipline.readFromFile, Discipline.writeToFile)
    gradesRepo = BinaryRepo(gradesFile, Grade.readFromFile, Discipline.writeToFile)
    gradesService = serviceGrades(undo, studentsRepo, disciplinesRepo, gradesRepo, gradeValidator)
    studentsService = serviceStudents(undo, studentsRepo, serviceStudentValidator, gradesService)
    disciplinesService = serviceDisciplines(undo, disciplinesRepo, serviceDisciplineValidator, gradesService)
    UIConsole = Console(studentsService, disciplinesService, gradesService, undo)
    UIConsole.run()
