from exceptions import *

'''
TODO : REWRITE UI LOOP SO BE SMALLER
       MOVE FUNCTION TRY / EXCEPT CALLS INTO FUNCTION BLOCK
       THEN JUST CALL IT
TODO : CREATE EXCEPTIONS FOR NON - NUMERICAL DATA TYPES PASSED AS INPUT BY USER
TODO (*OPTIONAL) : STRUCTURE COMMANDS AND OPTIONS IN TREE MODE WITH RETURN
'''


def numericalTypeCheck(inputNumber):
    try:
        inputNumber = int(inputNumber)
    except ValueError:
        raise UIError("Please insert a numerical value")


class Console(object):
    def __init__(self, serviceStudents, serviceDisciplines, serviceGrades):
        self.__serviceStudents = serviceStudents
        self.__serviceDisciplines = serviceDisciplines
        self.__serviceGrades = serviceGrades

    def __UIAddStudent(self, studentID, studentName):
        if studentID == "" or studentName == "":
            raise UIError("Please don't leave any fields empty")
        try:
            numericalTypeCheck(studentID)
            studentID = int(studentID)
            self.__serviceStudents.addStudent(studentID, studentName)
        except UIError as error:
            print(str(error))

    @staticmethod
    def printMenu():
        print("1. Student commands\n"
              "2. Discipline commands\n"
              "3. Grade commands\n")

    def __UIUpdateStudent(self, studentID, studentNewName):
        if studentID == "" or studentNewName == "":
            raise UIError("Please don't leave any fields empty")
        try:
            numericalTypeCheck(studentID)
            studentID = int(studentID)
            self.__serviceStudents.updateStudent(studentID, studentNewName)
        except UIError as error:
            print(str(error))

    def __UIRemoveStudent(self, studentID):
        if studentID == "":
            raise UIError("Please don't leave the ID empty")
        try:
            numericalTypeCheck(studentID)
            studentID = int(studentID)
            self.__serviceStudents.removeStudent(studentID)
        except UIError as error:
            print(str(error))

    def __UIListStudents(self):
        students = self.__serviceStudents.getStudents()
        for student in students:
            print(student)

    def __UISearchStudentByID(self, studentID):
        if studentID == "":
            raise UIError("Please don't leave the ID empty")
        try:
            numericalTypeCheck(studentID)
            studentID = int(studentID)
            print(self.__serviceStudents.searchStudentByID(studentID))
        except UIError as error:
            print(str(error))

    def __UISearchStudentsByName(self, searchStudentName):
        if searchStudentName == "":
            raise UIError("Please don't leave the name empty")
        searchMatches = self.__serviceStudents.searchStudentsByName(searchStudentName)
        for student in searchMatches:
            print(student)

    def __UIAddDiscipline(self, disciplineID, disciplineName):
        if disciplineID == "" or disciplineName == "":
            raise UIError("Please don't leave any fields empty")
        try:
            numericalTypeCheck(disciplineID)
            disciplineID = int(disciplineID)
            self.__serviceDisciplines.addDiscipline(disciplineID, disciplineName)
        except UIError as error:
            print(str(error))

    def __UIUpdateDiscipline(self, disciplineID, disciplineNewName):
        if disciplineID == "" or disciplineNewName == "":
            raise UIError("Please don't leave any fields empty")
        try:
            numericalTypeCheck(disciplineID)
            disciplineID = int(disciplineID)
            self.__serviceDisciplines.updateDiscipline(disciplineID, disciplineNewName)
        except UIError as error:
            print(str(error))

    def __UIRemoveDiscipline(self, disciplineID):
        if disciplineID == "":
            raise UIError("Please don't leave the ID empty")
        try:
            numericalTypeCheck(disciplineID)
            disciplineID = int(disciplineID)
            self.__serviceDisciplines.removeDiscipline(disciplineID)
        except UIError as error:
            print(str(error))

    def __UIListDisciplines(self):
        disciplines = self.__serviceDisciplines.getDisciplines()
        for discipline in disciplines:
            print(discipline)

    def __UIAddGrade(self, studentID, disciplineID, gradeValue):
        if studentID == "" or disciplineID == "" or gradeValue == "":
            raise UIError("Please don't leave any fields empty")
        try:
            numericalTypeCheck(studentID)
            studentID = int(studentID)
            numericalTypeCheck(disciplineID)
            disciplineID = int(disciplineID)
            numericalTypeCheck(gradeValue)
            gradeValue = int(gradeValue)
            self.__serviceGrades.addGrade(studentID, disciplineID, gradeValue)
        except UIError as error:
            print(str(error))

    def __UIListGrades(self):
        grades = self.__serviceGrades.getGrades()
        for grade in grades:
            print(grade)

    def run(self):
        while True:
            self.printMenu()
            command = input(">>>")
            command.strip()
            if command == "1":
                print("1. Add student.\n"
                      "2. Update student.\n"
                      "3. Remove student.\n"
                      "4. List students.\n"
                      "5. Search student by ID.\n"
                      "6. Search student(s) by name.\n")
                option = input(">>>")
                if option == "1":
                    try:
                        studentID = input("Insert student's ID (unique) : ")
                        studentName = input("Insert student's name : ")
                        self.__UIAddStudent(studentID, studentName)
                    except RepoError as error:
                        print(str(error))
                    except UIError as error:
                        print(str(error))
                    except ValidError as error:
                        print(str(error))
                if option == "2":
                    try:
                        studentID = input("Insert student ID to be updated : ")
                        studentNewName = input("Insert student's new name : ")
                        self.__UIUpdateStudent(studentID, studentNewName)
                    except RepoError as error:
                        print(str(error))
                    except UIError as error:
                        print(str(error))
                    except ValidError as error:
                        print(str(error))
                if option == "3":
                    try:
                        studentID = input("Insert student ID to be removed : ")
                        self.__UIRemoveStudent(studentID)
                    except RepoError as error:
                        print(str(error))
                    except UIError as error:
                        print(str(error))
                if option == "4":
                    self.__UIListStudents()
                if option == "5":
                    try:
                        studentID = input("Search by student ID : ")
                        self.__UISearchStudentByID(studentID)
                    except RepoError as error:
                        print(str(error))
                    except UIError as error:
                        print(str(error))
                if option == "6":
                    try:
                        studentSearchName = input("Search by student name : ")
                        self.__UISearchStudentsByName(studentSearchName)
                    except RepoError as error:
                        print(str(error))
                    except UIError as error:
                        print(str(error))
                    # TODO IMPLEMENT UI ERROR FOR FURTHER EXCEPTION THROWS
            if command == "2":
                print("1. Add discipline.\n"
                      "2. Update discipline.\n"
                      "3. Remove discipline.\n"
                      "4. List disciplines.\n")
                option = input(">>>")
                if option == "1":
                    try:
                        disciplineID = input("Insert discipline ID (unique) : ")
                        disciplineName = input("Insert discipline name : ")
                        self.__UIAddDiscipline(disciplineID, disciplineName)
                    except RepoError as error:
                        print(str(error))
                    except UIError as error:
                        print(str(error))
                    except ValidError as error:
                        print(str(error))
                if option == "2":
                    try:
                        disciplineID = input("Insert discipline ID to be updated : ")
                        disciplineNewName = input("Insert discipline's new name : ")
                        self.__UIUpdateDiscipline(disciplineID, disciplineNewName)
                    except RepoError as error:
                        print(str(error))
                    except UIError as error:
                        print(str(error))
                    except ValidError as error:
                        print(str(error))
                if option == "3":
                    try:
                        disciplineID = input("Insert discipline ID to be removed : ")
                        self.__UIRemoveDiscipline(disciplineID)
                    except RepoError as error:
                        print(str(error))
                    except UIError as error:
                        print(str(error))
                if option == "4":
                    self.__UIListDisciplines()
            if command == "3":
                print("1. Grade a student.\n"
                      "2. View all grades.\n")
                option = input(">>>")
                if option == "1":
                    studentID = input("Insert student's ID : ")
                    disciplineID = input("Insert the discipline's ID : ")
                    gradeValue = input("Insert grade value : ")
                    self.__UIAddGrade(studentID, disciplineID, gradeValue)
                if option == "2":
                    self.__UIListGrades()
