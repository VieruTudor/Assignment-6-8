from entities import *
import random


class serviceStudents(object):
    def __init__(self, repoStudents, validStudent, repoGrades):
        self.__repoStudents = repoStudents
        self.__validStudent = validStudent
        self.__repoGrades = repoGrades

    # Function that randomly generates 10 students from a certain list of names
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

    # Calls the repo and gets all the students
    def getStudents(self):
        return self.__repoStudents.getAllObjects()

    # With the student ID from the UI, calls the repo function that searches for the student with that ID
    def searchStudentByID(self, studentID):
        return self.__repoStudents.searchEntityByID(studentID)

    # Using the partial or full name given by the UI, calls the repo function and returns all students containing that
    # name
    def searchStudentsByName(self, searchName):
        return self.__repoStudents.searchEntityByName(searchName)

    # Creates a student based on the parameters from the UI, checks for its logical validity and calls the repo for
    # adding it to the list
    def addStudent(self, studentID, studentName):
        student = Student(studentID, studentName)
        self.__validStudent.validateStudent(student)
        self.__repoStudents.addUniqueObject(student)

    # Creates a new student based on the ID and new name given by the UI, checks for its validity and calls the repo
    # for the updating function
    def updateStudent(self, studentID, studentNewName):
        newStudent = Student(studentID, studentNewName)
        self.__validStudent.validateStudent(newStudent)
        self.__repoStudents.updateObject(newStudent.getID(), newStudent)

    # Calls the repo for the remove function using the given ID, also removing the grades of that student
    def removeStudent(self, studentID):
        self.__repoStudents.removeObject(studentID)
        self.__repoGrades.removeGradeByStudentID(studentID)


class serviceDisciplines(object):
    def __init__(self, repoDisciplines, validDiscipline, repoGrades):
        self.__repoDisciplines = repoDisciplines
        self.__validDiscipline = validDiscipline
        self.__repoGrades = repoGrades

    # Randomly generates 3 disciplines from a certain list of names
    def generateDisciplines(self):
        randomDisciplines = ["Computer Science", "Algebra", "Robotics"]
        for idChoice in range(3):
            disciplineName = random.choice(randomDisciplines)
            discipline = Discipline(idChoice + 1, disciplineName)
            self.__validDiscipline.validateDiscipline(discipline)
            self.__repoDisciplines.addUniqueObject(discipline)
            randomDisciplines.remove(disciplineName)

    # With the discipline ID from the UI, calls the repo function that searches for the discipline with that ID
    def searchDisciplineByID(self, disciplineID):
        return self.__repoDisciplines.searchEntityByID(disciplineID)

    # Using the partial or full name given by the UI, calls the repo function and returns all disciplines containing
    # that name
    def searchDisciplinesByName(self, disciplineName):
        return self.__repoDisciplines.searchEntityByName(disciplineName)

    # Creates a discipline based on the parameters from the UI, checks for its logical validity and calls the repo for
    # adding it to the list
    def addDiscipline(self, disciplineID, disciplineName):
        self.__repoDisciplines.clearList()
        discipline = Discipline(disciplineID, disciplineName)
        self.__validDiscipline.validateDiscipline(discipline)
        self.__repoDisciplines.addUniqueObject(discipline)

    # Creates a new discipline based on the ID and new name given by the UI, checks for its validity and calls the repo
    # for the updating function
    def updateDiscipline(self, disciplineID, disciplineNewName):
        newDiscipline = Discipline(disciplineID, disciplineNewName)
        self.__validDiscipline.validateDiscipline(newDiscipline)
        self.__repoDisciplines.updateObject(newDiscipline.getID(), newDiscipline)

    # Calls the repo for the remove function using the given ID, also removing the grades of that student
    def removeDiscipline(self, disciplineID):
        self.__repoDisciplines.removeObject(disciplineID)
        self.__repoGrades.removeGradeByDisciplineID(disciplineID)

    # Calls the repo and gets the list of all disciplines
    def getDisciplines(self):
        return self.__repoDisciplines.getAllObjects()


class serviceGrades(object):
    def __init__(self, repoStudents, repoDisciplines, repoGrades, validGrade):
        self.__repoStudents = repoStudents
        self.__repoDisciplines = repoDisciplines
        self.__repoGrades = repoGrades
        self.__validGrade = validGrade

    # Randomly generates 10 grades based on the existing students and disciplines, assigning a random grade
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

    # Creates a grade based on the parameters from the UI, checks for its logical validity and calls the repo for
    # adding it to the list
    def addGrade(self, studentID, disciplineID, gradeValue):
        grade = Grade(studentID, disciplineID, gradeValue)
        self.__validGrade.validateGrade(grade)
        self.__repoGrades.addObject(grade)

    # Function that is called in the students service upon the removal of a student. With the removal of a student, his
    # grades must be removed as well. Removes all the grades associated to a student ID
    def removeGradesByStudentID(self, studentID):
        self.__repoGrades.removeGradeByStudentID(studentID)

    # Function that is called in the disciplines service upon the removal of a discipline. With the removal of a
    # discipline, its grades must be removed as well. Removes all the grades associated to a discipline ID
    def removeGradesByDisciplineID(self, disciplineID):
        self.__repoGrades.removeGradeByDisciplineID(disciplineID)

    # Calls the repo and gets all grades in the list
    def getGrades(self):
        return self.__repoGrades.getAllObjects()

    # Computes for every student enrolled on a discipline the average of its grades at that discipline. If this average
    # is lower than 5, then he is considered to be failing that discipline.
    # Returns the list of all students failing at a discipline and their failing grade in the form :
    # [Student ID, Discipline, Final Grade]
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
        return studentsFailing[:]

    # Computes for every student the average of all their average grades at all disciplines they are enrolled in and
    # ranks them by their final average.
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
        return studentsRankings[:]

    # Computes for every discipline the average grade received by the students enrolled in it and ranks all the
    # disciplines by their final average.
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
        return disciplinesRankings[:]


