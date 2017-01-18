# -*- coding: utf-8 -*-
"""
Created on Thu Jan 12 14:46:24 2017

@author: Administrator
"""

def Feb(n):
    if n < 1:
        print('输入有误！')
        return -1
        
    if n== 2 or n == 1:
        return 1
    else :
        return Feb(n-1)+ Feb(n-2)

result = Feb(35)
if result != -1:
    print('总共有%d对小兔崽子'% result)