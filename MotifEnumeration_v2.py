#!/usr/bin/python

import sys
input = sys.stdin.read()
tokens = input.split()
k=int(tokens[0])
d=int(tokens[1])

# create all Kmer array
array={}
dict={0:'A',1:'C', 2:'G',3:'T'}
for i in range(0, 4**k):
    count=0
    I=i
    K=k
    lst=['A']*k
    while K-1>=0:
        if I >= 4**(K-1)*3:
            lst[count]='T'
            I-=4**(K-1)*3
        elif 4**(K-1)*2<=I<4**(K-1)*3:
            lst[count]='G'
            I-=4**(K-1)*2
        elif 4**(K-1)<=I<4**(K-1)*2:
            lst[count]='C'
            I-=4**(K-1)
        elif 0<=I<4:
            lst[-1]=dict[I]
        count+=1
        K-=1
    array[''.join(lst)]=i  

motif=set()
sequence=tokens[2]
kmers=array.keys()
length=len(sequence)
unique=set()
for i in range(0,length-k+1):
	pattern=sequence[i:i+k]
	unique.add(pattern)

for pattern in unique:
	for kmer in kmers:
		dis=0
		for i in range(0,k):
			if pattern[i]!= kmer[i]:
				dis+=1
		if dis <=d:
			motif.add(kmer)
n=len(tokens)
motif_2=list(motif)		
for i in range(3,n):
	sequence=tokens[i]
	print(sequence)
	for pattern in motif:
		print(pattern)
		j=0
		dis=k
		while dis>d and j<=length-k:
			dis=k
			for l in range(j,j+k):
				if pattern[l-j]==sequence[l]:
					dis-=1
			j+=1
		if dis>d and pattern in motif_2:
			print(motif_2)
			motif_2.remove(pattern)
print(' '.join(motif_2))