class Student(object):
    def __init__(self, studentID, studentName):
        self.__ID = studentID
        self.__name = studentName

    def getID(self):
        return self.__ID

    def getName(self):
        return self.__name

    def setName(self, newName):
        self.__name = newName

    def __eq__(self, other):
        return self.getID() == other.getID()

    def __str__(self):
        return "ID : " + str(self.__ID) + ", " + str(self.__name)

    @staticmethod
    def readFromFile(line):
        attributes = line.split(",")
        return Student(attributes[0].strip(), attributes[1].strip())

    @staticmethod
    def writeToFile(student):
        return str(student.getID()) + "," + str(student.getName())


class Discipline(object):
    def __init__(self, disciplineID, disciplineName):
        self.__ID = disciplineID
        self.__name = disciplineName

    def getID(self):
        return self.__ID

    def getName(self):
        return self.__name

    def setName(self, newName):
        self.__name = newName

    def __eq__(self, other):
        return self.getID() == other.getID()

    def __str__(self):
        return "ID : " + str(self.__ID) + ", " + str(self.__name)

    @staticmethod
    def readFromFile(line):
        attributes = line.split(",")
        return Discipline(attributes[0].strip(), attributes[1].strip())

    @staticmethod
    def writeToFile(discipline):
        return str(discipline.getID()) + "," + str(discipline.getName())


class Grade(object):
    def __init__(self, studentID, disciplineID, gradeValue):
        self.__student = studentID
        self.__discipline = disciplineID
        self.__grade = gradeValue

    def getStudentID(self):
        return self.__student

    def getDisciplineID(self):
        return self.__discipline

    def getGrade(self):
        return self.__grade

    def __str__(self):
        return "ID : " + str(self.__student) + ", " + "Discipline : " + str(
            self.__discipline) + ", " + "Grade : " + str(
            self.__grade)

    @staticmethod
    def readFromFile(line):
        attributes = line.split(",")
        return Grade(attributes[0], attributes[1], attributes[2])

    @staticmethod
    def writeToFile(grade):
        return str(grade.getStudentID) + "," + str(grade.getDisciplineID) + "," + str(grade.getGrade)