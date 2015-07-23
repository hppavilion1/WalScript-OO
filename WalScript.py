from include import *
import os.path
import sys
import lexer

libpath = 'Lib/'

def evalarg(exp, env):
    pass

def evalargs(args, env):
    pass

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
        args = evalargs(script[i].args, env)
