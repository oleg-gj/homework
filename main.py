# task_1
int_a = 55
str_b = 'cursor'
set_c = {1, 2, 3}
lst_d = [1, 2, 3]
dict_e = {'a': 1, 'b': 2, 'c': 3}

print(id(int_a))
print(id(str_b))
print(id(set_c))
print(id(lst_d))
print(id(dict_e))

#task_2
lst_d = [1, 2, 3, 4, 5]
print(id(lst_d))

#task_3
print(type(int_a))
print(type(str_b))
print(type(set_c))
print(type(lst_d))
print(type(dict_e))

#task_4
print(isinstance(int_a, int))
print(isinstance(str_b, str))
print(isinstance(set_c, set))
print(isinstance(lst_d, list))
print(isinstance(dict_e, dict))

#task_5
print("Anna has {} apples and {} peaches.".format(4, 5))

#task_6
print("Anna has {1} apples and {0} peaches.".format(4, 5))

#task_7
print("Anna has {quantity_apples} apples and {quantity_peaches} peaches.".format(quantity_apples=4, quantity_peaches=5))

#task_8

print("Anna has {:.5s} apples and {:.3s} peaches.".format('123456', '1234567'))


#task_9
quantity_apples = 4
quantity_peaches = 5
print(f"Anna has {quantity_apples} apples and {quantity_peaches} peaches.")

#task_10
print("Anna has %s apples and %s peaches."%(2,4))

#task_11
dict = {'first' : 1, 'second' : 2}
print("Anna has {first} apples and {second} peaches.".format(**dict))

#task_12
list_comprehension = [num ** 2 if num % 2 == 1 else num ** 4 for num in range(10) ]
print(list_comprehension)

#task_13
lst = []
for num in range(10):
    if num % 2 == 0:
        lst.append(num // 2)
    else:
        lst.append(num * 10)
print(lst)

#task_14
dict_comprehension = {x: x**2 for x in range(1,11) if x % 2 == 1}
print(dict_comprehension)

#task_15

dict_comprehension = {x: x**2 if x % 2 == 1 else x // 0.5 for x in range(1,11)}
print(dict_comprehension)

#task_16
d = {}
for num in range(10):
    if num ** 3 % 4 == 0:
        d[num] = num ** 3
print(d)

#task_17
d = {}
for num in range(10):
    if num ** 3 % 4 == 0:
        d[num] = num ** 3
    else:
        d[num] = num
print(d)

#task_18
foo = lambda x,y: x if x < y else y

#task_19
def foo(x,y,z):
    if y < x and x > z:
        return z
    else:
        return y

#task_20
lst_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]
sorted(lst_to_sort)

#task_21
sorted(lst_to_sort, reverse=True)

#task_22
a = list(map(lambda x: x * 2, lst_to_sort))
print(a)

#task_23
list_A = [2, 3, 4]
list_B = [5, 6, 7]
list_sum = list(map(sum, zip(list_A,list_B)))

#task_24
lst = [x for x in lst_to_sort if x % 2 == 1]

#task_25
lst_1 = [x for x in range(-10,10) if x < 0]

# task_26
list_1 = [1,2,3,5,7,9]
list_2 = [2,3,5,6,7,8]

lst = [x for x in list_1 if x in list_2]