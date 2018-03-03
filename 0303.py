#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Python 基础 - 使用dict和set

#函数 - 调用函数
#函数 - 定义函数

import math


def one():
    dict = {'a':1,'b':2}
    dict['d'] = 3
    print (dict.get('a'))
    print (dict.get('c'))
    print (dict.get('c',-1))
    print ('pop a :',dict.pop('a'))
    print (dict)
    
    
def two():
    print ('set:集合，和dict区别：没有存储对应的value. 要创建一个set，需要提供一个list作为输入集合')
    print ('set 和 dict 都没有重复的key，因此不能放入可变对象比如list')
    s = set([1,2,2,3])
    s.add(3) #set为add，dict没有add
    s.add(4)
    s.remove(2) #set为remove，不是pop
    ss = set([3,4,5])
    print (s & ss)
    print (s | ss)
    
    
def three():
    print ('字符串是不可变对象')
    a = 'abc'
    print (a.replace('a','A'))
    print (a) 
    b = a.replace('a','A')
    print (b)
    print ('对于不变对象来说，调用对象自身的任意方法都不会改变该对象自身的内容。相反，这些方法会创建新的对象并返回，这样，就保证了不可变对象本身永远是不可变的。')
    
    
def four():
    print ('函数名其实就是指向一个函数对象的引用，完全可以把函数名赋给一个变量，相当于给这个函数起了一个“别名”')
    a = abs
    print (a(-1))
    
    
def five():
    print ('函数执行完毕也没有return语句时，自动return None')
    print ('函数可以同时返回多个值，但其实就是一个tuple。')
    
    
def quadratic(a, b, c):
    # solution of ax2 + bx + c = 0
    if isinstance(a, (int, float)) and isinstance(b, (int, float)) and isinstance(c, (int, float)):
        pass
    else:
        print ('Input is wrong')
        return
    delta = b*b-4*a*c
    if (delta<0):
        print ('The funtion has no solution')
        return
    else:
        x1 = (-b+math.sqrt(delta))/2/a
        x2 = (-b-math.sqrt(delta))/2/a
        return (x1, x2)


if __name__ =='__main__':
    #one()
    #two()
    #three()
    #four()
    #five()
    quadratic(2, 3, 1)

