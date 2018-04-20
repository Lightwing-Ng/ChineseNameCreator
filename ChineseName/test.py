#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
 * @author: Lightwing Ng
 * email: rodney_ng@iCloud.com
 * created on Apr 21, 2018, 2:05 AM
 * Software: PyCharm
 * Project Name: Tutorial
"""

import chinesename  # 导入包

CnName = chinesename.ChineseName()  # 实例化
name = CnName.getName()  # 获取一个中文名
print("Name: \n", name)
names = CnName.getNames(100)  # 获取一个容量为100的中文名列表

print("Name: \n", names)
print(CnName.getNames.__doc__)
print(len(CnName._firstnames))
print(len(CnName._lastnames))
