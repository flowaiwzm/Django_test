# from Crypto.Cipher import DES

# # 加密函数，text为待加密的明文，key为8字节的密钥
# def encrypt(text, key):
#     # 生成DES对象，使用ECB模式，采用PKCS5Padding填充方式
#     des = DES.new(key, DES.MODE_ECB)
#     # 将明文按PKCS5Padding方式进行填充
#     padded_text = pad(text.encode(), 8)
#     # 加密并返回密文
#     encrypted_text = des.encrypt(padded_text)
#     return encrypted_text.hex()

# # 解密函数，text为待解密的密文，key为8字节的密钥
# def decrypt(text, key):
#     # 生成DES对象，使用ECB模式，采用PKCS5Padding填充方式
#     des = DES.new(key, DES.MODE_ECB)
#     # 解密并返回明文，先将密文转换为bytes类型再进行解密
#     decrypted_text = des.decrypt(bytes.fromhex(text))
#     # 去除填充
#     unpadded_text = unpad(decrypted_text, 8).decode()
#     return unpadded_text

# # PKCS5Padding填充函数，text为待填充的明文，block_size为分块大小
# def pad(text, block_size):
#     n = block_size - len(text) % block_size
#     return text + bytes([n] * n)

# # PKCS5Padding去除填充函数，text为待去除填充的明文，block_size为分块大小
# def unpad(text, block_size):
#     n = text[-1]
#     return text[:-n]

# # 测试
# key = b'12345678'
# text = 'hello world!'
# encrypted_text = encrypt(text, key)
# print('encrypted:', encrypted_text)
# decrypted_text = decrypt(encrypted_text, key)
# print('decrypted:', decrypted_text)
#阶乘
# def fac(num):
#     """求阶乘"""
#     result = 1
#     for n in range(1, num + 1):
#         result *= n
#     return result


# m = int(input('m = '))
# n = int(input('n = '))
# # 当需要计算阶乘的时候不用再写循环求阶乘而是直接调用已经定义好的函数
# print(fac(m) // fac(n) // fac(m - n))
# import math
# print(math.factorial(3))
#函数参数,并不需要去考虑函数重载，一个函数可以支持默认参数也可以去考虑可变参数
# from random import randint
# def roll_dice(n=2):
#     total=0
#     for _ in range(n):#下划线代表占位符
#         total+=randint(1,6)
#     return total
# def change_param(*args):#*说明args为可变参数
#     total=0
#     for val in args:
#         total+=val
#     return total
# print(change_param())
#重名函数的处理方法--模块化处理
#import module1 as m1/m2  m1.fun()/m2.fun()
#python中特殊的变量名
#python查找变量的作用域的顺序为 局部(局部变量)-->嵌套-->全局（全局变量）-->内置（input，output,print）
#减少重复，减少使用全局变量，降低代码之间的耦合度
#闭包--延长局部变量的生命周期
#列表--结构化非标量，带索引可以循环，切片
# list1=[1,6,3,4,5]
# #循环列表元素
# for i in list1:
#     print(i,end="")
# print('\n')
# #循环列表索引
# for j in range(len(list1)):
#     print(j)
# # 通过enumerate函数处理列表之后再遍历可以同时获得元素索引和值
# for index,value in enumerate(list1):
#     print(index,value)
# import os
# import time
# import keyboard

# def main():
#     content = '北京欢迎你为你开天辟地…………'
#     while True:
#         # 清理屏幕上的输出
#         os.system('cls')  # os.system('clear')
#         print(content)
#         # 休眠200毫秒
#         time.sleep(0.1)
#         content = content[1:] + content[0]
#         if(keyboard.on_press(key='a')):
#             break

# if __name__ == '__main__':
#     main()
# import random


# def generate_code(code_len=4):
#     """
#     生成指定长度的验证码

#     :param code_len: 验证码的长度(默认4个字符)

#     :return: 由大小写英文字母和数字构成的随机验证码
#     """
#     all_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
#     last_pos = len(all_chars) - 1
#     code = ''
#     for _ in range(code_len):
#         index = random.randint(0, last_pos)
#         code += all_chars[index]
#     return code
# #设计一个函数返回给定文件名的后缀名
# def get_suffix(filename, has_dot=False):
#     """
#     获取文件名的后缀名

#     :param filename: 文件名
#     :param has_dot: 返回的后缀名是否需要带点
#     :return: 文件的后缀名
#     """
#     pos = filename.rfind('.')
#     if 0 < pos < len(filename) - 1:
#         index = pos if has_dot else pos + 1
#         return filename[index:]
#     else:
#         return ''
# if __name__=="__main__":
#     print(generate_code(code_len=4))
# import os


# def print_board(board):
#     print(board['TL'] + '|' + board['TM'] + '|' + board['TR'])
#     print('-+-+-')
#     print(board['ML'] + '|' + board['MM'] + '|' + board['MR'])
#     print('-+-+-')
#     print(board['BL'] + '|' + board['BM'] + '|' + board['BR'])


