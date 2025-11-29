#3.1类与对象 “学生“类
from tkinter.font import names


class Student:
    def __init__(self,name,age,grades):
        self.name=name
        self.age=age
        self.grades=grades

    def calculate_average(self):
        if len(self.grades)==0:
            return 0
        return sum(self.grades)/len(self.grades)


    def display_info(self):
        avg_grade=self.calculate_average()
        print(f"学生姓名：{self.name}")
        print(f"平均成绩：{avg_grade}")

student1=Student("喵1",99,[11,22,33,44])
student2=Student("喵2",28,[44,55,66,77])
student3=Student("喵3",38,[66,77,88,99])

print("学生姓名及平均成绩：")
student1.display_info()
student2.display_info()
student3.display_info()

#3.2封装 3.3继承 多继承 复写 3.4多态 ”动物“类
class Animal:
    def __init__(self,name):
        self.name=name

    def make_sound(self):
        print(f"{self.name}在叫")

class Cat(Animal):
    def __init__(self,name):
        super().__init__(name)

    def make_sound(self):
        print(f"{self.name}在ha ha ha！")

class Dog(Animal):
    def __init__(self,name):
        super().__init__(name)

    def make_sound(self):
        print(f"{self.name}在汪汪叫！")

cat=Cat("猫傲天")
dog=Dog("小黑")

print("猫：")
cat.make_sound()

print("狗：")
dog.make_sound()

#多态演示
animals=[cat,dog]
for animal in animals:
    animal.make_sound()

#附加题
#tuple = ( 'runoob', 786 , 2.23, 'john', 70.2 )
#ele = tuple[-1]
# ele 是什么？
#python支持负索引，倒数第几开始   70.2