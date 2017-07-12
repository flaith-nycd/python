our_list = range(10)

print("Our list = {}".format(list(our_list)))

# map our list to have new values by using lambda
map_list = map(lambda x: x**2, our_list)
print("Mapped list = {}".format(list(map_list)))

# filter our list to have even
filter_list = filter(lambda x: x % 2 == 0, our_list)
print("Filtered list (even) = {}".format(list(filter_list)))

# Use comprehension list to be faster than using map & filter
# List comprehension example:
# indices_all = [index for index, search in enumerate(dsk.memdisk) for what in values_to_find if search == what]
map_list = [x**2 for x in our_list]
print("Mapped list = {}".format(map_list))

filter_list = [x for x in our_list if x % 2 == 0]
print("Filtered list (even) = {}".format(filter_list))
