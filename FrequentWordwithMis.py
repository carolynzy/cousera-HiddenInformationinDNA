#!/usr/bin/python
import sys

input = sys.stdin.read()
tokens = input.split()
sequence=tokens[0]
k=int(tokens[1])
d=int(tokens[2])


#file=open('test.txt')
#sequence=file.read()
#sequence=input('Sequence: ')
#k, d=input('Enter k, d here: ').split()
#k=int(k)
#d=int(d)

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
            
# create the reverse sequence of each pattern in neighbor
dict={'A':'T', 'T':'A', 'G':'C', 'C':'G'}
pair={}
for pattern in neighbor:
    pattern_r=[]
    for i in range(k-1,-1,-1):
        b=pattern[i]
        c=dict[b]
        pattern_r.append(c)
    pair[pattern]=''.join(pattern_r)
    pair[''.join(pattern_r)]=pattern
neighbor_r=set(pair.values())
for i in neighbor_r:
	neighbor.add(i)

# find the frequence of each pattern in neighbor + frequence of reverse pattern
count_all={}
for pattern in neighbor:
	count=0
	count_r=0
	for item in pattern_all:
		dis=0
		for i in range(0,k):
			if pattern[i]!= item[i]:
				dis+=1
		if dis<=d:
			count+=1
	for item in pattern_all:
		dis=0
		for i in range(0,k):
			if pair[pattern][i]!= item[i]:
				dis+=1
		if dis<=d:
			count_r+=1
	count_all[pattern]=count+count_r
if not count_all:
	count_max='none'
else:
	count_max=max(count_all.values())
pattern_max=[]
for pattern in neighbor:
	if count_all[pattern]==count_max:
		pattern_max.append(pattern)	
print(' '.join(pattern_max))
