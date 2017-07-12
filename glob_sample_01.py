import glob

for filename in glob.glob('apple/**', recursive=True):
    print('  {}'.format(filename))
