#!/usr/bin/python

import sys
input = sys.stdin.read()
tokens=input.split()
#input=open('test.txt')
#tokens = input.read().split()
pattern=tokens[0]

k=len(pattern)
dis=0
t=len(tokens)
for i in range(1,t):
	string=tokens[i]
	length=len(string)
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
print(dis)