from modular import *

file = open('target.mgtgt').read() + '.mgo'

head = ''
body = ''


data = {}


def run_ins(inst: list[Actions | Functions | VariablesSet | Nest]):
    global head, body, data
    for cmd in inst:
        if type(cmd) is Actions:
            f = cmd.det.split(':')
            arg = f[1]
            if arg[0] == '"':
                arg = arg[1:].removesuffix('"')
            elif arg[0] == '?':
                arg = data[arg[1:]]
            if cmd.obj == 'HEAD':
                if cmd.ins == 'set':
                    if f[0] == 'title':
                        head += f'<title>{arg}</title>\n'
                elif cmd.ins == 'import':
                    if f[0] == 'js':
                        head += f'<script src="{arg}"></script>\n'
                    elif f[0] == 'css':
                        head += f'<link rel="stylesheet" href="{arg}">\n'
            elif cmd.obj == 'BODY':
                if cmd.ins == 'add':
                    if f[0] == 'child':
                        body += arg + '\n'
        elif type(cmd) is Functions:
            if cmd.func == 'CREATE':
                data[cmd.arg] = ''
        elif type(cmd) is VariablesSet:
            arg = cmd.val
            if arg[0] == '"':
                arg = arg[1:].removesuffix('"')
            elif arg[0] == '?':
                arg = data[arg[1:]][1:].removesuffix('"')
            data[cmd.obj] = arg
        elif type(cmd) is Nest:
            if cmd.func == 'FOR':
                if cmd.arg['type'] == 'iter':
                    for i in range(int(cmd.arg['st']), int(cmd.arg['en'])):
                        data[cmd.arg['in']] = int(i)
                        run_ins(cmd.code)


if __name__ == '__main__':
    ins = pickle.load(open(file, 'rb'))
    run_ins(ins)
    open(f'{file.split(".")[0]}.html', 'w').write(
        f'<!DOCTYPE html>\n<html>\n<head>\n{head}\n</head>\n'
        f'<body>\n{body}\n</body>\n</html>'
    )

