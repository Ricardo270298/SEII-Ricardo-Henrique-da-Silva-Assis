
#if true:
#	print('conditional was true')
#if false:
#	print('conditional was true')

language = 'Python'
if language == 'Python':
	print('conditional was true')

# Comparisons:
# Equal:            ==
# Not Equal:        !=
# Greater Than:     >
# Less Than:        <
# Greater or Equal: >=
# Less or Equal:    <=
# Object Identity:  is

if language == 'Python':
	print('Language is Python')
else:
	print('No math')

language = 'Java'
if language == 'Python':
	print('Language is Python')
elif language == 'Java':
	print('Language is Java')
else:
	print('No math')

# and
# or
# not

user = 'Admin'
logged_in = False

if user == 'Admin' and logged_in:
	print ('Admin Page')
else:
	print ('Bad Creds')

if user == 'Admin' or logged_in:
	print ('Admin Page')
else:
	print ('Bad Creds')

if not logged_in:
	print ('Please Log In')
else:
	print ('welcome')

a = [1,2,3]
b = [1,2,3]

print (a == b)
print (id(a))
print (id(b))
print (a is b)
print (id(a) == id(b))

# False Values:
    # False
    # None
    # Zero of any numeric type
    # Any empty sequence. For example, '', (), [].
    # Any empty mapping. For example, {}.

condition1 = False

if condition1:
	print('Evaluated to True')
else:
	print('Evaluated to False')

condition2 = None

if condition2:
	print('Evaluated to True')
else:
	print('Evaluated to False')

condition3 = 0

if condition3:
	print('Evaluated to True')
else:
	print('Evaluated to False')

condition4 = []

if condition4:
	print('Evaluated to True')
else:
	print('Evaluated to False')

condition5 = {}

if condition5:
	print('Evaluated to True')
else:
	print('Evaluated to False')

