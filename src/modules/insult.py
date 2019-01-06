import random

from module import ModuleBaseClass


INSULTS_LOCATION = 'src/data/insults.txt'

class Insult(ModuleBaseClass):
    invocation = 'insult'

    def _get_insult(self):
        with open(INSULTS_LOCATION) as f:
            insults = f.readlines()
            return random.choice(insults)

    def run(self, message, *args, **kwargs):
        if message.strip():
            m = '{}, you {}'.format(
                    message, self._get_insult().lower()).strip()
        else:
            m = '{}'.format(self._get_insult())
        return m.strip()


module = Insult
