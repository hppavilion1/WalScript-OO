class InvalidModifier(Exception):
    pass

class ConstantReassignment(Exception):
    pass

class InvalidArgType(Exception):
    pass

class variable:
    def __init__(self, attributes={'local'}):
        if 'local' in attributes:
            self.globality = 0
        elif 'global' in attributes:
            self.globality = 1
        else:
            self.globality = 1
        attributes.remove('local')
        attributes.remove('global')
        
        if not self.local:
            if 'private' in attributes:
                self.referencability = 0
            elif 'protected' in attributes:
                self.referencability = 1
            elif 'public' in attributes:
                self.referencability = 2
            else:
                raise InvalidModifier('No accessibility modifier')
            attributes.remove('private')
            attributes.remove('protected')
            attributets.remove('public')

        if 'final' in attributes:
            self.isFinal = True
        else:
            self.isFinal = False
        attributes.remove('final')

        if 'static' in attributes:
            self.staticness = 1
        else:
            self.statcness = 0
        attributes.remove('static')

        if 'constant' in attributes:
            self.isconst = True
        else:
            self.isconst = False
        attributes.remove('constant')

        if len(attributes) > 0:
            raise InvalidModifier('Modifier '+list(attributes)[0]+' used')

    def set(self, value, t):
        self.t = t
        if self.const:
            self.value = value
        else:
            raise ConstantReassignment('Tried to reassign constant')

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
            

class command:
    def __init__(self, varattr, var, com, args):
        self.varname = var
        self.var = variable(set(varattr))
        self.com = com
        self.args = args
        for x in range(len(args)):
            args[x] = arg(args[x])
