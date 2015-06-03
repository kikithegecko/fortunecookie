import subprocess

# step 1: get a fortune that is not too long
fortune = ''
while (fortune == '') or (len(fortune) > 140):
	fortune = subprocess.getoutput('fortune')
	fortune = fortune.replace('\t', ' ')
	fortune = fortune.replace('\n', ' ')
#print("Your fortune is:")
#print(fortune)

# step 2: insert newlines, so that line width is at most 28 chars.
lines = []
for i in range(5):
	pos = 28
	try: # check if the remaining fortune is shorter than 28 chars
		fortune[pos]
	except:
		lines.append(fortune)
		fortune = ''
		break
	while fortune[pos] != ' ':
		pos -= 1
	#fortune[pos] = '' # so that the new line doesn't start with a space
	lines.append(fortune[:pos].lstrip())
	fortune = fortune[pos:].lstrip()
#for i in range(len(lines)):
#	print(lines[i])
if len(fortune) > 0:
	print("PANIC! Fortune turned out to be too long. This is the rest:")
	print(fortune)
