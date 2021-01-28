dict_jenny = {"a":1,"b":2}
dict_jenny2 = dict(a=1,b=2)
a = {}
b = a.fromkeys([1, 2, 3],["a","b","c"])
print(b)
print({i: i*2 for i in range(1, 3)})
# print("dict", dict_jenny, type(dict_jenny))
# print("dict2", dict_jenny2, type(dict_jenny2))
# #dict key值不可变
# print(dict_jenny.keys())
# print(dict_jenny.values())
# print(dict_jenny.pop("a"))
# print(dict_jenny)
# print(dict_jenny2.popitem())
# print(dict_jenny2)


# tuple_jenny = (1, 2, 3)
# print("tuple:", tuple_jenny)
# print(tuple_jenny)
# # tuple 不可变
#
# print({i for i in "adskioweurowfds"})









# list_square = []
# list_square = [i**2 for i in range(1, 4)]
# print(list_square)
# list_square2 = []
# for i in range(1,4):
#     if i!=1:
#         list_square2.append(i**2)
# print(list_square2)
#
# list_square3 = [i**2 for i in range(1,4) if i != 1]
# print(list_square3)
#
# list_square4 = [i*j for i in range(1, 4) for j in range(1, 4)]
# print(list_square4)



# list_jenny = [1,4, 2, 3]
# list_jenny.sort()
# list_jenny.sort(reverse=True)
# list_jenny.reverse()
# print(list_jenny)
# # list_jenny.append(0)
# # list_jenny.insert(0,9)
# # print(list_jenny)
# # list_jenny.remove(2)
# # y = list_jenny.pop(0)
# # print(list_jenny)
# # print(y)