from exceptions import *


# Checks if the provided input is a number, throws an exception otherwise
def numericalTypeCheck(inputNumber):
    try:
        inputNumber = int(inputNumber)
    except ValueError:
        raise UIError("Please insert a numerical value")


# Class managing the UI of the program
class Console(object):
    def __init__(self, serviceStudents, serviceDisciplines, serviceGrades, serviceUndo):
        self.__serviceStudents = serviceStudents
        self.__serviceDisciplines = serviceDisciplines
        self.__serviceGrades = serviceGrades
        self.__serviceUndo = serviceUndo

    # Randomly generates entries for students, disciplines and grades
    def initLists(self):
        self.__serviceStudents.generateStudents()
        self.__serviceDisciplines.generateDisciplines()
        self.__serviceGrades.generateGrades()

    # Prints the UI menu
    @staticmethod
    def __printMenu():
        print("1. Student commands\n"
              "2. Discipline commands\n"
              "3. Grade commands\n"
              "4. Undo last action\n"
              "5. Redo last action\n"
              "6. Exit program")

    def userInterface_undo(self):
        try:
            self.__serviceUndo.undoFunction()
        except Exception as ex:
            print(ex)

    def userInterface_redo(self):
        try:
            self.__serviceUndo.redoFunction()
        except Exception as ex:
            print(ex)

    # region STUDENT METHODS
    # Takes the parameters given by the user, checks for empty input and numerical types and passes them to service
    # for the adding function
    def __UIAddStudent(self, studentID, studentName):
        if studentID == "" or studentName == "":
            raise UIError("Please don't leave any fields empty")
        try:
            numericalTypeCheck(studentID)
            studentID = int(studentID)
            self.__serviceStudents.addStudent(studentID, studentName)
        except UIError as error:
            print(str(error))

    # Takes parameters from the user input, checks them and sends them to the service for the update function
    def __UIUpdateStudent(self, studentID, studentNewName):
        if studentID == "" or studentNewName == "":
            raise UIError("Please don't leave any fields empty")
        try:
            numericalTypeCheck(studentID)
            studentID = int(studentID)
            self.__serviceStudents.updateStudent(studentID, studentNewName)
        except UIError as error:
            print(str(error))

    # Takes parameter from user, checks it and sends it to the service for the remove function
    def __UIRemoveStudent(self, studentID):
        if studentID == "":
            raise UIError("Please don't leave the ID empty")
        try:
            numericalTypeCheck(studentID)
            studentID = int(studentID)
            self.__serviceStudents.removeStudent(studentID)
        except UIError as error:
            print(str(error))

    # Gets the students list from the service and prints them
    def __UIListStudents(self):
        students = self.__serviceStudents.getStudents()
        for student in students:
            print(student)

    # Takes a student ID from the user, checks it, sends it to the service and gets the matching student back
    def __UISearchStudentByID(self, searchStudentID):
        if searchStudentID == "":
            raise UIError("Please don't leave the ID empty")
        try:
            numericalTypeCheck(searchStudentID)
            searchStudentID = int(searchStudentID)
            print(self.__serviceStudents.searchStudentByID(searchStudentID))
        except UIError as error:
            print(str(error))

    # Takes a student partial or full name from the user, checks it and sends it to service, getting back a list
    # containing the results
    def __UISearchStudentsByName(self, searchStudentName):
        if searchStudentName == "":
            raise UIError("Please don't leave the name empty")
        searchMatches = self.__serviceStudents.searchStudentsByName(searchStudentName)
        for student in searchMatches:
            print(student)

    # endregion

    # region DISCIPLINE METHODS

    # Takes the parameters given by the user, checks for empty input and numerical types and passes them to service
    # for the adding function
    def __UIAddDiscipline(self, disciplineID, disciplineName):
        if disciplineID == "" or disciplineName == "":
            raise UIError("Please don't leave any fields empty")
        try:
            numericalTypeCheck(disciplineID)
            disciplineID = int(disciplineID)
            self.__serviceDisciplines.addDiscipline(disciplineID, disciplineName)
        except UIError as error:
            print(str(error))

    # Takes parameters from the user input, checks them and sends them to the service for the update function
    def __UIUpdateDiscipline(self, disciplineID, disciplineNewName):
        if disciplineID == "" or disciplineNewName == "":
            raise UIError("Please don't leave any fields empty")
        try:
            numericalTypeCheck(disciplineID)
            disciplineID = int(disciplineID)
            self.__serviceDisciplines.updateDiscipline(disciplineID, disciplineNewName)
        except UIError as error:
            print(str(error))

    # Takes parameter from user, checks it and sends it to the service for the remove function
    def __UIRemoveDiscipline(self, disciplineID):
        if disciplineID == "":
            raise UIError("Please don't leave the ID empty")
        try:
            numericalTypeCheck(disciplineID)
            disciplineID = int(disciplineID)
            self.__serviceDisciplines.removeDiscipline(disciplineID)
        except UIError as error:
            print(str(error))

    # Gets the disciplines list from the service and prints them
    def __UIListDisciplines(self):
        disciplines = self.__serviceDisciplines.getDisciplines()
        for discipline in disciplines:
            print(discipline)

    # Takes a discipline partial or full name from the user, checks it and sends it to service, getting back a list
    # containing the results
    def __UISearchDisciplinesByName(self, searchDisciplineName):
        if searchDisciplineName == "":
            raise UIError("Please don't leave the name empty")
        searchMatches = self.__serviceDisciplines.searchDisciplinesByName(searchDisciplineName)
        for discipline in searchMatches:
            print(discipline)

    # Takes a discipline ID from the user, checks it, sends it to the service and gets the matching discipline back
    def __UISearchDisciplineByID(self, searchDisciplineID):
        if searchDisciplineID == "":
            raise UIError("Please don't leave the ID empty")
        try:
            numericalTypeCheck(searchDisciplineID)
            searchDisciplineID = int(searchDisciplineID)
            print(self.__serviceDisciplines.searchDisciplineByID(searchDisciplineID))
        except UIError as error:
            print(str(error))

    # endregion

    # region GRADE METHODS

    # Takes parameters from the user, checks them and passes them to the service for the adding function
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

    # Gets the list of grades from the service and prints them
    def __UIListGrades(self):
        grades = self.__serviceGrades.getGrades()
        for grade in grades:
            print(grade)

    # Gets the list of failing students and prints them in the form [Student ID, Discipline, Grade]
    def __UIFailingStudents(self):
        failingStudents = self.__serviceGrades.studentsFailing()
        print(failingStudents)

    # Gets the list of students sorted descending by their average grade on all disciplines
    def __UIStudentsRankings(self):
        studentsRankings = self.__serviceGrades.studentsSituation()
        print(studentsRankings)

    # Gets the list of disciplines ranked by the average grade received by all students enrolled on that discipline
    def __UIDisciplinesRankings(self):
        disciplinesRankings = self.__serviceGrades.disciplinesRankings()
        print(disciplinesRankings)

    # endregion

    def run(self):
        while True:
            self.__printMenu()
            command = input(">>>")
            command.strip()
            if command == "1":
                print("1. Add student.\n"
                      "2. Update student.\n"
                      "3. Remove student.\n"
                      "4. List students.\n"
                      "5. Search student by ID.\n"
                      "6. Search student(s) by name.\n"
                      "7. Exit program.")
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
                if option == "7":
                    return
            if command == "2":
                print("1. Add discipline.\n"
                      "2. Update discipline.\n"
                      "3. Remove discipline.\n"
                      "4. List disciplines.\n"
                      "5. Search discipline by ID.\n"
                      "6. Search discipline(s) by name.\n"
                      "7. Exit program.")
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
                if option == "5":
                    try:
                        disciplineID = input("Search by discipline ID : ")
                        self.__UISearchDisciplineByID(disciplineID)
                    except RepoError as error:
                        print(str(error))
                if option == "6":
                    try:
                        disciplineName = input("Search discipline by name : ")
                        self.__UISearchDisciplinesByName(disciplineName)
                    except RepoError as error:
                        print(str(error))
                if option == "7":
                    return
            if command == "3":
                print("1. Grade a student.\n"
                      "2. View all grades.\n"
                      "3. Failing students.\n"
                      "4. Students rankings.\n"
                      "5. Disciplines rankings.\n"
                      "6. Exit program. \n")
                option = input(">>>")
                if option == "1":
                    studentID = input("Insert student's ID : ")
                    disciplineID = input("Insert the discipline's ID : ")
                    gradeValue = input("Insert grade value : ")
                    self.__UIAddGrade(studentID, disciplineID, gradeValue)
                if option == "2":
                    self.__UIListGrades()
                if option == "3":
                    self.__UIFailingStudents()
                if option == "4":
                    self.__UIStudentsRankings()
                if option == "5":
                    self.__UIDisciplinesRankings()
                if option == "6":
                    return
            if command == "4":
                self.userInterface_undo()
            if command == "5":
                self.userInterface_redo()
            if command == "6":
                return
