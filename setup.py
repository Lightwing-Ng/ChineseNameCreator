#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
 * @author: Lightwing Ng
 * email: rodney_ng@iCloud.com
 * created on Apr 21, 2018, 2:05 AM
 * Software: PyCharm
 * Project Name: Tutorial
"""

from setuptools import setup, find_packages

setup(
    name='ChineseName',
    version='0.0.5',
    description='Fet a ChineseName randomly',
    license='MIT License',
    install_requires=[],
    packages=['ChineseName'],  # 要打包的项目文件夹
    include_package_data=True,  # 是否自动打包文件夹内所有数据
    author='Lightwing_Ng',
    author_email='rodney_ng@iCloud.com',
    url='https://github.com/Lightwing-Ng',
)
