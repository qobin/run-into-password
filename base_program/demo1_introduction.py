#! /usr/bin/python
# -*- coding:UTF-8 -*-

class Person:
    """
    这是一个用户超类
    """
    __count = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.__count += 1

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getPersonNum(self):
        return Person.__count

if __name__ == "__main__":

    import re

    pattern = "\b*"
    str = "hjkdqweqwe"
    matObj = re.match(pattern, str, re.M)
    if matObj:
        matObj.group()