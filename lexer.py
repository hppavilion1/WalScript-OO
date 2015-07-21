from classes import *

def lex(script):
    r = []
    script = script.split(';')
    for x in range(len(script)):
        varsplit = script[x].split('=', 1)
        var = varsplit[0]
        com = varsplit[1]
        
        comsplit = com.split('}')
        command = comsplit[0].strip()
        args = comsplit[1:]

        varsplit = var.split('}')
        var = varsplit[-1]
        mods = varsplit[:-1]

        script[x]

    return script

if __name__ == '__main__':
    
