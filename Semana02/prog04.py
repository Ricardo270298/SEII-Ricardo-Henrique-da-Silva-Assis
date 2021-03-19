
#Listas
courses = ['History', 'Math', 'Physics', 'CompSci']

print (len(courses)) #Para ver a quantidade de itens na lista
print (courses[0]) # Para mostrar um item especifico da lista
print (courses[-1]) # Mostra um item especifico da lista, mas começa a contar o indice de tras para frente
print (courses[0:2]) # Para mostrar do primeiro indice até o segundo
print (courses[2:]) # Do indice de valor 2 até o fim da lista

courses.append('Art') # adiciona Art no fim da lista
courses.insert(0,'Art') # Adiciona Art na lista  no indice indicado
print (courses)

courses2 = ['Art', 'Education']
courses3 = courses 
courses.insert(0,courses2)
print (courses)
courses3.extend(courses2) #Para extender uma lista adicionando outra nela
print (courses3)

courses.remove('Math') # Para remover um item da lista
courses.pop() # Remove o ultimo item da lista
print (popped) # Printa o item q foi removido
courses.reverse # Inverte a lista
courses.sort 

nums = [1,5,2,4,3]
nums.sort # coloca a lista em ordem crescente ou alfabetica
course.sort(reverse = true) 

sorted_courses = sorted(courses)
print (sorted_courses)

print(min(nums))
print(max(nums))
print(sum(nums))

print (courses.index('CompSci')
#print ('Art' in courses) #Para descobrir se determinado item está na lista

#loop
for item in courses: 
	print(item)
for index,course in enumerate(courses,start = 1):
 # Retorna o indice e o valor, começando pelo indice de vaalor 1
	print (index,course) 

course_str = ', '.join(courses)
print (course_str)

new_list = course_str('-')
print (new_list)


# Mutable
list_1 = ['History', 'Math', 'Physics', 'CompSci']
list_2 = list_1

print(list_1)
print(list_2)

 list_1[0] = 'Art'

 print(list_1)
 print(list_2)


# Immutable
 tuple_1 = ('History', 'Math', 'Physics', 'CompSci')
 tuple_2 = tuple_1

 print(tuple_1)
 print(tuple_2)

 tuple_1[0] = 'Art'

 print(tuple_1)
 print(tuple_2)


# Sets
cs_courses = {'History', 'Math', 'Physics', 'CompSci'}  # A ordem muda a cada execução, sets não se importam com ordem. É usado para remover valores duplicados
art-courses = {'History', 'Math', 'art', 'Design'}
print(cs_courses)
print  ('Math' in cs_courses)

print (cs_courses.difference(art_courses))
print (cs_courses.union(art_courses))

# Empty Lists
empty_list = []
empty_list = list()

# Empty Tuples
empty_tuple = ()
empty_tuple = tuple()

# Empty Sets
empty_set = {} # This isn't right! It's a dict
empty_set = set()
