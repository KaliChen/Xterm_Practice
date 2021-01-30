from __future__ import print_function
import platform
import sys
import pexpect
make_child = pexpect.spawn('ssh '+sys.argv[2]+'@'+sys.argv[1])
make_child.expect ('password:')
make_child.sendline (sys.argv[3])
make_child.sendline('cd Desktop/Xterm_Practice/TestSocket')
#print(gZCchild.before)   # Print the result of the ls command.
make_child.sendline('make')
print(make_child.before)
make_child.interact()
