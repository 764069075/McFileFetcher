from os import name, system


def wait_for_key():
    if name == 'nt':
        system('pause')
    else:
        input("按回车继续...")