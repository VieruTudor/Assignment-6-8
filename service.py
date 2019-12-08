from entities import *
from statistics import mean
import random


class serviceStudents(object):
    def __init__(self, repoStudents, validStudent, repoGrades):
        self.__repoStudents = repoStudents
        self.__validStudent = validStudent
        self.__repoGrades = repoGrades

    def generateStudents(self):
        self.__repoStudents.clearList()
        nameChoiceList = ["John",
                          "Alice",
                          "Richard",
                          "Max",
                          "Chris",
                          "Robert",
                          "Megan",
                          "Liz",
                          "Mary",
                          "Harry"]
        for idChoice in range(10):
            student = Student(idChoice + 1, random.choice(nameChoiceList))
            self.__validStudent.validateStudent(student)
            self.__repoStudents.addUniqueObject(student)

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

    def generateDisciplines(self):
        randomDisciplines = ["Computer Science", "Algebra", "Robotics"]
        for idChoice in range(3):
            disciplineName = random.choice(randomDisciplines)
            discipline = Discipline(idChoice + 1, disciplineName)
            self.__validDiscipline.validateDiscipline(discipline)
            self.__repoDisciplines.addUniqueObject(discipline)
            randomDisciplines.remove(disciplineName)

    def searchDisciplineByID(self, disciplineID):
        return self.__repoDisciplines.searchEntityByID(disciplineID)

    def searchDisciplinesByName(self, disciplineName):
        return self.__repoDisciplines.searchEntityByName(disciplineName)

    def addDiscipline(self, disciplineID, disciplineName):
        self.__repoDisciplines.clearList()
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

    def generateGrades(self):
        students = self.__repoStudents.getAllObjects()
        disciplines = self.__repoDisciplines.getAllObjects()
        for grades in range(10):
            randomStudentID = random.choice(students).getID()
            randomDisciplineID = random.choice(disciplines).getID()
            randomGradeValue = random.randint(1, 10)
            grade = Grade(randomStudentID, randomDisciplineID, randomGradeValue)
            self.__validGrade.validateGrade(grade)
            self.__repoGrades.addObject(grade)

    def addGrade(self, studentID, disciplineID, gradeValue):
        grade = Grade(studentID, disciplineID, gradeValue)
        self.__validGrade.validateGrade(grade)
        self.__repoGrades.addObject(grade)

    def removeGradesByStudentID(self, studentID):
        self.__repoGrades.removeGradeByStudentID(studentID)

    def removeGradesByDisciplineID(self, disciplineID):
        self.__repoGrades.removeGradeByDisciplineID(disciplineID)

    def getGrades(self):
        return self.__repoGrades.getAllObjects()

    '''
    grades = [(1, 1, 10), (2, 1, 10), (1, 2, 8), (1, 2, 7), (2, 2, 10), (2, 2, 9)]
    studentGrades = [[(1, 1, 10), (1, 2, 8), (1, 2, 7)], [(2, 1, 10), (2, 2, 10), (2, 2, 9)]]
    '''

    def studentsFailing(self):
        studentsFailing = []
        for student in self.__repoStudents.getAllObjects():
            for discipline in self.__repoDisciplines.getAllObjects():
                numberOfGrades = 0
                gradesSum = 0
                for grade in self.__repoGrades.getAllObjects():
                    if grade.getStudentID() == student.getID() and grade.getDisciplineID() == discipline.getID():
                        gradesSum += grade.getGrade()
                        numberOfGrades += 1
                if numberOfGrades > 0:
                    average = gradesSum / numberOfGrades
                    if average < 5:
                        studentsFailing.append([student.getID(), discipline.getName(), average])
        return studentsFailing

    def studentsSituation(self):
        studentsRankings = []
        for student in self.__repoStudents.getAllObjects():
            studentAverage = 0
            studentNumberOfDisciplines = 0
            for discipline in self.__repoDisciplines.getAllObjects():
                numberOfGrades = 0
                gradesSum = 0
                for grade in self.__repoGrades.getAllObjects():
                    if grade.getStudentID() == student.getID() and grade.getDisciplineID() == discipline.getID():
                        gradesSum += grade.getGrade()
                        numberOfGrades += 1
                if numberOfGrades > 0:
                    studentNumberOfDisciplines += 1
                    average = gradesSum / numberOfGrades
                    studentAverage += average
            if studentNumberOfDisciplines > 0:
                studentAverage /= studentNumberOfDisciplines
                studentsRankings.append([student.getID(), studentAverage])
        studentsRankings.sort(key=lambda finalGrade: finalGrade[1], reverse=True)
        return studentsRankings

    def disciplinesRankings(self):
        disciplinesRankings = []
        for discipline in self.__repoDisciplines.getAllObjects():
            disciplineGradesSum = 0
            disciplineNumberOfGrades = 0
            for grade in self.__repoGrades.getAllObjects():
                if grade.getDisciplineID() == discipline.getID():
                    disciplineGradesSum += grade.getGrade()
                    disciplineNumberOfGrades += 1
            if disciplineNumberOfGrades > 0:
                disciplineAverage = disciplineGradesSum / disciplineNumberOfGrades
                disciplinesRankings.append([discipline.getName(), disciplineAverage])
        disciplinesRankings.sort(key=lambda disciplineFinalGrade: disciplineFinalGrade[1], reverse=True)
        return disciplinesRankings

