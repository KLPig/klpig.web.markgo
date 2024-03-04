import time

import pre_loader
import modular
import compiler
import os
import MarkGoErrors

file = input('File to compile: ')

dirname = os.path.dirname(file) + '/'

file = file.removeprefix(dirname).split('.')[0]

if not os.path.isfile(f'{os.path.join(dirname, file)}.mg'):
    raise MarkGoErrors.MarkGoLanguageError()

time.sleep(0.1)

print('Pre-loading..')
pre_loader.load(dirname, file)
print(f'Loading done, {file}.mgins was created.')

time.sleep(0.3)

print('Modularizing...')
modular.mod(dirname, file)
print(f'Modularization done, {file}.mgo was created.')

time.sleep(0.3)

print('Compiling..')
time.sleep(1.5)
compiler.compile_ins(dirname, file)
print(f'Compilation was done, please check for {file}.html.')