# def main():
#     init_board = {
#         'TL': ' ', 'TM': ' ', 'TR': ' ',
#         'ML': ' ', 'MM': ' ', 'MR': ' ',
#         'BL': ' ', 'BM': ' ', 'BR': ' '
#     }
#     begin = True
#     while begin:
#         curr_board = init_board.copy()
#         begin = False
#         turn = 'x'
#         counter = 0
#         os.system('cls')
#         print_board(curr_board)
#         while counter < 9:
#             move = input('轮到%s走棋, 请输入位置: ' % turn)
#             if curr_board[move] == ' ':
#                 counter += 1
#                 curr_board[move] = turn
#                 if turn == 'x':
#                     turn = 'o'
#                 else:
#                     turn = 'x'
#             os.system('cls')
#             print_board(curr_board)
#         choice = input('再玩一局?(yes|no)')
#         begin = choice == 'yes'


# if __name__ == '__main__':
#     main()
# class student(object):
#     #创建对象的时候初始化操作
#     def __init__(self,name,age,sex):
#         self.name=name
#         self.age=age
#         self.__sex=sex
#     #普通函数
#     def study(self,course):
#         print(f'{self.__sex}')
#         print(f'{self.name}选的是{course}')
# def main():
#     stu1=student('文主',21,'男')
#     # stu1._student__study('数学')
#     print(stu1.__sex)
# if __name__=='__main__':
#       main()
# from math import sqrt
# import turtle

# class Point(object):

#     def __init__(self, x=0, y=0):
#         """初始化方法
        
#         :param x: 横坐标
#         :param y: 纵坐标
#         """
#         self.x = x
#         self.y = y

#     def move_to(self, x, y):
#         """移动到指定位置
        
#         :param x: 新的横坐标
#         "param y: 新的纵坐标
#         """
#         self.x = x
#         self.y = y

#     def move_by(self, dx, dy):
#         """移动指定的增量
        
#         :param dx: 横坐标的增量
#         "param dy: 纵坐标的增量
#         """
#         self.x += dx
#         self.y += dy

#     def distance_to(self, other):
#         """计算与另一个点的距离
        
#         :param other: 另一个点
#         """
#         dx = self.x - other.x
#         dy = self.y - other.y
#         return sqrt(dx ** 2 + dy ** 2)

#     def __str__(self):
#         return '(%s, %s)' % (str(self.x), str(self.y))


# def main():
#     # print(turtle.position())
#     p1 = Point(3, 5)
#     p2 = Point()
#     print(p1)
#     print(p2)
#     p2.move_by(-1, 2)
#     print(p2)
#     print(p1.distance_to(p2))


# if __name__ == '__main__':
#     main()
# class Person(object):
#     """人"""

#     def __init__(self, name, age):
#         self._name = name
#         self._age = age

#     @property
#     def name(self):
#         return self._name

#     @property
#     def age(self):
#         return self._age

#     @age.setter
#     def age(self, age):
#         self._age = age

#     def play(self):
#         print('%s正在愉快的玩耍.' % self._name)

#     def watch_av(self):
#         if self._age >= 18:
#             print('%s正在观看爱情动作片.' % self._name)
#         else:
#             print('%s只能观看《熊出没》.' % self._name)


# class Student(Person):
#     """学生"""

#     def __init__(self, name, age, grade):
#         super().__init__(name, age)
#         self._grade = grade

#     @property
#     def grade(self):
#         return self._grade

#     @grade.setter
#     def grade(self, grade):
#         self._grade = grade

#     def study(self, course):
#         print('%s的%s正在学习%s.' % (self._grade, self._name, course))


# class Teacher(Person):
#     """老师"""

#     def __init__(self, name, age, title):
#         super().__init__(name, age)
#         self._title = title

#     @property
#     def title(self):
#         return self._title

#     @title.setter
#     def title(self, title):
#         self._title = title

#     def teach(self, course):
#         print('%s%s正在讲%s.' % (self._name, self._title, course))


# def main():
#     stu = Student('王大锤', 15, '初三')
#     stu.study('数学')
#     stu.watch_av()
#     t = Teacher('骆昊', 38, '砖家')
#     t.teach('Python程序设计')
#     t.watch_av()


# if __name__ == '__main__':
#     main()
from abc import ABCMeta, abstractmethod


class Pet(object, metaclass=ABCMeta):
    """宠物"""

    def __init__(self, nickname):
        self._nickname = nickname

    @abstractmethod
    def make_voice(self):
        """发出声音"""
        pass


class Dog(Pet):
    """狗"""

    def make_voice(self):
        print('%s: 汪汪汪...' % self._nickname)


class Cat(Pet):
    """猫"""

    def make_voice(self):
        print('%s: 喵...喵...' % self._nickname)


def main():
    pets = [Dog('旺财'), Cat('凯蒂'), Dog('大黄')]
    for pet in pets:
        pet.make_voice()


if __name__ == '__main__':
    main()