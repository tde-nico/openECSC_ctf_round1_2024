with open('b.txt', 'r') as f:
	src = f.read()

blocks = src.split('# *')

LEN = len(blocks)

consts = []
constraints = []

for i in range(LEN-1):
	conds = blocks[i].split('<')

	constraint = conds[-1].strip().split('\n')[-1].split(' ')[0]

	const = []
	for j, cond in enumerate(conds):
		if j == 0:
			continue
		tmp = cond[1:].split(',')[0]
		const.append(int(tmp))

	consts.append(const)
	constraints.append(int(constraint))	

print(consts)
print(constraints)

