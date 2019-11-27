from exceptions import ValidError


class studentValidator(object):

    def validateStudent(self, student):
        errors = ""
        if student.getID() < 0:
            errors += "Student ID cannot be negative\n"
        if student.getName() == "":
            errors += "Student name cannot be empty\n"
        if len(errors) > 0:
            raise ValidError(errors)


class disciplineValidator(object):

    def validateDiscipline(self, discipline):
        errors = ""
        if discipline.getID() < 0:
            errors += "Discipline ID cannot be negative\n"
        if discipline.getName() == "":
            errors += "Discipline name cannot be empty"
        if len(errors) > 0:
            raise ValidError(errors)


class gradeValidator(object):

    @staticmethod
    def validateGrade(grade):
        errors = ""
        if grade.getStudentID() < 0:
            errors += "Student ID cannot be negative\n"
        if grade.getDisciplineID() < 0:
            errors += "Discipline ID cannot be negative\n"
        if grade.getGrade() < 0 or grade.getGrade() > 10:
            errors += "Grade must be between 1-10"
        if len(errors) > 0:
            raise ValidError(errors)


