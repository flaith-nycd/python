def dump(filename, **kwargs):
    print("Filename:", filename)
    if len(kwargs) == 2:
        for key, value in kwargs.items():
            print(key.upper(), ":", value)
    else:
        print('Merci de stipuler deux parametres')


dump_option = "32"
org_option = "$0800"

dump("test", nb_byte=dump_option, org=org_option)
