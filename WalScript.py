from include import *
import os.path
import sys
import lexer

libpath = 'Lib/'

def evalarg(exp, env):
    return exp.a

def evalargs(args, env):
    for x in range(len(args)):
        args[x] = evalarg(args[x], env) #Will change later
    return(args)

class functionConstruct:
    def _import(self, env, *args):
        if os.path.isfile(libpath+args[0]):
            if args[0].endswith('.py'):
                exec(open(libpath+args[0]).read()) #Build new functions from a file
                return((True, env))
            
            elif args[0].endswith('.wal'):
                env=run(open(libpath+args[0]).read(), env)
                return((True, env))

            elif os.path.isfile(args[0]+'.wal'):
                env=run(open(libpath+args[0]+'.wal').read(), env)
                return((True, env))
            
            else:
                return((False, env))
        else:
            return((False, env))

evaluator = functionConstruct()

def run(script, env={'__loops__':[], '__functions__':{}}, lex=True):
    script = lexer.lex(script)
    i = 0
    c = None

    ignore = ['return', 'debug', 'endfunc']

    while c not in ignore:
        o = (None, env)

        v = script[i].varname
        c = script[i].com
        args = []
        args = evalargs(script[i].args, env)
        print(script[i].args)

        if '_'+c in dir(evaluator):
            o = getattr(evaluator, '_'+c)(env, *args)

if __name__ == '__main__':
    run(input()+';')
