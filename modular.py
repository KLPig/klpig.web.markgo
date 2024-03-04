import MarkGoErrors
import code_spliter
import pickle
import os


class Instructions:
    pass


def modularize(code: str) -> list[Instructions]: pass


class Actions(Instructions):
    def __init__(self, cmd: str):
        self.cmd = cmd
        c = cmd.split('.')
        try:
            self.obj = c[0]
            self.ins = c[1]
            self.det = c[2]
        except IndexError:
            raise MarkGoErrors.MarkGoArgumentNumberError(3, len(c))


class VariablesSet(Instructions):
    def __init__(self, cmd: str):
        self.cmd = cmd
        c = cmd.split(' ')
        try:
            self.obj = c[0]
            self.op = c[1]
            self.val = ' '.join(c[2:])
            if self.op != '=' and self.op != '+':
                raise MarkGoErrors.MarkGoSyntaxError(c[1])
        except IndexError:
            raise MarkGoErrors.MarkGoArgumentNumberError(3, len(c))


class Functions(Instructions):
    def __init__(self, cmd: str):
        self.cmd = cmd
        c = cmd.split(' ')
        try:
            self.func = c[0]
            self.arg = c[1:]
        except IndexError:
            raise MarkGoErrors.MarkGoArgumentNumberError(2, len(c))


class Nest(Instructions):
    def __init__(self, cmd: str):
        self.cmd = cmd
        pre = ''
        aft = ''
        b = False
        for i in range(len(cmd)):
            if cmd[i] == '{':
                b = True
                continue
            elif cmd[i] == '}':
                continue
            if b:
                aft += cmd[i]
            else:
                pre += cmd[i]
        c = pre.split(' ')
        # print(pre, aft)
        try:
            self.func = c[0]
            self.arg = {}
            for i in c[1:]:
                self.arg[i.split('=')[0]] = i.split('=')[1]
            s = '\n'.join(code_spliter.split(aft))
            self.code = modularize(s)
        except IndexError:
            raise MarkGoErrors.MarkGoArgumentNumberError(2, len(c))


def modularize(code: str) -> list[Instructions]:
    cmd = code.removesuffix('\n').split('\n')
    cmds = []
    for c in cmd:
        if c[0] == '!':
            cmds.append(Actions(c[1:]))
        elif c[0] == '?':
            cmds.append(VariablesSet(c[1:]))
        elif c[0] == '#':
            cmds.append(Functions(c[1:]))
        elif c[0] == '@':
            cmds.append(Nest(c[1:]))
        else:
            raise MarkGoErrors.MarkGoSyntaxError(c[0])
    return cmds


def mod(dirname, filename):
    file = os.path.join(dirname, filename)
    s = modularize(open(file + '.mgins').read())
    pickle.dump(s, open(file + '.mgo', 'wb'))

