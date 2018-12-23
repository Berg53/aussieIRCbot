from importlib import import_module

import config as c


def get_module(name):
    return import_module(c.MODULE_LOCATION + '.' + name).module


def setup_modules():
    modules = {}
    for m in c.INSTALLED_MODULES:
        module = get_module(m)
        modules[module.invocation] = module()
    return modules


class ModuleBaseClass:
    """
    Base class for modules
    """
    invocation = ''

    def __init__(self, *args, **kwargs):
        self.config = c

    def execute(self, bot, *args, **kwargs):
        raise NotImplementedError
