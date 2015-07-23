class InvalidModifier(Exception):
    pass

class ConstantReassignment(Exception):
    pass

class InvalidArgType(Exception):
    pass

class variable:
    def __init__(self, attributes={'local'}):
        self.attr = '}'.join(attributes)
        if 'local' in attributes:
            self.globality = 0
            attributes.remove('local')
        elif 'global' in attributes:
            self.globality = 1
            attributes.remove('global')
        else:
            self.globality = 1
        
        if self.globality:
            if 'private' in attributes:
                self.referencability = 0
                attributes.remove('private')
            elif 'protected' in attributes:
                self.referencability = 1
                attributes.remove('protected')
            elif 'public' in attributes:
                self.referencability = 2
                attributes.remove('public')
            else:
                raise InvalidModifier('No accessibility modifier')

        if 'final' in attributes:
            self.isFinal = True
            attributes.remove('final')
        else:
            self.isFinal = False

        if 'static' in attributes:
            self.staticness = 1
            attributes.remove('static')
        else:
            self.staticness = 0
        
        if 'constant' in attributes:
            self.isconst = True
            attributes.remove('constant')
        else:
            self.isconst = False

        if len(attributes) > 0:
            raise InvalidModifier('Modifier '+list(attributes)[0]+' used')

    def set(self, value, t):
        self.t = t
        if self.const:
            self.value = value
        else:
            raise ConstantReassignment('Tried to reassign constant')

    def __repr__(self):
        return(attr+' variable('+str(self.value)+')')

class arg:
    def __init__(self, a):
        if a[0] == '{':
            if a[1] == 'a':
                self.t = 'exp'
            elif a[1] == 'b':
                self.t = 'bool'
            elif a[1] == 's':
                self.t = 'str'
            else:
                raise InvalidArgType('Invalid argtype declaration '+a[1])
            self.a = a[2:]
        else:
            self.t = 'raw'
            self.a = a
    def __repr__(self):
        return(' Arg('+self.t+', '+self.a+')')
            

class command:
    def __init__(self, varattr, var, com, args):
        self.varname = var
        self.var = variable(set(varattr))
        self.com = com
        self.args = args
        for x in range(len(args)):
            args[x] = arg(args[x])

    def __repr__(self):
        return('Command('+'variable('+self.var.attr.replace('}', ', ')+', '+self.varname+'), '+self.com+', '+', '.join([str(a) for a in self.args])+')')
