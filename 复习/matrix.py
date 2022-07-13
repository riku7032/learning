

# matrix = [
#     [1,2,3,4],
#     [5,6,7,8],
#     [9,10,11,12]
# ]

# a= [[row[i] for row in matrix] for i in range(4)]

# print(a)
# questions = ['name', 'quest', 'favorite color']
# answers = ['lancelot', 'the holy grail', 'blue']
# for q, a in zip(questions, answers):
#     print(f'What is your {q}?  It is {a}.')


import sys 

print('命令行参数如下：')
for i in sys.argv:
    print(i)
    
print(f'python路径位:{sys.path}')

print(f'{__name__}')

if __name__ == "__main__":
    print("程序入口")