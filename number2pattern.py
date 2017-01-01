#!/usr/bin/python


i=int(input('Enter your number here: '))
K=int(input('Enter K here: '))
list=['A']*K
dict={0:'A',1:'C', 2:'G',3:'T'}
count=0
while K-1>=0:
	if i >= 4**(K-1)*3:
		list[count]='T'
		i-=4**(K-1)*3
	elif 4**(K-1)*2<=i<4**(K-1)*3:
		list[count]='G'
		i-=4**(K-1)*2
	elif 4**(K-1)<=i<4**(K-1)*2:
		list[count]='C'
		i-=4**(K-1)
	elif 0<=i<4:
		list[K-1]=dict[i]		
	count+=1
	K-=1
print(''.join(list))
