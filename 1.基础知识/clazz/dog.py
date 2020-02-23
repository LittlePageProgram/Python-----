class Dog():
    """模拟小狗"""

    def __init__(self, name, age):
        """初始化属性"""
        self.name = name
        self.age = age

    def sit(self):
        print(self.name + " sit")

my_dog = Dog('wang', 12)

my_dog.sit()

print(my_dog.age)

my_dog.ppp = 1
print(my_dog.ppp)