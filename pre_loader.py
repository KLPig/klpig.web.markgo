import MarkGoErrors
import code_spliter


def load():
    file = open('target.mgtgt').read() + '.mg'

    code = open(file).read()

    if code.split('\n')[0] != 'LANGUAGE MARKGO':
        raise MarkGoErrors.MarkGoLanguageError()

    code = code[16:]

    s = 0
    b = True

    loaded_code = ''

    for i in range(len(code)):
        if code[i] == '\'':
            b = not b
            continue
        if b and code[i] != '\n' and code[i] != '\t':
            loaded_code += code[i]

    c = ''

    p = ''
    for cc in loaded_code:
        if cc == '>':
            cmd = c.split(' ')
            if cmd[0] == 'NEW-ELEMENT':
                if len(cmd) == 2:
                    p = loaded_code.replace(f"<{c}>",
                                            f'"<{cmd[1]}></{cmd[1]}>"')
                    loaded_code = p
                else:
                    raise MarkGoErrors.MarkGoArgumentNumberError(2, len(cmd))
            else:
                raise MarkGoErrors.MarkGoProcessorError(cmd[0])
            continue
        c += cc
        if cc == '<':
            c = ''

    ans = '\n'.join(code_spliter.split(loaded_code))

    open(f'{file.split(".")[0]}.mgins', 'w').write(ans)
