import sys
import string

l = list()
l = ['Adduser','Hydra_FTP','Hydra_SSH','Java_Meterpreter','Meterpreter','Web_Shell']
output = open('match3.txt','w')
read_file = open('data_feature_set_for_3gram.txt','r')
data_list = list()

dic = dict()
for line in read_file:
	line = line.rstrip('\n')
	data_list.append(line)
read_file.close()

for prefix in l:
	read_file = open('attack_sevengram_'+prefix+'.txt','r')
	for line in read_file:
		if line[0] != '$':
			line = line.rstrip('\n')
			words = line.split()
			temp = words[0]+" "+words[1]+" "+words[2]
			if temp in dic:
				dic[temp] += 1
			else:
				dic[temp] = 1
		else:
			line = line[2:]
			for i in range(1,5):
				var = str(words[i]+" "+words[i+1]+" "+words[i+2])
				if var in dic:
					dic[var] += 1
				else:
					dic[var] = 1	
			for l in data_list:
				if l in dic:
					output.write(str(dic[l])+' ')
				else:	
					output.write('0 ')
			output.write(prefix+'\n')
			dic.clear()		


read_file = open('normal_sevengram.txt','r')
for line in read_file:
	if line[0] != '$':
		line = line.rstrip('\n')
		words = line.split()
		temp = words[0]+" "+words[1]+" "+words[2]
		if temp in dic:
			dic[temp] += 1
	else:
		line = line[2:]
		for i in range(1,5):
			var = str(words[i]+" "+words[i+1]+" "+words[i+2])
			if var in dic:
				dic[var] += 1
		for l in data_list:
			if l in dic:
				output.write(str(dic[l])+' ')
			else:
				output.write('0 ')	
		output.write('normal\n')
		dic.clear()