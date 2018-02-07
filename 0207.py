#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Python 基础 - 字符串和编码

def one():
    print ('ascii: 编码1个字节， unicode：编码2个字节， utf-8：编码1-6个字节，其中英文1字节，中午3字节')
    print ('在计算机内存中，统一使用Unicode编码，当需要保存到硬盘或者需要传输的时候，就转换为UTF-8编码')
    
    
def two():  
    print (ord('A'))
    print (ord('中')) # only allow one character
    print (chr(66))
    print(chr(25991))
    print ('\u4e2d\u6587')
    
    
def three():
    print ('abc'.encode('ascii'))
    print ('中文'.encode('utf-8'))
    #print ('中文'.encode('unicode'))
    print (b'abc'.decode('ascii'))
    print (b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))
    print (b'\xe4\xb8\xad\xff'.decode('utf-8', errors='ignore'))
    
    
def four():
    print (len('abc'))
    print (len(b'abc'))
    print (len('中文'))
    #print (len(b'中文'))
    print (len(b'\xe4\xb8\xad\xe6\x96\x87'))
    print (len('中文'.encode('utf-8')))
    
    
def five():
    print('%.2f' % 3.1415926)
    print ('Hello, {0},  {1:.1f}%'.format('小天才', 88.88))
    
    
if __name__ =='__main__':
    #one()
    #two()
    #three()
    #four()
    five()