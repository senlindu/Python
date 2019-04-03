# python的文件类型
# 主要有三种，分别为源代码、字节代码和优化代码。

# 源代码
# 源代码的文件以"py"为扩展名，由Python.exe解释，可以在控制台下运行。
# 用Python语言写的程序不需要编译成二进制代码，可以直接运行源代码。
# "pyw"是程序开发图形用户接口的源文件的扩展名，由pythonw.exe运行


# 字节代码
# Python源文件经过编译后生成扩展名为"pyc"的文件。
# "pyc"是编译过的字节文件，与平台无关的。
# 也可以通过脚本生成该类型的文件
# import py_compile
# py_compile.compile('hello.py')


# 优化代码
# 经过优化的源文件生成扩展名为"pyo"的文件，需要命令行工具生成。
# 1、启动命令窗口，进入hello.py文件所在的目录
# cd /D filepath
# 2、在命令行中输入"Python -O -m py_compile hello.py"，然后回车
# python -O -m py_compile hello.py
# 参数"-O" 表示生成优化代码
# 参数"-m"表示把导入的py_compile模块作为脚本运行。
# 编译hello.py需要调用py_compile模块的compile()方法