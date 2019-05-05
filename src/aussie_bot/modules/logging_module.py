import datetime

def log_print(line):
    try:
        logs_file = ('/home/berg/bin/aussieIRCbot/src/aussie_bot/log/log.txt')
        with open(logs_file, 'a') as f:
            f.write(line)
            f.close()
        print( "Yeth MATHTA  {}".format(line))
    except Exception as e:
        print(e)
        return "well thats not in the logs Master {}"

def handler(connection, event):
    if event.arguments and event.arguments[0].startswith("") and event.target == "##aussies":
        log_print('[{0:%Y-%m-%d %H:%M:%S}]'.format(datetime.datetime.now()) + " <{}> {}\n".format(event.source.nick,event.arguments[0]))
        print(event.target)


def get_handlers():
    return (("pubmsg", handler),)
