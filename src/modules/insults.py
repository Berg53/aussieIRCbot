from module import ModuleBaseClass


class Insult(ModuleBaseClass):
    invocation = 'w'

    def execute(self, *args, **kwargs):
        return 'Insults not found'


module = Insult
