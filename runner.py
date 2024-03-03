import time

import MarkGoErrors
import pre_loader
import modular
import compiler
import os
import MarkGoErrors

if open('./target.mgtgt').read() == '':
    file = input('File to compile: ')
else:
    file = open('./target.mgtgt').read()

file = file.split('.')[0]

if not os.path.isfile(f'{file}.mg'):
    raise MarkGoErrors.MarkGoLanguageError()

print('Writing target file..')
open('target.mgtgt', 'w').write(file)
print('Done writing.')

time.sleep(0.1)

print('Pre-loading..')
pre_loader.load()
print(f'Loading done, {file}.mgins was created.')

time.sleep(0.3)

print('Modularizing...')
modular.mod()
print(f'Modularization done, {file}.mgo was created.')

time.sleep(0.3)

print('Compiling..')
time.sleep(1.5)
compiler.compile_ins()
print(f'Compilation was done, please check for {file}.html.')
