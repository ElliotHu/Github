# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 15:08:59 2017

@author: Administrator
"""

def MyFirstFunction(name):
    '函数定义过程中的name是叫形参'
    #因为Ta只是一个形式
    print('传递进来的' + name + '叫做实参，因为Ta是具体的参数值！')
    
MyFirstFunction('小甲鱼')

def SaySome (name,words):
    print(name + '->' + words)
    
SaySome('小甲鱼','让程序改变世界')