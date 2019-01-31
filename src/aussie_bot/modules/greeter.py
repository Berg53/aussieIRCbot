RESPONSES = {"o/", r"\o"}


def handler(connection, event):
    if event.arguments and event.arguments[0] in RESPONSES:
        response = {event.arguments[0]} ^ RESPONSES
        if response:
            connection.privmsg(event.target, list(response)[0])


def get_handlers():
    return (("pubmsg", handler),)
