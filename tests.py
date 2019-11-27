from entities import *
from service import *
from repo import *


class studentTests():
    def __init__(self):
        pass

    @staticmethod
    def __test_studentName_expectedName():
        student = Student(1, "Tudor")
        assert student.getName() == "Tudor"

    @staticmethod
    def __test_studentID_expectedID():
        student = Student(1, "Tudor")
        assert student.getID() == 1

    def __test_addStudent_correctAdd(self):
        self.__repo = Repo()
        assert len(self.__repo.getAllObjects()) == 0
        student = Student(1, "Tudor")
        self.__repo.addUniqueObject(student)
        assert len(self.__repo.getAllObjects()) == 1

    def __test_addStudent_duplicateID_RepoError(self):
        self.__repo = Repo()
        assert len(self.__repo.getAllObjects()) == 0
        student = Student(1, "Tudor")
        self.__repo.addUniqueObject(student)
        try:
            duplicateStudent = Student(1, "Stefan")
            self.__repo.addUniqueObject(duplicateStudent)
            assert False
        except RepoError as error:
            print(str(error))
        assert len(self.__repo.getAllObjects()) == 1

    def __test_updateStudent_correctUpdate(self):
        self.__repo = Repo()
        student = Student(1, "Tudor")
        self.__repo.addUniqueObject(student)
        newStudent = Student(1, "Tudorr")
        self.__repo.updateObject(newStudent.getID(), newStudent)
        students = self.__repo.getAllObjects()
        assert students[0].getName() == "Tudorr"

    def __test_removeStudent_correctRemoval(self):
        self.__repo = Repo()
        student = Student(1, "Tudor")
        self.__repo.addUniqueObject(student)
        self.__repo.removeObject(student.getID())
        assert len(self.__repo.getAllObjects()) == 0

    def runAllTests(self):
        self.__test_studentID_expectedID()
        self.__test_studentName_expectedName()
        self.__test_addStudent_correctAdd()
        self.__test_addStudent_duplicateID_RepoError()
        self.__test_updateStudent_correctUpdate()
        self.__test_removeStudent_correctRemoval()


class disciplineTests():
    def __init__(self):
        pass

    @staticmethod
    def __test_disciplineID_expectedID():
        discipline = Discipline(1, "Biology")
        assert discipline.getID() == 1

    @staticmethod
    def __test_disciplineName_expectedName():
        discipline = Discipline(1, "Biology")
        assert discipline.getName() == "Biology"

    def __test_addDiscipline_duplicateID_RepoError(self):
        self.__repo = Repo()
        assert len(self.__repo.getAllObjects()) == 0
        discipline = Discipline(1, "Biology")
        self.__repo.addUniqueObject(discipline)
        try:
            duplicateDiscipline = Student(1, "History")
            self.__repo.addUniqueObject(duplicateDiscipline)
            assert False
        except RepoError as error:
            print(str(error))
        assert len(self.__repo.getAllObjects()) == 1

    def __test_addDiscipline_correctAdd(self):
        self.__repo = Repo()
        assert len(self.__repo.getAllObjects()) == 0
        discipline = Discipline(1, "Tudor")
        self.__repo.addUniqueObject(discipline)
        assert len(self.__repo.getAllObjects()) == 1

    def __test_updateDiscipline_correctUpdate(self):
        self.__repo = Repo()
        discipline = Discipline(1, "Biology")
        self.__repo.addUniqueObject(discipline)
        newDiscipline = Discipline(1, "Biologyy")
        self.__repo.updateObject(newDiscipline.getID(), newDiscipline)
        students = self.__repo.getAllObjects()
        assert students[0].getName() == "Biologyy"

    def __test_removeDiscipline_correctRemoval(self):
        self.__repo = Repo()
        discipline = Discipline(1, "Biology")
        self.__repo.addUniqueObject(discipline)
        self.__repo.removeObject(discipline.getID())
        assert len(self.__repo.getAllObjects()) == 0

    def runAllTests(self):
        self.__test_disciplineID_expectedID()
        self.__test_disciplineName_expectedName()
        self.__test_addDiscipline_correctAdd()
        self.__test_addDiscipline_duplicateID_RepoError()
        self.__test_updateDiscipline_correctUpdate()
        self.__test_removeDiscipline_correctRemoval()


class gradeTests():
    def __init__(self):
        pass

    @staticmethod
    def __test_gradeStudentID_expectedID():
        grade = Grade(1, 1, 10)
        assert grade.getStudentID() == 1

    @staticmethod
    def __test_gradeDisciplineID_expectedID():
        grade = Grade(1, 2, 10)
        assert grade.getDisciplineID() == 1

    @staticmethod
    def __test_gradeValue_expectedValue():
        grade = Grade(1, 1, 10)
        assert grade.getGrade() == 10

    def runAllTests(self):
        self.__test_gradeDisciplineID_expectedID()
        self.__test_gradeStudentID_expectedID()
        self.__test_gradeValue_expectedValue()
