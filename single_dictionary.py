# Irdi Caushaj
# HomeWork 2

from module import dict_modules

student_dict = {
    'name': 'Irdi Caushaj',
    'school': 'AUBG',
    'grades': [78.3, 85.5, 90.9]
}

print(student_dict,"\n\n")

grades_string = input("Enter the grades you want to upload separated by ',':\n\n")

grades_float = list(map(float, grades_string.split(",")))

for grades in grades_float:
    dict_modules.add_grade(student_dict,grades)

print(student_dict)