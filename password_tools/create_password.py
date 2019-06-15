#!/usr/bin/python
# -*- coding:utf-8 -*-

tup_num = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
tup_words = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
              'u', 'v', 'w', 'x', 'y', 'z')
tup_big = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
              'U', 'V', 'W', 'X', 'Y', 'Z')
top_spec = ('!', '@', '#', '$', '%')

tup_total = tup_num + tup_words + tup_big + top_spec

list_password = []
def createPassword( num ):
    if num < 4 or num >= 12:
        return 0
    else:
        for i in (0, len(tup_total)):
            str1 = ""
            for j in range(0, num):
                str1 += tup_total[i]