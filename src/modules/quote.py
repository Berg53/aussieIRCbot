from twisted.python import log

from module import ModuleBaseClass


class Quote(ModuleBaseClass):
    invocation = 'save'

    def _write_message_to_file(self, message, target):
        with open(target, 'a') as f:
            quote = self.config.QUOTE_FORMAT.format(
                    message.time, message.sender, message.text)
            f.write(quote)
            log.msg('Quote added: {}'.format(quote))

    def run(self, query):
        for m in self.bot.messages:
            if query.strip() in m:
                self._write_message_to_file(message=m, target='quotes.txt')
                return 'Saved: "{}"'.format(m.text)
        else:
            log.msg('Quote not found')
            return self.config.QUOTE_NOT_FOUND_MESSAGE


module = Quote
