import time
import os

file = input('File to compile: ')
file = file.split('.')[0]

print()

print('Writing target file..')

open('target.mgtgt', 'w').write(file)

print('Done writing.')

print()

time.sleep(0.1)

print('Pre-loading..')

os.system('python pre_loader.py')

print(f'Loading done, {file}.mgins was created.')

print()

time.sleep(0.3)

print('Modularizing...')

os.system('python modular.py')

print(f'Modularization done, {file}.mgo was created.')

print()

time.sleep(0.3)

print('Compiling..')

time.sleep(1.5)

os.system('python compiler.py')

print(f'Compilation was done, please check for {file}.html.')
