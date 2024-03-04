from modular import *

head = ''
body = ''


data: dict[str, str] = {}


def find_val(name: str, cmd: str = None):
    if name[0] == '?':
        try:
            return data[name[1:]]
        except KeyError:
            raise MarkGoErrors.MarkGoUndefinedError(name[1:], 'variable', cmd)
    else:
        return name.removesuffix('"').removeprefix('"')


def run_ins(inst: list[Actions | Functions | VariablesSet | Nest]):
    global head, body, data
    for cmd in inst:
        if type(cmd) is Actions:
            f = cmd.det.split(':')
            arg = find_val(f[1], cmd.cmd)
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
            arg = find_val(cmd.val, cmd.cmd)
            if cmd.op == '=':
                data[cmd.obj] = arg
            elif cmd.op == '+':
                data[cmd.obj] = data[cmd.obj].replace('</', f'{arg}</',  1)
        elif type(cmd) is Nest:
            if cmd.func == 'FOR':
                if cmd.arg['type'] == 'iter':
                    for i in range(int(find_val(cmd.arg['st'])), int(find_val(cmd.arg['en']))):
                        data[cmd.arg['in']] = str(i)
                        run_ins(cmd.code)


if __name__ == '__main__':
    ins = pickle.load(open(file, 'rb'))
    run_ins(ins)
    open(f'{file.split(".")[0]}.html', 'w').write(
        f'<!DOCTYPE html>\n<html>\n<head>\n{head}\n</head>\n'
        f'<body>\n{body}\n</body>\n</html>'
    )


def compile_ins(dirname, filename):
    file = os.path.join(dirname, filename)
    ins = pickle.load(open(file + '.mgo', 'rb'))
    run_ins(ins)
    open(file + '.html', 'w').write(
        f'<!DOCTYPE html>\n<html>\n<head>\n{head}\n</head>\n'
        f'<body>\n{body}\n</body>\n</html>'
    )
