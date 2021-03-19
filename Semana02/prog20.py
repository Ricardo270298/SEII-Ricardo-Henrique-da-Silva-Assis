try:
	f = open('testfile.txt')
	var = bad_var
except FileNotFoundError as e:
	print('Sorry. This file doesn not exist')
	print(e)
except Exception as e:
	print('Sorry. Something went wrong')
	print(e)
else:
	print(f.read())
	f.close()
finally:
	print("Executing Finally...")
try:
    f = open('curruptfile.txt')
     if f.name == 'currupt_file.txt':
         raise Exception
except IOError as e:
    print('Error!')
except Exception as e:
    print('Second')
else:
    print(f.read())
    f.close()
finally:
    print("Executing Finally...")

print('End of program')
