#!/usr/bin/python
#find the position of a certain pattern
file=open('Vibrio_cholerae.txt')
seq=file.read()
pattern=raw_input('Enter your pattern here: ')

i=0
len1=len(seq)
len2=len(pattern)
for c in seq:
	if i+len2<=len(seq)-1:
		pattern2=seq[i:i+len2]
		if pattern2==pattern:
			print(i)
	if i+len2==len(seq):
		pattern2=seq[i:]
		if pattern2==pattern:
			print(i)
	i+=1
file.close()
