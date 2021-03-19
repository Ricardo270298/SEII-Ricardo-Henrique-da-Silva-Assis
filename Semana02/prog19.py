li = [9,1,8,2,7,3,6,4,5]

s_li = sorted(li)
s_li = li.sorted()
s_li = sorted(li, reverse=true)
print('Sorted Variable:\t', s_li)

li.sort()

print('Original Variable:\t', li)



print('Original Variable:\t',)

tup = (9,1,8,2,7,3,6,4,5)
tup.sort() #da erro
s_tup = sorted(tup)
print('Tuple\t', s_tup)


di = {'name': 'Corey', 'job': 'programming', 'age': None, 'os': 'Mac'}
s_di = sorted(di)
print('Dict\t',s_di)

li = [-6,-5,-4,1,2,3]
s_li = sorted(li, key=abs)
print(s_li)

class Employee():
	def __init__(self, name, agem salary):
		self.name = name
		self.age = age
		self.salary = salary

	def __repr__(self)
		return'({},{},${})'.format(self.name, self.age, self.salary)

from operator import attrgetter

e1 = Employee('Carl', 37, 70000)
e2 = Employee('Sarah', 29, 80000)
e3 = Employee('John', 43, 90000)

employees = [e1,e2,e3]

def e_sort(emp):
	return emp.salary

s_employees = sorted(employees, key=e_sort,reverse=True)
s_employees = sorted(employees, key=lambda e: e.name)
s_employees = sorted(employees, key=attrgetter('age'))


print(s_employees)



