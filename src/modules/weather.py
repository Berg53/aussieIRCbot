from module import ModuleBaseClass


class Weather(ModuleBaseClass):
    invocation = 'w'

    def run(self, *args, **kwargs):
        return 'Weather not found'


module = Weather
