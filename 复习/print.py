# import sys

# print('命令行参数为：')

# for i in sys.argv:
#     print(i)
# print('\n python 路径为：',sys.path)

# from sys import argv,path

# print("path:",argv)

a = "hello"


code = a.encode("utf-8")

string = code.decode("utf-8")

print(string)