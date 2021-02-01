from __future__ import print_function
import pexpect
client_child = pexpect.spawn('ssh '+sys.argv[2]+'@'+sys.argv[1])
client_child.expect ('password:')
#server_child.sendline ('raspberry')
client_child.sendline (sys.argv[3])
#child.expect ('~$')
#child.sendline ('ifconfig')
client_child.sendline('cd ~/Xterm_Practice/TestSocket')
client_child.sendline('ls')
client_child.sendline('./client1')
print(client_child.before)
client_child.interact()
