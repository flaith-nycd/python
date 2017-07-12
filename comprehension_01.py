# Following map_filter_01.py

# Comprehension dictionnary
dic_number = {10112: 'jean', 15324: 'eric', 21654: 'martine'}
print(dic_number)
print('User with number 15324: {}'.format(dic_number[15324]))

print()
# Now we want to know the number for a name
# We are converting key to value and value to key
dic_name = {dic_number[key]: key for key in dic_number}

print(dic_name)
print('User "martine" have the number: {}'.format(dic_name['martine']))
