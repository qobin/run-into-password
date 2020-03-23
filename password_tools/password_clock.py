#!/usr/bin/python
# -*- coding:utf-8 -*-

import logging
import create_password


# 密码生成器
class Password:

    def __init__(self, hash_tup, current_words=None, num=4, head=None):
        self.hash_tup = hash_tup
        self.total_size = len(hash_tup)
        if not self.total_size:
            self.total_size = 0
        self.num = num
        self.head = head
        if not current_words:
            self.current_words = ""
            if not head:
                head = "0"
            self.current_words += head
            for i in range(1, num):
                self.current_words += self.hash_tup[0]
        else:
            self.current_words = current_words

    # 顺序密码生成器
    # count 为间隔
    # 设置不同的首字母可以用于分片
    # 如果不设置首字母则进行全局唯一
    def next_order_password(self, count=1):
        """
        use in get net password
        default add 1
        :return:
        """
        if self.total_size <= 0:
            logging.warning("hash map is null")
        else:
            current_list = list(self.current_words)
            if self.head:
                current_list.remove(current_list[0])
                self.current_words = self.head + self.__add(current_list=current_list, count=count)
            else:
                self.current_words = self.__add(current_list=list(self.current_words), count=count)
        return self.current_words

    # 顺序密码生成器算法规则
    # 思想四不确定进制
    # 类似于10进制，24进制，60进制等等
    def __add(self, current_list=None, pos=-1, count=1):
        """
        password add a count
        default last element
        :param count:
        :return:
        """
        if not current_list:
            current_list = list(self.current_words)
        currentPos = self.hash_tup.index(current_list[pos]) + count
        if currentPos >= self.total_size:
            current_list[pos] = self.hash_tup[0]
            self.__add(current_list, pos - 1, 1)
        else:
            current_list[pos] = self.hash_tup[currentPos]
        return "".join(current_list)

    # 返回是否还有下一个密码
    def has_next(self):
        """
        has_next_password?
        yes result true
        no result false
        :return:
        """
        current_list = list(self.current_words)
        last_word = self.hash_tup[-1]
        if self.head:
            current_list.remove(current_list[0])
        for w in current_list:
            if w != last_word:
                return True
        return False


if __name__ == "__main__":
    password = Password(create_password.tup_total, head="a", num=6)
    while True:
        strPassword = password.next_order_password()
        print strPassword
        if not password.has_next():
            print "create password end"
            break
