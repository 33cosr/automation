num = 2
if num > 1:
    print("num >1")


def div(a,b):
    return a / b
#
try:
    print(div(1, 1))
    list1 = [1,2,3]
    print(list1[2])
except Exception as e:
    print(e)
    print('there is an exception')
else:
    print('there is no exception')
finally:
    print("over ")
# except IndexError as e:
#     print(e)
# except ZeroDivisionError as e:
#     print("there is an exception", e)

def set_age(num):
    if num <= 0 or num > 200:
        raise ValueError(f"age is not corrct,age is {num}")
    else:
        print("this is reasonable")
set_age(203)