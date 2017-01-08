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
import itertools
import sys
input = sys.stdin.read()
tokens = input.split()
sequence=tokens[0]
k=int(tokens[1])
d=int(tokens[2])


#find all the patterns in the sequence
pattern_all=[]
unique=set()
length=len(sequence)
for i in range(0,length-k+1):
	pattern=sequence[i:i+k]
	pattern_all.append(pattern)
for pattern in pattern_all:
	unique.add(pattern)
	
	
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



# find d-neighbor of k-mers in the sequence
kmers=array.keys()
neighbor=set()
for pattern in unique:
    for kmer in kmers:
        dis=0
        for i in range(0,k):
            if pattern[i]!= kmer[i]:
                dis+=1
        if dis <=d:
            neighbor.add(kmer)


# find frequence of d-neighbors in sequence
count_all={}
for match_d in neighbor:
    count=0
    for item in pattern_all:
        dis=0
        for i in range(0,k):
            if match_d[i]!= item[i]:
                dis+=1
        if dis<=d:
            count+=1
    count_all[match_d]=count
if count_all:
	count_max=max(count_all.values())
else:
	count_max='NULL'
pattern_max=[]
for match_d in neighbor:
    if count_all[match_d]==count_max:
        pattern_max+=[match_d]
print(' '.join(pattern_max))

		
		
		
		
		
		
		
		
		
		
		
	
		
	
