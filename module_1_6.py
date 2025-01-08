my_dict = {'Sofia': 1990, 'Mishel': 1985, 'Nick': 1980, 'Gary': 1994}
print(my_dict)
print(my_dict['Nick'])
print(my_dict.get('Holy', 'нет такого ключа'))
my_dict.update({'Smith': 1982, 'Ruth': 2001})
print(my_dict)
my_dict.pop('Mishel')
print(my_dict)

my_set = {3, 3, 3, 1, 2, 3, True, False, True, 'list', 'set', 'list'}
print(my_set)
my_set.add('keys')
my_set.add('room')
my_set.discard(2)
print(my_set)


