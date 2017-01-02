#!/usr/bin/python


file=open('dataset_7_6.txt')
seq=file.read()

list=[0]
value=0
for c in seq:
	if c=='C':
		value-=1
	elif c=='G':
		value+=1
	list+=[value]

min=min(list)
min_index=[i for i, x in enumerate(list) if x==min]
print(min_index)
file.close()