def handler(connection, event):
    if event.arguments and event.arguments[0].startswith("!r"):
        connection.privmsg(event.target, "\x02\x034 Rule one:  \x035  No Banninating!")
        connection.privmsg(event.target, "\x02\x034 Rule two:  \x035  See rule one")
        connection.privmsg(
            event.target,
            "\x02\x034 Rule three: \x035 It's against the rules to enforce em"
        )
        connection.privmsg(
            event.target,
            "\x02\x034 Rule four: \x035 Free speech is you right in this channel if you truly beleave your right go fuck yourself THE BOT IS ALWAYS RIGHT"
        )


def get_handlers():
    return (("pubmsg", handler),)
