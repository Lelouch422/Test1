#!/usr/bin/python
# -*- coding: utf-8 -*-

#第一个Python程序 - 输入和输出

#Python 基础 - 数据类型和变量

def one():
    name = input('please enter your name: ')  # read the input
    print('hello,', name)
    
    
def two():  # change line print
    print ('''    line1
    line2
    line3''')
    print ('        line1\n\tline2\n\tline3')
    print ('\\lala\\')
    print (r'\\lala\\')
    
    
def three():
    a = 'abc'    # create 'abc' and a, and put a point to 'abc'
    b = a    # create b and put b point to 'abc'
    a = 'xyz'    # put a point to 'xyz',but b doesnot change
    print (b)
    
    
def four():
    print ('10/3 = ',10/3)
    print ('int 10/3 =',10//3)
    print ('10%3 = ',10%3)
    
    
def five():
    n = 123
    f = 456.789
    s1 = 'Hello, world'
    s2 = 'Hello, \'Adam\''
    s3 = r'Hello, "Bart"'
    s4 = r'''Hello,
    Lisa!'''
    print (n)
    print (f)
    print (s1)
    print (s2)
    print (s3)
    print (s4)
    
    
if __name__ =='__main__':
    #one()
    #two()
    #three()
    four()