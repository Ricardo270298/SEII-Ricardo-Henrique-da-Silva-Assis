message1 = 'Hello world'
message2 = 'Bobby\'s world'
message3 = """Bobby's world
 was a good cartoon in the 1900s"""
print (message1)
print (len(message1))
print (message1[0])
print (message1[0:5])
print (message1[6:])
print (message1.lower())
print (message1.upper())
print (message1.count('Hello'))
print (message1.find('World'))
new_message = message1.replace('world', 'Universe')
print (new_message)
message1 =  message1.replace('world', 'Universe')

greeting = 'Hello'
name = 'Michael'
message4 = greeting + ', ' + name + '. Welcome!'
print (message4)
message5 = '{}, {}. Welcome!'.format(greeting, name)
print (message5)
message6 = f'{greeting}, {name.upper}. Welcome!'

print (dir(name))

print (help(str));
print (help(str.lower));




