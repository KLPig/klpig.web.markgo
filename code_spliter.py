import MarkGoErrors


def split(code: str) -> list:
    lcode = []
    l = ''
    x = 0

    for i in range(len(code)):
        if code[i] == '{':
            x += 1
        elif code[i] == '}':
            x -= 1
            if x < 0:
                raise MarkGoErrors.MarkGoSyntaxError('}')
        elif code[i] == ';' and x == 0:
            lcode.append(l)
            l = ''
            continue
        l += code[i]

    return lcode
