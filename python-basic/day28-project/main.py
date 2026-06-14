from student_utils import get_number, get_students, print_students, get_average, get_passer, get_highest_person
from file_utils import save_students, read_students

students = get_students()
save_students(students)

print("students saved to students.csv")

loaded_students = read_students()
if len(loaded_students) > 0:
    print_students(loaded_students)
    average = get_average(loaded_students)
    passer = get_passer(loaded_students)
    highest_person = get_highest_person(loaded_students)
    print("average:", average)
    print("passer:", passer)
    print("highest student:", highest_person)
else:
    print("nothing")