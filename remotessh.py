#!/usr/bin/python

import pxssh
import getpass
import sys


try:
    s = pxssh.pxssh()
    hostname = sys.argv[1]
    username = sys.argv[2]
    password = sys.argv[3]
    command = sys.argv[4]
    s.login (hostname, username, password)
    s.sendline ('uptime')
    s.prompt()
    print s.before
    s.sendline (command)
    s.prompt()
    print s.before
    s.logout()
except pxssh.ExceptionPxssh, e:
    print "pxssh failed on login."
    print str(e)
