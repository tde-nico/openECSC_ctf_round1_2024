
with open('bytecode', 'rb') as f:
	bytecode = f.read()

rip = 0

with open('jmps.txt', 'r') as f:
	jumps = [list(map(int, line.split(','))) for line in f]

# 3907,116617


ops = {
	'(': 'print(f"jmp {ra}")',
	')': 'if (rb == rc): print(f"{rb} == {rc}, jmp {ra}")',
	'*': 'if (rb != rc): print(f"{rb} != {rc}, jmp {ra}")',
	'+': 'if (rb < rc or 1): print(f"{rb} < {rc}, jmp {ra}")',
	',': 'r0 = ""',
	'-': 'r1 = ""',
	'.': 'r2 = ""',
	'/': 'r3 = ""',
	'0': 'r4 = ""',
	'1': 'r5 = ""',
	'2': 'r6 = ""',
	'3': 'r7 = ""',
	'4': 'r8 = ""',
	'5': 'r9 = ""',
	'6': 'ra = ""',
	'7': 'rb = ""',
	'8': 'rc = ""',
	'9': 'rd = ""',
	':': 're = ""',
	';': 'rf = ""',
	'=': '',
	'>': '',
	'?': '',
	'@': 'r0 = "0"',
	'A': 'r1 = "0"',
	'B': 'r2 = "0"',
	'C': 'r3 = "0"',
	'D': 'r4 = "0"',
	'E': 'r5 = "0"',
	'F': 'r6 = "0"',
	'G': 'r7 = "0"',
	'H': 'r8 = "0"',
	'I': 'r9 = "0"',
	'J': 'ra = "0"',
	'K': 'rb = "0"',
	'L': 'rc = "0"',
	'M': 'rd = "0"',
	'N': 're = "0"',
	'O': 'rf = "0"',
	'P': '',
	'Q': '',
	'R': '',
	'S': '',
	'T': '',
	'U': 'print(rf)',
	'V': 'if not os.path.exists(r0): r0 = "-1"\nelse:\n\ttry:\n\t\tr0 = eval(f"r{r0}")\n\texcept:\n\t\twith open(r0, "r") as f:\n\t\t\tr0 = f.read()',
	'W': 'exit()',
}

source = dict()
rips = []


while rip < len(bytecode):
	opcode = bytecode[rip]
	curr_op = rip

	op = ops.get(opcode.to_bytes(1, 'big').decode(), None)
	if op is None:
		print('Unknown opcode: 0x{:02x} {}'.format(opcode, bytes([opcode])))
		break
	opcode = opcode.to_bytes(1, 'big').decode()


	if opcode == '=':
		reg1 = hex(bytecode[rip + 1])[2:]
		reg2 = hex(bytecode[rip + 2])[2:]
		op += f'r{reg2} = str(ord(r{reg1}[len(r{reg1})-1]))'
		rip += 2
	
	elif opcode == '>':
		reg1 = hex(bytecode[rip + 1])[2:]
		reg2 = hex(bytecode[rip + 2])[2:]
		op += f'r{reg2} = chr(int(r{reg1}) % 256)'
		rip += 2

	elif opcode == '?':
		reg1 = hex(bytecode[rip + 1])[2:]
		reg2 = hex(bytecode[rip + 2])[2:]
		reg3 = hex(bytecode[rip + 3])[2:]
		op += f'r{reg3} = r{reg1} + r{reg2}'
		rip += 3

	elif opcode == 'P':
		reg1 = hex(bytecode[rip + 1])[2:]
		reg2 = hex(bytecode[rip + 2])[2:]
		op += f'r{reg2} = r0 = str(len(r{reg1}))'
		rip += 2
	
	elif opcode == 'Q':
		reg1 = hex(bytecode[rip + 1])[2:]
		reg2 = hex(bytecode[rip + 2])[2:]
		reg3 = hex(bytecode[rip + 3])[2:]
		op += f'r{reg3} = str(int(r{reg1}) + int(r{reg2}))'
		rip += 3

	elif opcode == 'R':
		reg1 = hex(bytecode[rip + 1])[2:]
		op += f'r{reg1} += "1"'
		rip += 1
	
	elif opcode == 'S':
		reg = hex(bytecode[rip + 1])[2:]
		op += f'if len(r{reg}):\n\tr{reg} = r{reg}[:-1]'
		rip += 1
	
	elif opcode == 'T':
		reg1 = hex(bytecode[rip + 1])[2:]
		op += f'if r{reg1}[0] == \'-\':\n\tr{reg1} = r{reg1}[1:]\nelse:\n\tr{reg1} = "-" + r{reg1}'
		rip += 1

	if opcode in 'U()*+':
		if opcode != 'U':
			op = op.replace('{ra}', f'{{int(ra)+{curr_op}}}')
		op += f'; print("# {opcode} {curr_op}")'


	rips.append(curr_op)
	source[curr_op] = op + f" # {curr_op}"
	rip += 1


src = ['import os\n']
rip = 0
k = 0
prev = -1

while k < len(rips)-1:

	# jump resolve
	'''
	for j in jumps:
		if rip == j[0]:
			rip = j[1] + 1
			prev = j[0]
			jumps.remove(j)
			break

	if rip == prev:
		src.append('print(r0, r1, r2, r3, r4, r8, sep="\\t")')
	'''
	src.append(source[rip])

	k = rips.index(rip)
	if k+1 < len(rips):
		rip = rips[k+1]


src = '\n'.join(src)
with open('source.py', 'w') as f:
	f.write(src)
