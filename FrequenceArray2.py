#!/usr/bin/python
# create frequence array for K-mers and return the result for a sequence


K=int(input('Enter K here: '))
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

file=open("dataset_2994_5.txt", 'r')
seq=file.read()
i=0
list2=[]
unique=set()
for c in seq:
	if i+K<=len(seq)-1:
		pattern=seq[i:i+K]
		list2.append(pattern)
	if i+K==len(seq):
		pattern=seq[i:]
		list2.append(pattern)
	i+=1
for pattern in list2:
	unique.add(pattern)


list3=['0']*4**K
for pattern in unique:
	initial=pattern[0]
	range=[pos for pos, char in enumerate(seq) if char == initial]
	len1=len(pattern)
	len2=len(seq)
	count=0
	for i in range:
		if i<len2-len1:
			if seq[i:i+len1]==pattern:
				count+=1
		elif i==len2-len1:
			if seq[i:]==pattern:
				count+=1
	I=array[pattern]
	list3[I]=str(count)
file.close()
print(' '.join(list3))




