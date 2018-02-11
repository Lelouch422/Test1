#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Python 基础 - 使用List和Tuple
#Python 基础 - 条件判断
#Python 基础 - 循环

def one():
    list = [1,2,3,4,5]
    print (list.insert(2,2.5),list)
    print (list.pop())
    print (list.pop(2))
    
    
def two():  
    print ('tuple: 初始化就不能修改')
    t = (1,2)
    t1 = ()
    t2 = (1,)
    print ('tuple: %s, 空tuple: %s, 一个元素tuple：%s' %(t,t1,t2))
    
    
def three():
    t = ('a', 'b', ['A', 'B'])
    t[2][1] = 'X'
    print (t)
    print ('tuple所谓的“不变”是说，tuple的每个元素，指向永远不变。')
    
    
def four():
    s = input('birth year: ')
    birth = int(s)
    if birth < 2000:
        print('00前')
    else:
        print('00后')
        
        
def five():
    print ('endless loop')
    #n=1
    #while n>0:
    #    x = n
    print ('Ctrl C to quite')    
        
        
if __name__ =='__main__':
    #one()
    #two()
    #three()
    #four()
    five()