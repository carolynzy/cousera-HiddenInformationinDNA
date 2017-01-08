#!/usr/bin/python

import sys
input = sys.stdin.read()
tokens = input.split()
k=int(tokens[0])

# create all Kmer array
array={}
dict={0:'A',1:'C', 2:'G',3:'T'}
for i in range(0, 4**k):
    count=0
    I=i
    K=k
    list=['A']*k
    while K-1>=0:
        if I >= 4**(K-1)*3:
            list[count]='T'
            I-=4**(K-1)*3
        elif 4**(K-1)*2<=I<4**(K-1)*3:
            list[count]='G'
            I-=4**(K-1)*2
        elif 4**(K-1)<=I<4**(K-1)*2:
            list[count]='C'
            I-=4**(K-1)
        elif 0<=I<4:
            list[-1]=dict[I]
        count+=1
        K-=1
    array[''.join(list)]=i  


# find the k-neighbor of all patterns in all sequences
length=len(tokens[1])
kmers=array.keys()
t=len(tokens)
for i in range(1,t):
	sequence=tokens[i]
	unique=set()
	neighbor=set()
	for j in range(0,length-k+1):
		pattern=sequence[j:j+k]
		unique.add(pattern)
	for pattern in unique:
		for kmer in kmers:
			dis=0
			for j in range(0,k):
				if pattern[j]!= kmer[j]:
					dis+=1
			if dis <=k:
				neighbor.add(kmer)

# distance of each pattern in the neighbor to the sequences
matrix={}
for pattern in neighbor:
	dis=0
	for i in range(1,t):
		string=tokens[i]
		hd=k
		for j in range(0,length-k+1):
			kmer=string[j:j+k]
			h=0
			for c in range(0,k):
				if pattern[c]!=kmer[c]:
					h+=1
			if hd>h:
				hd=h
		dis+=hd
	matrix[pattern]=dis


# minimum distance of pattern
min_pattern=[]
min_dis=min(matrix.values())
for pattern in neighbor:
	if matrix[pattern]==min_dis:
		min_pattern+=[pattern]
print(' '.join(min_pattern))



