
with open('bytecode', 'rb') as f:
	bytecode = f.read()

rip = 0


ops = {
	'(': 'print(f"jmp {r5}")',
	')': 'if r6 == r7: print(f"{r6} == {r7} jmp {r5}")',
	'*': 'if r6 != r7: print(f"{r6} != {r7} jmp {r5}")',
	'+': 'if r6 < r7: print(f"{r6} < {r7} jmp {r5}")',
	',': 'r0 = ""',
	'-': 'r1 = ""',
	'.': 'r2 = ""',
	'/': 'r3 = ""',
	'0': 'r4 = ""',
	'1': 'r5 = ""',
	'2': 'r6 = ""',
	'3': 'r7 = ""',
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
	'Q': '',
	'R': '',
	'S': '',
	'T': '',
	'U': 'print(r4)',
	'V': 'r0 = input()',
	'W': 'exit()',
}

source = ''

while rip < len(bytecode):
	opcode = bytecode[rip]
	curr_op = rip

	op = ops.get(opcode.to_bytes(1, 'big').decode(), None)
	if op is None:
		print('Unknown opcode: 0x{:02x} {}'.format(opcode, bytes([opcode])))
		break

	opcode = opcode.to_bytes(1, 'big').decode()

	if opcode == '=':
		reg = bytecode[rip + 1]
		off = bytecode[rip + 2]
		op += f'r{off} = str(ord(r{reg}[len(r{reg})-1]))'
		rip += 2

	elif opcode == '>':
		reg = bytecode[rip + 1]
		reg2 = bytecode[rip + 2]
		op += f'r{reg2} = chr(int(r{reg}))'
		rip += 2

	elif opcode == '?':
		reg1 = bytecode[rip + 1]
		reg2 = bytecode[rip + 2]
		reg3 = bytecode[rip + 3]
		op += f'r{reg3} = r{reg1} + r{reg2}'
		rip += 3

	elif opcode == 'Q':
		reg1 = bytecode[rip + 1]
		reg2 = bytecode[rip + 2]
		reg3 = bytecode[rip + 3]
		op += f'r{reg3} = str(int(r{reg1}) + int(r{reg2}))'
		rip += 3

	elif opcode == 'R':
		reg1 = bytecode[rip + 1]
		op += f'r{reg1} += "1"'
		rip += 1
	
	elif opcode == 'S':
		reg = bytecode[rip + 1]
		op += f'if len(r{reg}):\n\tr{reg} = r{reg}[:-1]'
		rip += 1
	
	elif opcode == 'T':
		reg1 = bytecode[rip + 1]
		op += f'if r{reg1}[0] == \'-\':\n\tr{reg1} = 0\nelse:\n\tr{reg1} = "-" + r{reg1}' # maybe?
		rip += 1


	source += op + f" # {curr_op}\n"
	rip += 1


with open('source.py', 'w') as f:
	f.write(source)
