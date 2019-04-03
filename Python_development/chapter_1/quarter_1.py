#  实验github
#  查看Python中的保留字
#  ['False', 'None', 'True', 'and', 'as', 'assert',
# 'break', 'class', 'continue', 'def', 'del', 'elif', 
#  'else', 'except', 'finally', 'for', 'from', 'global', 
# 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 
#   'not', 'or', 'pass', 'raise', 'return', 'try', 
#  'while', 'with', 'yield']

from keyword import kwlist
print(kwlist)


#第一个Python程序
#相当于C语言的main()函数，是Python程序的入口
#hello world
if __name__ == "__main__":
	print("hello world")


# 通过元组可以输出多个变量的值，
# 元组中变量的顺序必须与字符串中对应的定制符一致，
# 定制符用于说明输出变量的类型
# bill is 30 years old
age = 30
name = "bill"
print('%s is %d years old' % (name,age))

# python程序的运行命令
# Python Python_file_path + python_file_py