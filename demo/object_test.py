class Person:
    name = "default"
    age = 0
    gender = "male"
    weight = 0

    def __init__(self,name):
        print("**********init*******")
        self.name = name

    def eat(self):
        print('eating')
        print('*****')


    def play(self):
        print("playing")

    def jump(self):
        print("jump")

person = Person("zhangsan")

print(f"the name is {person.name}, age is {person.age}")

# 类方法 Person.eat()
# 类方法不能直接访问方法 需要装饰器才可以 @classmate