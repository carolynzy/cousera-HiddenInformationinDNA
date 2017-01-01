#!/usr/bin/python
# create frequence array for K-mers and return the index for a pattern


pattern=raw_input('Enter pattern here: ')
K=len(pattern)
print(K)
dict={'A':0, 'C':1, 'G':2, 'T':3}
index=0
for c in pattern:
	print(c)
	index1=4**(K-1)*dict[c]
	print(index1)
	K-=1
	index+=index1
	print(index)
print(index)