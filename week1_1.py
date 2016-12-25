#!/usr/bin/python

import os

initial=os.environ['initial']
pattern=os.environ['pattern']



file=open('dataset_2_7.txt')
text=file.read()
print(text)
range=[pos for pos, char in enumerate(text) if char == initial]
len1=len(pattern)
len2=len(text)-1
count=0
for i in range:
	if i<len2-len1:
		if text[i:i+len1]==pattern:
			count+=1
	elif i==len2-len1:
		if text[i:]==pattern:
			count+=1
print(str(count)+str(range))
file.close()
exit

