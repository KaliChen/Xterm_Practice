from __future__ import print_function
import platform
import sys
import pexpect

makeclean_child = pexpect.spawn('ssh '+sys.argv[2]+'@'+sys.argv[1])
makeclean_child.expect ('password:')
makeclean_child.sendline (sys.argv[3])
makeclean_child.sendline('cd Desktop/Xterm_Practice/TestSocket')
makeclean_child.sendline('make clean')
print(server_child.before)
makeclean_child.interact()