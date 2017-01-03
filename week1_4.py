#!/usr/bin/python
#find the position of a certain pattern
file=open('Vibrio_cholerae.txt')
seq=file.read()
pattern=input('Enter your pattern here: ')

i=0
len1=len(seq)
len2=len(pattern)
i=0
for c in seq[0:len1-len2+1]:
	pattern2=seq[i:i+len2]
	if pattern2==pattern:
		print(i)
	i+=1
file.close()
