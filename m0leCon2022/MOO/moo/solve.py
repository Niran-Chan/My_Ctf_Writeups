from pwn import *
import re
r = remote("challs.m0lecon.it",1753)
r.recvline()
n = r.recvuntil('\n')
n = int(b''.join(re.split(b'n = ',n)))

c = r.recvuntil('\n')
c = int(b''.join(re.split(b'c = ',c)))
e = 65537

r.recv()


r.close()