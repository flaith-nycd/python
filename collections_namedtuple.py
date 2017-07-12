# For collection, have a look at :
# https://my.smeuh.org/al/blog/astuces-collections-python
# http://alexmarandon.com/articles/python_collections_tips/
from collections import namedtuple
import csv

# EmployeeRecord = namedtuple('EmployeeRecord', 'name, age, title, department, paygrade')
# OR
EmployeeRecord = namedtuple('EmployeeRecord', ['name', 'age', 'title', 'department', 'paygrade'])


me = EmployeeRecord(name='me', age=22, title='guess', department='somewhere', paygrade='what?')
you = EmployeeRecord(name='you', age=20, title='guess again', department='somewhere', paygrade='why?')
print('Fields for the namedtuple "{}"'.format(EmployeeRecord.__name__))
print(EmployeeRecord._fields)
print()
print('Fields by index:')
for meyou in [me, you]:
    print('{} is {} years old and {} {}'.format(meyou.name, meyou.age, meyou.title, meyou.paygrade))

print()

# 'map()' : Return an iterator that applies function to every item of iterable, yielding the results.
#           If additional iterable arguments are passed, function must take that many arguments and is applied
#           to the items from all iterables in parallel. With multiple iterables, the iterator stops when the
#           shortest iterable is exhausted. For cases where the function inputs are already arranged into
#           argument tuples, see itertools.starmap().
#
# '_make' : Class method that makes a new instance from an existing sequence or iterable.
print('name           age title                department paygrade')
print('-------------- --- -------------------- ---------- --------------')
for emp in map(EmployeeRecord._make, csv.reader(open("employees.csv", "r"))):
    print('{:14} {:>3} {:20} {:10} {:14}'.format(emp.name, emp.age, emp.title, emp.department, emp.paygrade))
