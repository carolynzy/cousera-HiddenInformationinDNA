#!/usr/bin/python
#find the all the K-mers in a sequence of length L appears at least t times


#import sy#s
#input = sys.stdin.read()
#tokens = input.split()
#sequence=tokens[0]
#k=int(tokens[1])
#L=int(tokens[2])
#t=int(tokens[3])

#sequence=input('sequence: ')
file=open('E_coli.txt')
sequence=file.read()
k=int(input('k: '))
L=int(input('L: '))
t=int(input('t: '))


length=len(sequence)
sub_seq=sequence[0:L]
pattern_list=[]
pattern_unique=set()
freq={}
clump=set()
for j in range(0,L-k+1):
	pattern=sub_seq[j:j+k]
	pattern_list+=[pattern]
	pattern_unique.add(pattern)
	
for pattern in pattern_unique:
	freq[pattern]=pattern_list.count(pattern)
	if pattern_list.count(pattern)>=t:
		clump.add(pattern)
		
for i in range(0,length-L+1):
	first_pattern=sequence[i:i+k]
	last_pattern=sequence[i+L-k+1:i+L+1]
	freq[first_pattern]-=1
	if last_pattern in freq.keys():
		freq[last_pattern]+=1
		if freq[last_pattern]>=t:
			clump.add(last_pattern)
	else:
		freq[last_pattern]=1
print(len(clump))
file.close()
