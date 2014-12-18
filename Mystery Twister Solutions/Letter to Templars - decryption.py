#!/usr/bin/python3.4
# Written by Anirudh Anand (lucif3r) : email - anirudh@anirudhanand.com

# Letter to Templars.py: A python program to de-cipher strings using keys
# This is a simple python program which helps in cracking Ciphers based on
# keys. This is written in general to work with any length of keys but is
# originally written to crack the challenge: Letter to Templars series in
# Mystery Twister. Challenge url:  http://goo.gl/nwzTr1

__author__ = 'lucif3r'

import itertools
import argparse


class Templar:
    def __init__(self):
        self.plain = ""

    def crack(self, cipher, key, outfile=""):
        """
        This function will intake the cipher text, key and the optional
        argument outfile (file to which output should be written). The
        function will first calculate all the possible permutations of
        the given key and use every single one of them to brute force
        the cipher.

        :type outfile: str
        :param cipher: The cipher text
        :param key:  Sample key/string which should be used for permuting
        :param outfile: File to which output should be written (optional)
        :return:
        """
        keys = self.permute_keys(key)
        for i in keys:
            j = -1
            while j < len(cipher) - len(key) + 1:
                self.plain += cipher[j + int(i[0])]
                self.plain += cipher[j + int(i[1])]
                self.plain += cipher[j + int(i[2])]
                self.plain += cipher[j + int(i[3])]
                j += len(key)
            self.print_args(i, outfile)
            self.plain = ""
        return self.plain

    def print_args(self, key, outfile=" "):
        """
        This will check if an output file is specified in the arguments
        if so, then the output will be written to the file or else it
        will be printed on the terminal

        :param key:
        :param outfile: File to which output should be written
        :return:
        """
        if outfile == " ":
            print("Key: ", key)
            print("Decrypted String: ", self.plain)
            return
        else:
            file = open(outfile, "a")
            file.write("\nkey: " + key + "\nDecrypted String: " + self.plain + "\n")
            return

    def permute_keys(self, words):
        """
        This function will return all the permutations of the key which
        is used to decrypt the cipher.

        :type words: list
        :param words: The words which is used to permute
        :return:
        """
        list_pass = [''.join(i) for i in itertools.permutations(words)]
        print(len(list_pass))
        return list_pass


def main():
    c = Templar()
    parser = argparse.ArgumentParser(description='To decipher a string using the given key')
    parser.add_argument('-k', '-key', type=str, default=0,
                        help='Enter a sample key (we will permutate and give results of all possibilities)')
    parser.add_argument('-c', '-cipher', type=str, default=" ",
                        help='File in which the cipher is saved')
    parser.add_argument('-o', '-output', type=str, default=" ",
                        help='Output the result to a file')
    args = parser.parse_args()

    if args.k == 0:
        print("Please enter a valid key. Use -h to see help commands")
        exit(0)
    if args.c == " ":
        print("A valid file containing cipher is required. Use -h to see help commands")
        exit(0)
    else:
        try:
            cipher = open(args.c, "r").readline()
        except FileNotFoundError:
            print("File not Found. Please enter a valid file")

    c.crack(cipher, args.k, args.o)
    return


if __name__ == '__main__':
    main()