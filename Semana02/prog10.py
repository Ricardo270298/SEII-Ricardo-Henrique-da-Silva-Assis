import os
from datetime import datetime
print (dir(os))
print (os.getcwd())

os.chdir('/home/ricardo/Desktop/')

os.mkdir('Semana02-2')
os.makedirs('Semana02-2/Sub-Dir-1')
os.rmdir('Semana02-2')
os.removedirs('Semana02-2/Sub-Dir-1')
os.rename('test.odt', 'demo.odt')

mod_time = os.stat('demo.ods').st_mtime
print(os.stat('demo.ods').st_size)
print(daterime.fromtimestamp(mod_time))

print(os.listdir())

for dirpath, dirnames, filenames in os.walk('/home/ricardo/Desktop/')
	print('Current Path:', dirpath)
	print('Directories:', dirname)
	print('Files:', filenames)
	print()

print(os.environ.get('HOME'))

'test.txt'

file_path = os.path.join(os.environ.get('HOME') + 'test.txt')
print(file_path)

print(os.path.basename('/tmp/test.txt'))
print(os.path.dirname('/tmp/test.txt'))
print(os.path.split('/tmp/test.txt'))
print(os.path.exists('/tmp/test.txt'))
print(os.path.isdir('/tmp/test.txt'))
print(os.path.isfile('/tmp/test.txt'))
print(os.path.splitext('/tmp/test.txt'))
print(dir(os.path))





