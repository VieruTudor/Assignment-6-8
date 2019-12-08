from entities import *
from service import *
from repo import *
import unittest
import coverage

class studentTests(unittest.TestCase):

    def test_studentName_expectedName(self):
        student = Student(1, "Tudor")
        self.assertTrue(student.getName() == "Tudor")

    def test_studentID_expectedID(self):
        student = Student(1, "Tudor")
        self.assertTrue(student.getID() == 1)

    def test_addStudent_correctAdd(self):
        self.__repo = Repo()
        assert len(self.__repo.getAllObjects()) == 0
        student = Student(1, "Tudor")
        self.__repo.addUniqueObject(student)
        assert len(self.__repo.getAllObjects()) == 1

    def testAddUniqueObject(self):
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

    def test_updateStudent_correctUpdate(self):
        self.__repo = Repo()
        student = Student(1, "Tudor")
        self.__repo.addUniqueObject(student)
        newStudent = Student(1, "Tudorr")
        self.__repo.updateObject(newStudent.getID(), newStudent)
        students = self.__repo.getAllObjects()
        assert students[0].getName() == "Tudorr"

    def test_removeStudent_correctRemoval(self):
        self.__repo = Repo()
        student = Student(1, "Tudor")
        self.__repo.addUniqueObject(student)
        self.__repo.removeObject(student.getID())
        assert len(self.__repo.getAllObjects()) == 0


class disciplineTests(unittest.TestCase):

    def test_disciplineID_expectedID(self):
        discipline = Discipline(1, "Biology")
        self.assertTrue(discipline.getID() == 1)

    def test_disciplineName_expectedName(self):
        discipline = Discipline(1, "Biology")
        self.assertTrue(discipline.getName() == "Biology")

    def test_addDiscipline_duplicateID_RepoError(self):
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

    def test_addDiscipline_correctAdd(self):
        self.__repo = Repo()
        assert len(self.__repo.getAllObjects()) == 0
        discipline = Discipline(1, "Tudor")
        self.__repo.addUniqueObject(discipline)
        assert len(self.__repo.getAllObjects()) == 1

    def test_updateDiscipline_correctUpdate(self):
        self.__repo = Repo()
        discipline = Discipline(1, "Biology")
        self.__repo.addUniqueObject(discipline)
        newDiscipline = Discipline(1, "Biologyy")
        self.__repo.updateObject(newDiscipline.getID(), newDiscipline)
        students = self.__repo.getAllObjects()
        assert students[0].getName() == "Biologyy"

    def test_removeDiscipline_correctRemoval(self):
        self.__repo = Repo()
        discipline = Discipline(1, "Biology")
        self.__repo.addUniqueObject(discipline)
        self.__repo.removeObject(discipline.getID())
        assert len(self.__repo.getAllObjects()) == 0


class gradeTests(unittest.TestCase):

    def test_gradeStudentID_expectedID(self):
        grade = Grade(1, 1, 10)
        self.assertTrue(grade.getStudentID() == 1)

    def test_gradeDisciplineID_expectedID(self):
        grade = Grade(1, 2, 10)
        self.assertTrue(grade.getDisciplineID() == 2)

    def test_gradeValue_expectedValue(self):
        grade = Grade(1, 1, 10)
        self.assertTrue(grade.getGrade() == 10)


if __name__ == "__main__":
    unittest.main()
