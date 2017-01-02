#!/usr/bin/python

pattern=raw_input('Enter your pattern here: ')
d=int(raw_input('Enter d here: '))
neighbor=set()
if d==0:
	print(pattern)
else:
	K=len(pattern)
	array={}
	dict={0:'A',1:'C', 2:'G',3:'T'}		
	for I in range(0, 4**K):
		count=0
		list=['A']*K
		k=K
		i=I
		while k-1>=0:
			if i >= 4**(k-1)*3:
				list[count]='T'
				i-=4**(k-1)*3
			elif 4**(k-1)*2<=i<4**(k-1)*3:
				list[count]='G'
				i-=4**(k-1)*2
			elif 4**(k-1)<=i<4**(k-1)*2:
				list[count]='C'
				i-=4**(k-1)
			elif 0<=i<4:
				list[K-1]=dict[i]		
			count+=1
			k-=1
		array[''.join(list)]=I
	if len(pattern)<d:
		for i in array.keys():
			print(i)
	else:
		kmers=array.keys()
		for key in kmers:
			dis=0
			for i in range(0,len(pattern)):
				if pattern[i]!= key[i]:
					dis+=1
			if dis <=d:
				neighbor.add(key)
		for i in neighbor:
			print(i)

			
		

		
	
