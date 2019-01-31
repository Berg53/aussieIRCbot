def parse_int(string, default=0):
    try:
        return int(string)
    except ValueError:
        return default
