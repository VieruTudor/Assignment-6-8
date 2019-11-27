from UI import Console
from service import serviceStudents, serviceDisciplines, serviceGrades
from validators import studentValidator, disciplineValidator, gradeValidator
from tests import studentTests, disciplineTests
from repo import *
from entities import *

studentTest = studentTests()
studentTest.runAllTests()
disciplineTest = disciplineTests()
disciplineTest.runAllTests()
serviceStudentValidator = studentValidator()
serviceDisciplineValidator = disciplineValidator()
serviceGradeValidator = gradeValidator()
studentsRepo = Repo()
disciplinesRepo = Repo()
gradesRepo = Repo()
studentsService = serviceStudents(studentsRepo, serviceStudentValidator, gradesRepo)
disciplinesService = serviceDisciplines(disciplinesRepo, serviceDisciplineValidator, gradesRepo)
gradesService = serviceGrades(studentsRepo, disciplinesRepo, gradesRepo, gradeValidator)
UIConsole = Console(studentsService, disciplinesService, gradesService)
UIConsole.run()
