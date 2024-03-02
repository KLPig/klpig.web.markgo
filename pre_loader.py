import errors
import code_spliter

file = open('target.mgtgt').read() + '.mg'

code = open(file).read()

if code.split('\n')[0] != 'LANGUAGE MARKGO':
    raise errors.MarkGoLanguageError()

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
            if len(cmd) == 3:
                p = loaded_code.replace(f"<{c}>",
                                        f'"<{cmd[1]} id={cmd[2]}></{cmd[1]}>"')
                loaded_code = p
            else:
                raise errors.MarkGoArgumentNumberError(3, len(cmd))
        else:
            raise errors.MarkGoProcessorError(cmd[0])
        continue
    c += cc
    if cc == '<':
        c = ''

ans = '\n'.join(code_spliter.split(loaded_code))

open(f'{file.split(".")[0]}.mgins', 'w').write(ans)
