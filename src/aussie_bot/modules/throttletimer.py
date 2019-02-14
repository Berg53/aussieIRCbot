import time
name_timers = {}
def handler(connection, event):
    if event.arguments and (event.arguments[0].startswith("!n") or event.arguments[0].startswith("!t") or event.arguments[0].startswith("my place") or event.arguments[0].startswith("!q")):
        try:
            gap = time.time() - name_timers[(event.source.nick)]
        except KeyError:
            gap = 6
        name_timers.update({(event.source.nick): time.time()})
        if gap <= 5:
            event.arguments = ""
        
        
        print(name_timers)
        return event.arguments, name_timers


def get_handlers():
    return (("pubmsg", handler),)
