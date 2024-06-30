immutable_var = 1, 'dog', False, [4, 8, 12]
print(immutable_var)
#immutable_var[1] = 'cat'   TypeError: 'tuple' object does not support item assignment
#print(immutable_var)       TypeError: объект 'tuple' не поддерживает назначение элементов
immutable_var[3][1] = 6
print(immutable_var)
#immutable_var.append('Hello')  AttributeError: 'tuple' object has no attribute 'append'
#print(immutable_var)           AttributeError: объект 'tuple' не имеет атрибута 'append'


mutable_list = [1, 'dog', False, [4, 8, 12]]
print(mutable_list)
mutable_list[1] = 'cat'
mutable_list.append('Hello')
print(mutable_list)