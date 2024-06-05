from z3 import *

LEN = 37
mul = [73, 45, 69, 78, 57, 38, 40, 25, 45, 78, 26, 65, 33, 82, 96, 34, 93, 78, 36, 16, 75, 58, 96, 94, 69, 25, 27, 98, 94, 50, 9, 60, 43]
constraint = 172921

if 0:
	with open('flag.txt', 'r') as f:
		test_flag = f.read()

	res = 0
	i = 0
	gap = 0
	while i < LEN - gap:
		char = ord(test_flag[LEN-i-1-gap])
		prod = (mul[i]+1) * char
		print(mul[i], char, prod, res, test_flag[:LEN-i-1 - gap], sep='\t')
		res += prod
		if i in [8, 9, 23, 27]:
			gap += 1
			res += ord(test_flag[LEN-i-1-gap])
		i += 1

	print(constraint, res)




flag = [BitVec(f'c{i}', 16) for i in range(LEN)]
s = Solver()

# openECSC{ABCDEFGHIJKLMNOPQRSTUVWXYZ_}

for i in range(9, LEN-1):
	s.add(Or(
		And(flag[i] >= 0x30, flag[i] <= 0x39),
		And(flag[i] >= 0x41, flag[i] < 0x5b),
		And(flag[i] >= 0x61, flag[i] < 0x7b),
		flag[i] == ord('_'),
	))

'''
for i in range(32, 127):
	print(i, chr(i))
'''


s.add(flag[0] == ord('o'))
s.add(flag[1] == ord('p'))
s.add(flag[2] == ord('e'))
s.add(flag[3] == ord('n'))
s.add(flag[4] == ord('E'))
s.add(flag[5] == ord('C'))
s.add(flag[6] == ord('S'))
s.add(flag[7] == ord('C'))
s.add(flag[8] == ord('{'))
s.add(flag[LEN-1] == ord('}'))

res = 0
i = 0
gap = 0
while i < (LEN - gap):
	char = flag[LEN-i-1-gap]
	prod = (mul[i]+1) * char
	print(mul[i], char, prod, test_flag[:LEN-i-1-gap], sep='\t')
	res += prod
	if i in [8, 9, 23, 27]:
		gap += 1
		res += flag[LEN-i-1-gap]
	i += 1

s.add(res == constraint)

# print(s)

while s.check() == sat:
	m = s.model()
	print(''.join([
		chr(m[flag[i]].as_long())
		for i in range(LEN)
	]))

	s.add(Or([
		flag[i] != m[flag[i]].as_long()
		for i in range(LEN)
	]))