# -*- coding: utf-8 -*-
"""
Created on Sat Jan 14 09:20:52 2017

@author: Administrator
"""

brand = ['李宁','耐克','阿迪达斯','鱼C工作室']
slogan = ['一切皆有可能','Just do it','Impossible is nothing','让编程改变世界']
print ('鱼C工作室的口号是:',slogan[brand.index('鱼C工作室')])

dict1={'李宁':'一切皆有可能','耐克':'Just do it','阿迪达斯':'Impossible is nothing','鱼C工作室':'让编程改变世界'}
print ('鱼C工作室的口号是:',dict1['鱼C工作室'])

dict2 = {1:'one',2:'two',3:'three'}
print(dict2[2])