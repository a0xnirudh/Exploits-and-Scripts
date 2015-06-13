#!/usr/bin/python3.4
# Written by Anirudh Anand (lucif3r) : email - anirudh@anirudhanand.com

# This is the solution to 0ldzombie's Webhacking.kr Challenge 6: Base64 cookie encoding
# The script uses requests library in python 3.4

import base64

__author__ = 'lucif3r'


class Challenge6:

    def __init__(self):
        print("[+] 0ldZombie challenge6: - Base64 Cookie decode \n")
        return

    def encode_cookie(self, username, password):

        for i in range(1, 21):
            username = base64.b64encode(username)
            password = base64.b64encode(password)

        replace = {'1': '!', '2': '@', '3': '$', '4': '^', '5': '&', '6': '*', '7': '(', '8': ')'}

        username = self.replace_all(username, replace)
        password = self.replace_all(password, replace)

        self.print_all(username, password)
        return

    def replace_all(self, string, replace):
        """
        This function will take a dictionary as an input and replaces the values with its keys in the
        strings.

        :param string:       ->     The string which should be used to replace characters.
        :param replace:      ->     A dictionary which contains the words to be replaces with their keys
        :return:
        """
        for i, j in replace.iteritems():
            string = string.replace(i, j)

        return string

    def print_all(self, username, password):
        print("[+] Encoded username to be set as cookie is: \n \n" + username)
        print("\n[+] -------------------------------------------------------------------------------------------[+] \n")
        print("[+] Encoded password to be set as cookie is: \n \n" + password)
        return


def main():
    challenge6 = Challenge6()
    challenge6.encode_cookie('admin', 'admin')
    return

if __name__ == '__main__':
    main()

