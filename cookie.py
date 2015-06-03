import subprocess

# step 1: get a fortune that is not too long
fortune = ''
while (fortune == '') or (len(fortune) > 140):
	fortune = subprocess.getoutput('fortune')
	fortune.replace('\t', ' ')
	print("Your fortune is:")
	print(fortune)
