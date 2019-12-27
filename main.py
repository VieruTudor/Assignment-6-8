from UI import Console
from service import serviceStudents, serviceDisciplines, serviceGrades
from validators import studentValidator, disciplineValidator, gradeValidator
from tests import studentTests, disciplineTests
from repo import *
from entities import *
from undoRepo import *


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
UIConsole.run()
