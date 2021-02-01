from __future__ import print_function
import pexpect
server_child = pexpect.spawn('ssh '+sys.argv[2]+'@'+sys.argv[1])
server_child.expect ('password:')
server_child.sendline (sys.argv[3])
server_child.sendline('cd ~/Xterm_Practice/TestSocket')
server_child.sendline('ls')
server_child.sendline('./server1)
print(server_child.before)
server_child.interact()
