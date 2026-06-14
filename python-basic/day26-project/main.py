from student_utils import get_students, print_students, get_average, get_pass_students
from file_utils import write_students, read_students

students = get_students()
write_students(students)

print("save students to students.txt")

loaded_students = read_students()

print("upload")

print_students(loaded_students)
get_average(loaded_students)
get_pass_students(loaded_students)

print("average:", get_average)
print("pass students:", get_pass_students)