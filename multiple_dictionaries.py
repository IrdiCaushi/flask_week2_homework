# Irdi Caushaj
# HomeWork 2


students_dict = {
    
       'first_dict': {
            'name': 'Irdi Caushaj',
            'school': 'AUBG',
            'grades': [90.5, 97.2, 87.5]
        },
        'second_dict': {
            'name': 'Someone Some',
            'school': 'AUBG',
            'grades': [50.3, 60.9, 77.5]
        },
        'third_dict': {
            'name': 'Somebody Body',
            'school': 'AUBG',
            'grades': [63.5, 45.2, 78.2]
        }
}

for keys in students_dict:
    print("student_name-> ",students_dict[keys]['name'])
    print("average_grade-> ",sum(students_dict[keys]['grades'])/len(students_dict[keys]['grades']),"\n\n")
