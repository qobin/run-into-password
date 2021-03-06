#!/usr/bin/python
# -*- coding:utf-8 -*-

## 下一版修改时，根据用户使用规则，只有首字母才会大写，其他的不会
## 特殊字符一般是  “.” 和  “@”
tup_num = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
tup_words = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
              'u', 'v', 'w', 'x', 'y', 'z')
tup_big = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
              'U', 'V', 'W', 'X', 'Y', 'Z')
top_spec = ('!', '@', '#', '$', '%')

tup_total = tup_num + tup_words + tup_big + top_spec


# 承载生成的密码
# password： 明文密码
# password_md5：md5加密密码
# password_sha：sha家秘密吗
class PasswordObj:

    def __init__(self, password, password_md5, password_sha):
        self.password = password
        self.password_md5 = password_md5
        self.password_sha = password_sha

    def __str__(self):
        return "password: " + self.password + ",password_md5: " + self.password_md5 \
               + ",password_sha: " + self.password_sha


from password_tools.password_clock import Password
import hashlib


def create_password_file(num, head=None):
    # list_password = []
    # i = 0
    # sql =
    sql_file = open("F:\\camp\\4.sql", "w+")
    # sql = "insert into camp('password', 'password_md5') value "
    # sql_file.write(sql + "\n")
    if 4 <= num < 12:
        password_creator = Password(tup_total, num=num)
        md5_tools = hashlib.md5()
        # sha256_tools = hashlib.sha256()
        while password_creator.has_next():
            password_str = password_creator.next_order_password()
            md5_tools.update(password_str)
            # sha256_tools.update(password_str)
            sql = "insert into camp('password', 'password_md5') value ('%s', '%s')" % (password_str, md5_tools.hexdigest())
            sql_file.write(sql + "\n")

        #     obj = PasswordObj(password_str, md5_tools.hexdigest(), sha256_tools.hexdigest())
        #     list_password.append(obj)
        #     if len(list_password) == 100:
        #         break
        # return list_password
            # if i < 10:
            #     list_password.append(obj)
            # else:
            #     i = 0
            #     list_password.clear()
            #     list_password.append(obj)
            # print list_password
    sql_file.close()
    print "well done"


import MySQLdb
def create_password_db(num, head=None):
    mysqldb = MySQLdb.connect(host='127.0.0.1', user='modesty', passwd='x3cKKpTiLa2Dprkj', db='modesty')
    cursor = mysqldb.cursor()
    i = 0
    if 4 <= num < 12:
        password_creator = Password(tup_total, num=num)
        md5_tools = hashlib.md5()
        # sha256_tools = hashlib.sha256()
        mysqldb.begin()
        while password_creator.has_next():
            i += 1
            password_str = password_creator.next_order_password()
            md5_tools.update(password_str)
            sql = "insert into camp(password, password_md5) value (\"%s\", \"%s\");" % (password_str, md5_tools.hexdigest())
            cursor.execute(sql)
            if i == 1000:
                mysqldb.commit()
                i = 0
                mysqldb.begin()
    mysqldb.commit()
    mysqldb.close()


if __name__ == "__main__":
    create_password_db(num=4)
    # for obj in list_total:
    #     print len(obj.password), len(obj.password_md5), len(obj.password_sha)