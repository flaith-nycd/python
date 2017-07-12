import os

cmd = os.popen('dir')
directories = cmd.read()
directories = directories.split(sep='\n')

for file in directories:
    print(file)
