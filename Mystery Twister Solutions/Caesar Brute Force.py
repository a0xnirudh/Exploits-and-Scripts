#!/usr/bin/python3.4
# Written by Anirudh Anand (lucif3r) : email - anirudh@anirudhanand.com

# Caesar Brute force.py: A python program to Crack caesar/Rotational ciphers
# This is a simple python program which helps in cracking Caesar/rotational
# cipher.The program basically works in the following way (must have 3 args):
# From the Cipher each character is analysed and is processed accordingly
# if it is a lower case or an upper case letters.

#The Non-Alphabetic chars are retained in the decrypted plain text message.

__author__ = 'lucif3r'

import argparse
import sys


class CipherBrute:

    def __init__(self):
        self.plain = ''

    def cipher_brute(self, rot, cipher):
        """
        The function will intake the cipher and possible rotation amount
        to decrypt it. If a rotation amount is not specified, this will
        print every possibilities from 1 - 26

        :rtype : String
        :param rot: Amount of Rotation to be tested
        :param cipher: The original Cipher to decrypt
        :return:
        """
        for i in str(cipher):

            self.non_alpha(i)

            if i.isupper():  # Calling the upper_brute function if character
                             # is in upper case
                self.upper_brute(i, rot)

            if i.islower():  # Calling the lower_brute function if character
                             # is in lower case
                self.lower_brute(i, rot)

            if not i.isalpha():  # If the character is not alphabet, then
                                 # it is simply added to the decrypted string
                self.plain += i

        return self.plain

    def non_alpha(self, i):
        """
        If the character is non-alphabet, we will leave it as it is and
        will be simply added to the plain decrypted text also (eg: space)

        :type self: NULL
        :param i: Individual character from the cipher string
        :return:
        """
        if i == " ":
            self.plain += " "
        return

    def lower_brute(self, i, rot):
        """
        If the cipher character is in lower case, this function will be
        invoked which checks if the rotation amount goes bigger than the
        ascii value of z and if so, we are returned it to the beginning.

        :rtype : None
        :param i: Individual Character from the cipher string
        :param rot: Amount of rotation
        """
        if ord(i)+rot > 122:
            self.plain += chr(ord(i)+rot-26)
        else:
            self.plain += chr(ord(i) + rot)
        return

    def upper_brute(self, i, rot):
        """
        If the cipher character is in upper case, this function will be
        invoked which checks if the rotation amount goes bigger than the
        ascii value of Z and if so, we are returned it to the beginning.

        :type self: None
        :param i: Individual Character from the cipher string
        :param rot: Amount of Rotation
        """
        if ord(i)+rot > 90:
            self.plain += chr(rot+ord(i)-26)
        else:
            self.plain += chr(ord(i) + rot)

    def print_args(self, i, plain, output=" "):
        """
        Function which handles the output. If an output file is specified,
        then the results in written into the file and is not shown in the
        terminal

        :param output: The output file to write (if specified)
        :param i: Individual character in the cipher text
        :param plain: The decrypted plain text
        """
        if output == " ":
                print("ROT: ", i)
                print("Decrypted Text: ", plain, "\n")
                return
        else:
            outfile = open(output, "a")
            outfile.write("Rot: " + str(i) + "\nDecrypted Text: " + str(plain) + "\n \n")
            return


def main():
    parser = argparse.ArgumentParser(description='To Break the Ceasar/Rotation cipher')
    parser.add_argument('-r', '-rot', type=int,
                        help='Rotation amount (use -a for default:- Will print all the possibilities)')
    parser.add_argument('-c', '-cipher', type=str,
                        help='String to decipher')
    parser.add_argument('-a', '-all', action="count",
                        help='Brute force with All rotations from 1 to 26')
    parser.add_argument('-o', '-output', type=str, default=" ",
                        help='Output the result to a file')
    args = parser.parse_args()

    if len(sys.argv) < 3:
        print(''' usage: Caesar Brute Force.py [-h] [-r R] [-c C] [-a]

To Break the Ceasar/Rotation cipher

optional arguments:
  -h , --help    show this help message and exit
  -r , -rot      Rotation amount (Use -a for default:- Will print all the possibilities)
  -c , -cipher   String to decipher (Should be enclosed in double)
  -a , -all      Brute force with All rotations from 1 to 26 ''')
        exit(0)
    if args.a:
        #if -a parameter is specified, we need to print all possibilities
        #from 0 - 26
        for i in range(1, 26):
            c = CipherBrute()
            plain = c.cipher_brute(i, args.c)
            c.print_args(i, plain, args.o)

    else:
        c = CipherBrute()
        plain = c.cipher_brute(args.r, args.c)
        c.print_args(args.r, plain, args.o)

    return

if __name__ == '__main__':
    main()