from School import School, ClassRoom, Subject
from Persons import Student, Teacher


def main():
    school = School("zilla", "fp")

    # add class
    eight = ClassRoom("eight")
    school.add_classroom(eight)

    nine = ClassRoom("nine")
    school.add_classroom(nine)

    ten = ClassRoom("ten")
    school.add_classroom(ten)

    # add students
    abir = Student("abir", eight)
    school.student_admission(abir)

    akash = Student("akash", eight)
    school.student_admission(akash)

    araf = Student("araf", eight)
    school.student_admission(araf)
    # subjects
    physics_teacher = Teacher("Shahjahan Tapon Rana")
    physics = Subject("physics", physics_teacher)
    eight.add_subject(physics)

    chemistry_teacher = Teacher("Haradon Nag")
    chemistry = Subject("chemistry", chemistry_teacher)
    eight.add_subject(chemistry)

    biology_teacher = Teacher("Azmal Sir")
    biology = Subject("biology", biology_teacher)
    eight.add_subject(biology)

    eight.take_semester_final()

    print(school)


if __name__ == "__main__":
    main()
