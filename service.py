from entities import *


class serviceStudents(object):
    def __init__(self, repoStudents, validStudent, repoGrades):
        self.__repoStudents = repoStudents
        self.__validStudent = validStudent
        self.__repoGrades = repoGrades

    def getStudents(self):
        return self.__repoStudents.getAllObjects()

    def searchStudentByID(self, studentID):
        return self.__repoStudents.searchEntityByID(studentID)

    def searchStudentsByName(self, searchName):
        return self.__repoStudents.searchEntityByName(searchName)

    def addStudent(self, studentID, studentName):
        student = Student(studentID, studentName)
        self.__validStudent.validateStudent(student)
        self.__repoStudents.addUniqueObject(student)

    def updateStudent(self, studentID, studentNewName):
        newStudent = Student(studentID, studentNewName)
        self.__validStudent.validateStudent(newStudent)
        self.__repoStudents.updateObject(newStudent.getID(), newStudent)

    def removeStudent(self, studentID):
        self.__repoStudents.removeObject(studentID)
        self.__repoGrades.removeGradeByStudentID(studentID)


class serviceDisciplines(object):
    def __init__(self, repoDisciplines, validDiscipline, repoGrades):
        self.__repoDisciplines = repoDisciplines
        self.__validDiscipline = validDiscipline
        self.__repoGrades = repoGrades

    def addDiscipline(self, disciplineID, disciplineName):
        discipline = Discipline(disciplineID, disciplineName)
        self.__validDiscipline.validateDiscipline(discipline)
        self.__repoDisciplines.addUniqueObject(discipline)

    def updateDiscipline(self, disciplineID, disciplineNewName):
        newDiscipline = Discipline(disciplineID, disciplineNewName)
        self.__validDiscipline.validateDiscipline(newDiscipline)
        self.__repoDisciplines.updateObject(newDiscipline.getID(), newDiscipline)

    def removeDiscipline(self, disciplineID):
        self.__repoDisciplines.removeObject(disciplineID)
        self.__repoGrades.removeGradeByDisciplineID(disciplineID)

    def getDisciplines(self):
        return self.__repoDisciplines.getAllObjects()


class serviceGrades(object):
    def __init__(self, repoStudents, repoDisciplines, repoGrades, validGrade):
        self.__repoStudents = repoStudents
        self.__repoDisciplines = repoDisciplines
        self.__repoGrades = repoGrades
        self.__validGrade = validGrade

    def removeGradesByStudentID(self, studentID):
        self.__repoGrades.removeGradeByStudentID(studentID)

    def removeGradesByDisciplineID(self, disciplineID):
        self.__repoGrades.removeGradeByDisciplineID(disciplineID)

    def getGrades(self):
        return self.__repoGrades.getAllObjects()

    def addGrade(self, studentID, disciplineID, gradeValue):
        grade = Grade(studentID, disciplineID, gradeValue)
        self.__validGrade.validateGrade(grade)
        self.__repoGrades.addObject(grade)
