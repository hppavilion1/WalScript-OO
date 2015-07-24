from classes import *

def lex(script):
    r = []
    script = script.split(';')[:-1]
    for x in range(len(script)):
        varsplit = script[x].split('=', 1)
        if len(varsplit) == 2:
            var = varsplit[0]
            com = varsplit[1]
        else:
            var = 'global}public}ret'
            com = varsplit[-1]
        
        comsplit = com.split('}')[:-1]
        com = comsplit[0].strip()
        args = comsplit[1:]
        for x in range(len(args)):
            args[x] = arg(args[x])

        varsplit = var.split('}')
        var = varsplit[-1]
        mods = varsplit[:-1]

        script[x] = command(mods, var, com, args)

    return script

if __name__ == '__main__':
    print(repr(lex(input())))
