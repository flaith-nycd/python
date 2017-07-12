# https://wiki.python.org/moin/HowTo/Sorting
# https://docs.python.org/3.6/howto/sorting.html#sortinghowto
# https://developers.google.com/edu/python/sorting
etudiants = [
    ("Clément", 14, 16),
    ("Charles", 12, 15),
    ("Oriane", 14, 18),
    ("Thomas", 11, 12),
    ("Damien", 12, 15),
]

print(sorted(etudiants))

sorted_etudiant_second_column = sorted(etudiants, key=lambda colonnes: colonnes[2])

print(sorted_etudiant_second_column)

student_tuples = [
    ('john', 'A', 15),
    ('jane', 'B', 12),
    ('dave', 'B', 10),
]
print(sorted(student_tuples, key=lambda student: student[2]))  # sort by age
# [('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]


# https://docs.python.org/3.6/howto/sorting.html#sortinghowto
class Student:
    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age

    def __repr__(self):
        return repr(('Student: {}, Grade: {}, age: {}'.format(self.name.capitalize(), self.grade, self.age)))

student_objects = [
    Student('john', 'A', 15),
    Student('jane', 'B', 12),
    Student('dave', 'B', 10),
]
print(sorted(student_objects, key=lambda student: student.age))  # sort by age
print(sorted(student_objects, key=lambda student: student.age, reverse=True))  # sort by age descending
# ['Student: Dave, Grade: B, age: 10', 'Student: Jane, Grade: B, age: 12', 'Student: John, Grade: A, age: 15']
