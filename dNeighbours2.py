#!/usr/bin/python
import itertools

pattern=raw_input('Enter your pattern here: ')
d=int(raw_input('Enter d here: '))
neighbor=set()

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
			for item in combination:
				str_list=[i for i in pattern]
				for change in permutation:
					for i in change:
						str_list[item[change.index(i)]]=i
					neighbor.add(''.join(str_list))
			d0+=1
		for all in neighbor:
			print(all)
				
			
		
					
					
					
					
					
					
		
		
		
		
		
		
		
		
		
			