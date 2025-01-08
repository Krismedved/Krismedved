immutable_var = (4, 2.0, 'one', [1,2,3,4], True)
print(immutable_var )

#immutable_var[0] = 1
#TypeError: 'tuple' object does not support item assignment
#кортеж - не изменяемая коллекция априори

mutable_list = [4, 2.0, 'one', [1,2,3,4], False]
mutable_list[0] = 'one'
mutable_list[1] = 3
print(mutable_list[0])
print(mutable_list[1])
print(mutable_list)