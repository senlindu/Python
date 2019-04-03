# python的编码规则
#
# Python语言有自己独特的编码规则，包括命名规则、代码书写规则等。
#
#
# 命名规则
#
# 变量名的首字符必须是字母或下划线，首字符之外的字符可以由字母、数字或下划线组成，并且不能使用Python的保留字。
#
# 变量名通常由字母和下划线组成，包名、模块名通常用小写字母
# Filename:quarter_2.py
# _rule = "rule information"
#
# 第一行用于声明模块的名称，模块名用小写字母。也可以不指定，以py结尾的文件就是一个模块。模块名就是文件名。
# 第二行代码定义了一个全局变量_rule.
#
#
# 类名、对象名
#
# 类名首字母用大写，其他字母采用小写。对象名用小写字母。
# 类的属性和方法名以对象作为前缀，对象通过操作符"."访问属性和方法。
# 类的私有变量、私有方法以两个下划线作为前缀。


class Student:
    # 私有实例变量前必须有两个下划线
    __name = ""

    def __init__(self, name):
        # self相当于Java中的this
        self.__name = name
    # 方法名首字母用小写，其后每个单词用大写

    def getName(self):
        return self.__name


if __name__ == "__main__":
    student = Student("borphi")
    print(student.getName())

# 函数名
# 函数名通常采用小写，并用下划线或单词首字母大写来增加名称的可读性
# 导入的函数以模块名作为前缀
#
# randrange()声明如下
# randrange(start,stop[,step])
# 参数start表示生成随机数所在范围的开始数字
# 参数stop表示生成随机数所在范围的结束数字，但不包括数字stop
# 参数step表示从start开始往后的步数。生成的随机数在[start,stop-1]的范围内，取值等于start+step
#
#
import random


def compareNum(num1, num2):
    if(num1 > num2):
        return 1
    elif(num1 == num2):
        return 0
    else:
        return -1


num1 = random.randrange(1, 9)
num2 = random.randrange(1, 9)
print("num1 =", num1)
print("num2 =", num2)
print(compareNum(num1, num2))

# 符合命题规则的写法
# sumpay表示年终奖金
# monthPay表示月薪
# sumPay表示全年的薪水
sumPay = 0
bonusOfYear = 2000
monthPay = 1200

sumPay = bonusOfYear + 12 * monthPay
print(sumPay)

# 代码缩进与冒号
# Python中代码缩进是一种语法，用冒号和代码缩进来区分代码之间的层次

x = 1
if x == 1:
    print("x = ", x)
else:
    print("x = ", x)
    x = x + 1
print("x = ", x)


# 模块导入的规范
# 模块是类或函数的集合，用于实现某个功能。
# 在Python中，如果需要在程序中调用标准库或其他第三方库的类时，
# 需要先使用import或from..import..语句导入相关的模块
# 命名空间是指标识符的上下文
# import语句
# 在当前程序的命名空间中创建导入模块的引用，从而可以使用
# "类名.属性"的方式调用
import sys
print(sys.path)
print(sys.argv)

# from..import..语句只导入模块中的一部分内容，并在当前的命名空间中
# 创建导入对象的引用
# 不规范导入方式
from sys import path
from sys import argv
print(path)
print(argv)


# 使用空行分隔代码
# 函数之间或类的方法之间用空行分隔，表示一段新的代码的开始
# 类和函数入口之间也用一行空行分隔，以突出函数入口的开始


class A:

    def funX(self):
        print("funY()")

    def funY(self):
        print("funY()")


if __name__ == "__main__":
    a = A()
    a.funX()
    a.funY()


# 正确的注释
# 如果只对一行进行注释，使用"//#"加若干空格开始
# 如果对一段代码进行注释，段落之间以一个"\\#"行分隔。
# 中文注释，如果需要在代码中使用中文注释，必须在Python文件的最前面加上如下注释说明
# -*- coding: utf-8 -*-
#
# 跨平台注释
#！ /usr/bin/python
#
# 语句的分隔
# Python中分号已经没那么重要了，可以通过换行识别语句的结束
# 如果一行中写多条语句，必须使用分号分隔
# x=1;y=2;z=3
# 
# python同样支持多行写一条语句，使用"\"作为换行符。
# 字符串的换行
# 写法一
sql = "select id.name \
from dept \
where name = 'A'"
print(sql)

# 写法二
sql = "select id.name " \
    "from dept " \
    "where name = 'A'"
print(sql)
