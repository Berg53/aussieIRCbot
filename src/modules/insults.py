from module import ModuleBaseClass


class Insult(ModuleBaseClass):
    invocation = 'w'

    def run(self, *args, **kwargs):
        return 'Insults not found'


module = Insult
