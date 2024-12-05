my_dict = {'Ola': 2023, 'Ivan': 2024, 'Oleg': 2019, 'Jon': 2020}
print(my_dict)
print(my_dict.get('Ola'))
print(my_dict.get('Olecya'))
my_dict.update({'Jon': 2018,
                'Bom': 2003})
a = my_dict.pop('Ivan')
print(a)
print(my_dict)

#3
print('---------------------------------------------------------')
#3

my_set = {10, 10, 2, 3, 4, 1.2, 1.5, True, True, 'HI'}
print(my_set)
my_set.update([111,100])
my_set.discard(1)
print(my_set)