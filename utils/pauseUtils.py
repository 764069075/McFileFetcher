from os import name, system


def waitforkey():
    if name == 'nt':
        system('pause')
    else:
        input("按回车继续...")