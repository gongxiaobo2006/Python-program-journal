

#codes for testing class syntax
#author:Peihan
#date: 2018年4月3日


class Employee(object): 
	def __init__(self,name,salary): #千万注意这里是init 不是 int，错特么几次了
		self.name = name
		self.salary = salary

	def print_salary(self):
		print("%s: %s" % (self.name, self.salary))

	#用 __双下划线定义的函数，在class外部是不能访问的

	pass

bart = Employee('ding ding',10000)
#bart.print_salary()



class Animal(object):
	def __init__(self,name,height):
		self.name = name 
		self.height = height
	def run(self):
		print("running...")

class Dog(Animal):
	def bite(self):
		print("bite someone...")
	pass

class Human(Animal):
	def talk(self):
		print("talk to someone...")

class Tangwei(Human):
	def speak(self):
		print("talk to Peihan...")
		pass
#这里 先 定义了 Animal类，其中包含Dog和Human两类。
#其中Human类里又有Tangwei类
#所以我将dingding赋值给Tangwei这一类的话
#dingding就可以调用上面Animal和Human这两类的函数。

dingding = Tangwei('ding ding',157)
#dingding.speak()


a = Animal('Oliver',173)
b = Dog('Oliver',173)
c = Tangwei('Oliver',173)
# isinstance可以帮助判断 c 是不是 Dog或者其他什么的类型
#print(isinstance(c,Dog)) 

# isinstance 也可以判断 变量是否为 tuple，list等
#语法如下
#print(isinstance({1,2,3},list))
#print(isinstance({1,2,3}, (list, set)))


#print(dir('abc')) #dir可以获取 ‘abc’的所有属性

'''
class Student(object):
	__slots__ = ('name','age')

s = Student()
#使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的
#除非在子类中也定义__slots__，这样，子类实例允许定义的属性就是自身的__slots__加上父类的__slots__。
#在 IDE中运行的时候，如果对对象 s 绑定的 比如 s.socre并不是 object 的attribute
#其中slot中只有 name和age，所以这样赋值会报错
#不能用 s.score = 99
'''

#如果我们想要不是很容易的修改score的数据，此时可以用 @property
#例如 如下代码

class Student(object):
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 - 100!')
        self._score = value







