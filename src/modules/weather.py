from twisted.python import log

from module import ModuleBaseClass


class Weather(ModuleBaseClass):
    invocation = 'w'

    def run(self, *args, **kwargs):
        log.msg(args)
        return 'Disavowed hasn\'t added the fucking weather yet.'



module = Weather
