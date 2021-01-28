














################################ 字面量插值




# formatted string literals
# 1 格式化输出 format  %的用法
# name = "Jenny"
# age = 18
# age2 = 12.33
# print("my name is  %s age is %d %.2f " % (name, age, age2))

#2 format () 方法
# str.format()
# name = "Jenny"
# age = 18
# hello = 'nihao'
# print('my name is {0}, age is {1}{0}{0}{2}'.format(name, age, hello))
# list1 = [1,2,3]
# dict1= {'name':'tom','gender':'male'}
# print('my list is {},dict is {}'.format(list1, dict1))
# namelist = ['jenny','tom','jerry']
# print("our name is: {},{},{}".format(*namelist)) #列表解包
# infodict = {'name':'tom','gender':'male'}
#
# print('my name is {name}, gener is {gender}'.format(**infodict)) #字典解包

#3 F-strings 字符串格式化机制
# f'{变量名}'
# 大括号内可以是表达式或者函数 但是不能转义 不能使用\

# name = 'jenny'
# age = 20
# list1  = [1, 3, 4]
# dict1 = {'name':'tom', 'gender':'male'}
# print(f'my name is {name.upper()},age is {age} {dict1["name"]},list is {list1[0]}')
# print(f"result is {(lambda x: x + 1)(2)}")
# print(f'my age is {"hello"}')






