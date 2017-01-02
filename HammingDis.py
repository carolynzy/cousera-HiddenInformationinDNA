#!/usr/bin/python

file1=open('dataset_9_3_1.txt')
file2=open('dataset_9_3_2.txt')
seq1=file1.read()
seq2=file2.read()
dis=0
for i in range(0,len(seq1)):
	if seq1[i]!= seq2[i]:
		dis+=1
print(dis)		
file2.close()
file1.close()