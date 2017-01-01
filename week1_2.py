#!/usr/bin/python

file=open('dataset_2_10.txt')
seq=file.read()
k=int(input('Input the k here: '))

i=0
list=[]
unique=set()
output={}
value=set()
for c in seq:
	if i+k<=len(seq)-1:
		pattern=seq[i:i+k]
		list.append(pattern)
	if i+k==len(seq):
		pattern=seq[i:]
		list.append(pattern)
	i+=1
##print(list)
for pattern in list:
	unique.add(pattern)
##print(unique)
for item in unique:
	count=list.count(item)
	output[item]=count
	value.add(count)
max=max(value)
for item in output:
	if output[item]==max:
		print(item)
file.close()
