from pwn import *
from string import printable

context.log_level = 'error'

p = printable[:-6]

i = 0
j = 0
LEN = 29
flag = ['_'] *  LEN

while i < LEN:

	r = process(['python3', 'source.py'])
	r.recvline()

	flag[i] = p[j]
	print(''.join(flag))
	r.sendline(''.join(flag).encode())

	res = r.recvline()
	if res[i] == 48:
		i += 1
		j = 0
	else:
		j += 1
	r.close()

# openECSC{supereasyvmc4e87c4d}
