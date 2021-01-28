"""  Python中的函数第二部分  """
"""
    函数的类型: 1）无参无返回值：一般用于提示信息打印
              2）无参有返回值：一般用于数据采集，比如获取系统信息
              3）有参无返回值：多用于设置一些不需要返回值的参数设置
              4）有参有返回值：一般是计算型，需要参数，最终也要返回结果
"""

# 局部变量 与 全局变量
"""
    局部变量：1、就是在函数内部定义的变量【作用域局限在函数体内】 同C语言的局部变量
            2、一般是为了临时的保存数据 需要在函数中定义
"""
pro = '计算机信息管理'  # pro 为全局变量

def printInfo():
    name = 'peter'  # name 为局部变量
    # pro = '局部定义的pro'  # 作用域会产生覆盖，生效效果与C语言一致
    print(pro)
    pass

def changeGlobal():
    """
    通过函数修改全局变量
    :return:
    """
    # pro = '市场营销'  # 相当于定义了一个局部变量pro，无法修改全局变量
    global pro
    pro = '市场营销'  # 通过声明global 即可修改全局变量
    pass

changeGlobal()
printInfo()

# Python中的引用
"""
    在python中，万物皆对象，不管是数字、列表，或是字典、函数，都可以视为对象。
    
    变量可以视为是对象的引用
    
"""
# 可变类型
a = 1
b = a
c = 1
print(id(a))
print(id(b))  # 可以发现b与a的地址是相同的
print(id(c))  # 可以发现c与a的地址也是相同的
a = 2
print(id(a))  # 此时a的地址发生改变，但b、c的地址没有改变
# 通过上述代码结果验证可知，变量为对象的一个引用。通过赋值操作将变量和对象绑定起来
def func(x):
    print(id(x))
    x = 20
    print(id(x))  # x的值改变之后，他的id地址发生改变
    pass

func(a)  # 发现x与a的id地址是一样的
print(a)  # a的值没有发生改变
print(id(20))  # 发现20的id地址与函数中改变x为20之后的地址相同

# 可变类型
li = []
def testRenc(parms):
    print(id(parms))
    parms.append(3)
    pass

print(id(li))
testRenc(li)  # 发现两次输出的结果是一样的。
li.append(2)
print(id(li))  # 发现修改之后，地址并未发生变化
print(li)  # 根据结果可知，函数操作的结果会直接造成变量值的改变


"""
    小结：Python中变量与对象（或者数据）是分开的两个部分，通过赋值绑定在一起，实参传递传递的就是对象的引用。
    个人理解：1、对于不可变类型，类似于每次绑定会扫描已存在的数据值，若该值已存在，则将变量直接绑定在对应地址。若不存在，才会申请新的空间，进行绑定。
            这样的变量成为不可变类型：int、str、元组。
            2、对于可变类型，值的改变相当于直接对对象进行修改，所以函数内部的修改直接会导致对象的变化，地址不会改变。
"""
