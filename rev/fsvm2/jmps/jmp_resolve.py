from pwn import *
import os

context.log_level = 'error'

while True:
	os.system('python3 decompile.py')
	r = process(['python3', 'source2.py'])
	jmp = r.recvline().decode().strip()
	jmp = int(jmp.split('jmp ')[1])
	start = r.recvline().decode().strip()
	start = int(start[3:])
	print(start, jmp)
	with open('jmps.txt', 'a') as f:
		f.write(f'{start},{jmp}\n')
	r.close()

	#input()


# print(r0, r1, r2, r3, r4, r5, r6, r7, r8, r9, ra, rb, rc, rd, re, rf)