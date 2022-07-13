# f = open("./foo.txt", "w+")

# f.write("hello")

# # 关闭打开的文件
# f.close()

# f = open("./print.py", "r",encoding="utf-8")

# strs = f.read()
# print(strs)

# # 关闭打开的文件
# f.close()

import codecs


with codecs.open("./foo.py","a+","utf-8") as f:
    f.write("this is method is prior")