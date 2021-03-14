#Dictionaries

student = {'name': 'John', 'age': 25, 'courses':['Math', 'CompSci']}

student['phone'] = '555-5555'
student['name'] = 'Jane'
student.update ({'name': 'Liz', 'age': 26, 'phone': '555-5556'})
print (student.get('name'))
#print (student.get('phone', 'Not Found'))

del student['age']

print (student)

#age = student.pop('age')
#print (age)

#print (len(student))
print (student.keys()) 
print (student.values())
print (student.items())

for key, value in student.items():
	print(key,value)
