#!/usr/bin/python

pattern=raw_input('Enter your pattern here: ')
hd=int(raw_input('Enter d here: '))
#seq=raw_input('Enter your seq here: ')
file=open('test.txt')
seq=file.read()


len1=len(seq)
len2=len(pattern)
count=0
for i in range(0,len(seq)):
	if i+len2<=len(seq)-1:
		pattern2=seq[i:i+len2]
		dis=0
		for j in range(0,len(pattern)):
			if pattern2[j]!= pattern[j]:
				dis+=1
		if dis<=hd:
			print(i)
			count+=1
	if i+len2==len(seq):
		pattern2=seq[i:]
		dis=0
		for j in range(0,len(pattern)):
			if pattern2[j]!= pattern[j]:
				dis+=1
		if dis<=hd:
			print(i)
			count+=1
	i+=1
print(count)
file.close()