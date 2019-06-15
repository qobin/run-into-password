#!/usr/bin/python
# -*- coding:utf-8 -*-

import logging
import create_password


class Password():

    def __init__(self, hashTup, currentWords=None, num=4, head="0"):
        self.hashTup = hashTup
        self.totalSize = len(hashTup)
        if not self.totalSize:
            self.totalSize = 0
        self.num = num
        self.head = head
        if not currentWords:
            self.currentWords = ""
            for i in range(0, num):
                self.currentWords += head
        else:
            self.currentWords = currentWords

    def getNextPassword(self, count=1):
        """
        use in get net password
        default add 1
        :return:
        """
        if self.totalSize <= 0:
            logging.warning("hash map is null")
            return self.currentWords
        else:
            return self.__add()

    def __add(self, currentList=None, pos=-1, count=1):
        """
        password add a count
        default last element
        :param count:
        :return:
        """
        if not currentList:
            currentList = list(self.currentWords)
        currentPos = self.hashTup.index(currentList[pos]) + count
        if currentPos >= self.totalSize:
            currentList[pos] = self.hashTup[0]
            self.__add(currentList, pos - 1, 1)
        else:
            currentList[pos] = self.hashTup[currentPos]
        self.currentWords = "".join(currentList)
        return self.currentWords


if __name__ == "__main__":
    password = Password(create_password.tup_total )
    for i in range(0, 10000):
        passstr = password.getNextPassword()
        print passstr