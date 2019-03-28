#coding=utf-8

#方法一：使用模块

'''
Python的模块就是天然的单例模式，因为模块在第一次导入时，会生成 .pyc 文件，当第二次导入时，就会直接加载 .pyc 文件，而不会再次执行模块代码
'''
class MySingleton(object):
    def __init__(self, val):
        self.val = val

single = MySingleton(1)

'''
#test_module.py
from mysingleton import single
a = single
b = single
print(a.val) #1
print(b.val) #1
a.val = 233
print(a.val) #233
print(b.val) #233
'''

#方法二：使用 __new__
'''将类的实例和一个类变量 _instance 关联起来，如果 cls._instance 为 None 则创建实例，否则直接返回 cls._instance'''
class Singleton(object):
    _instance = None
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance

class MyTest(Singleton):
    a = 1

'''
from mysingleton import *
one = MyTest()
two = MyTest()
print(one==two) #True
print(id(one))  #42308272
print(id(two))  #42308272
'''

#使用装饰器
'''装饰器（decorator）可以动态地修改一个类或函数的功能。这里，我们也可以使用装饰器来装饰某个类，使其只能生成一个实例'''
from functools import wraps
'''
Python装饰器（decorator）在实现的时候，被装饰后的函数其实已经是另外一个函数了（函数名等函数属性会发生改变），为了不影响，
Python的functools包中提供了一个叫wraps的decorator来消除这样的副作用。写一个decorator的时候，最好在实现之前加上functools的wrap，
它能保留原有函数的名称和docstring
'''

def singleton(cls):
    instance = {}
    @wraps(cls)
    def getinstance(*args, **kwargs):
        if cls not in instance:
            instance[cls] = cls(*args, **kwargs)
        return instance[cls]
    return getinstance

@singleton
class MyClass(object):
    a = 1

'''
我们定义了一个装饰器 singleton，它返回了一个内部函数 getinstance，该函数会判断某个类是否在字典 instances 中，
如果不存在，则会将 cls 作为 key，cls(*args, **kw) 作为 value 存到 instances 中，否则，直接返回 instances[cls]
'''
