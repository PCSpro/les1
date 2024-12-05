immutable_var = ([1, 1.5], True, 5, 10.7)
print(immutable_var)
try:immutable_var[2] = 2
except:immutable_var[0][0] = 2
print(immutable_var)
# Сам кортеж менять нельзя, но можно изменить некоторые обьекты которые он в себе хранит
mutable_list = [1, 2, 3, 4, 5]
mutable_list[0] = 10
mutable_list[1] = 20
print(mutable_list)
