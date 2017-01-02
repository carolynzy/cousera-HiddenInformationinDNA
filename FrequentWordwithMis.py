#!/usr/bin/python
import itertools

file=open('test.txt')
sequence=file.read()
d=int(raw_input('Enter d here: '))
k=int(raw_input('Enter k here: '))

i=0
list_all=[]
unique=set()
length=len(sequence)
neighbor=set()
for c in sequence:
	if i+k<=length-1:
		pattern=sequence[i:i+k]
		list_all.append(pattern)
	if i+k==len(sequence):
		pattern=sequence[i:]
		list_all.append(pattern)
	i+=1
for pattern in list_all:
	unique.add(pattern)
print(unique)

for pattern in unique:
	if d==0:
		print(pattern)
	else:
		length=len(pattern)
		pos=[i for i in range(0,length)]
		letter=['A','C','G','T']
		if length<d:
			print('Error! d should not be greater than the length of the pattern')
		else:
			d0=1
			while d0<=d:
				combination_iter=itertools.combinations(pos,d0)
				permutation_iter=itertools.permutations(letter,d0)
				combination=[]
				permutation=[]
				for com in combination_iter:
					combination+=[com]
				for per in permutation_iter:
					permutation+=[per]
				print(combination)
				print(permutation)
				for item in combination:
					str_list=[i for i in pattern]
					for change in permutation:
						for i in change:
							str_list[item[change.index(i)]]=i
						neighbor.add(''.join(str_list))
				d0+=1
print(neighbor)
count_all={}
for match_d in neighbor:
	len_match=len(match_d)
	count=0
	for item in list_all:
		dis=0
		for i in range(0,len_match):
			if match_d[i]!= item[i]:
				dis+=1
		if dis<=d:
			count+=1
	count_all[match_d]=count
max=max(count_all.values())
print(max)
for match_d in neighbor:
	if count_all[match_d]==max:
		print(match_d)	
file.close()		

		
		
		
		
		
		
		
		
		
		
		
	
		
	