from module import ModuleBaseClass


class Weather(ModuleBaseClass):
    invocation = 'w'

    def execute(self, *args, **kwargs):
        return 'Weather not found'


module = Weather
