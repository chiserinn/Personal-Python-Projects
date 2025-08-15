#Indexing Cheatsheet

#STRINGS
intro = "My name is Jeff!"

print(intro[0]) 
print(intro[0:2])
print(intro[-5:-1])

print(len(intro)) 

print(intro.lower())
print(intro.upper())
print(intro.title())

print(intro.split())
print(intro.split('name')) 
print(intro.split('!'))

#LISTS
lst = ['abc', 123, 'def', 10.5, 62, ['g', 'h', 'i']]
print(lst)

print(lst[0]) 
print(lst[4:6])

print(len(lst))

lst.append(99) 
print(lst)

lst.remove(62) 
print(lst)

lst.pop()
print(lst)

lst.pop(0) 
print(lst)

#TUPLES
#more memory & time efficient compared to lists

my_tuple = ('abc', 123, 'def', 456, 789, 'ghi')

print(my_tuple[0])
print(my_tuple[3:5])

print(len(my_tuple)) 

print(my_tuple.index('abc'))
print(my_tuple.index(789)) 

##DICT
#immutable
groceries = {
'fruits': ['mangoes', 'bananas', 'kiwis'],
'protein': ['beef', 'pork', 'salmon'], 
'carbs': ['rice', 'pasta', 'bread'],
'veggies': ['lettuce', 'cabbage', 'onions']
}

print(groceries['veggies'])

second_list = {'desserts': ['mochi', 'ice cream', 'gulab jamun']}
groceries.update(second_list)
print(groceries)

print(groceries.keys())
print(groceries.values())

##SET
#immutable
students1 = {'Jane', 'Carlos', 'Amy', 'Bridgette', 'Chau', 'Dmitry'}

print(students1)

students1.add('George')
print('George' in students1) 

students2 = {'Alice', 'Lily', 'Zhuo', 'Amy', 'Jane'}

students3 = students1.union(students2)
print(students3)

students1.remove('Bridgette')
print(students1)

for student in students1:
  print(student)

  