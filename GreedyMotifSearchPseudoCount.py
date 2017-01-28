#!/usr/bin/python

import sys
input= sys.stdin.read()
tokens=input.split()
k=int(tokens[0])
t=int(tokens[1])

kmer_list=[]
string=tokens[2]
length=len(string)
for i in range(0,length-k+1):   ##需要在末尾+1，才能得到最后一个kmer
	kmer_list.append(string[i:i+k])	
	
##计算最开始的集合及得分
bestmotif_ori=[]  ##需要有个保持不变的
count=[]
for i in range(0,k):
	count+=[[0,0,0,0]]   ##不能用简单乘法，各个list只是同一个list的映射，会一起改变
for i in range(2,t+2):
	string=tokens[i]
	motif=string[0:k]
	bestmotif_ori.append(motif)
	for c in range(0,k):
		if motif[c]=='A':
			count[c][0]+=1
		if motif[c]=='C':
			count[c][1]+=1
		if motif[c]=='G':
			count[c][2]+=1
		if motif[c]=='T':
			count[c][3]+=1
score_best=k*t
for i in count:
	score_best-=max(i)

##计算每个最优组合及其得分，并与最开始的组合进行比较
best_final=list(bestmotif_ori)	##需要有个可变的，但又保持比最新的较老的一个版本的
for kmer in kmer_list:
	profile_a=[0]*k  ##如果是单个元素，不是list，则可以
	profile_c=[0]*k
	profile_g=[0]*k
	profile_t=[0]*k
	count_a=[1]*k
	count_c=[1]*k
	count_g=[1]*k
	count_t=[1]*k
	bestmotif=list(bestmotif_ori)
	bestmotif[0]=kmer
	for i in range(0,k):
		if kmer[i] == 'A':
			count_a[i]+=1
		if kmer[i] == 'C':
			count_c[i]+=1
		if kmer[i] == 'G':
			count_g[i]+=1
		if kmer[i] == 'T':
			count_t[i]+=1
	for i in range(0,k):
		profile_a[i]=count_a[i]/(k+1)
		profile_c[i]=count_c[i]/(k+1)
		profile_g[i]=count_g[i]/(k+1)
		profile_t[i]=count_t[i]/(k+1)
	dict={'A':profile_a,'C':profile_c,'G':profile_g,'T':profile_t}  ##得到profile
	for i in range(3,t+2):
		string=tokens[i]
		pro=0
		for j in range(0,length-k+1):
			sub_string=string[j:j+k]
			Pro_j=1
			for c in range(0,k):
				letter=sub_string[c]
				p=float(dict[letter][c])
				Pro_j*=p
			if Pro_j>pro:
				pro=Pro_j
				bestmotif[i-2]=sub_string  ##得到最大可能motif
		motif_i=bestmotif[i-2]
		for j in range(0,k):
			if motif_i[j] == 'A':
				count_a[j]+=1
			if motif_i[j] == 'C':
				count_c[j]+=1
			if motif_i[j] == 'G':
				count_g[j]+=1
			if motif_i[j] == 'T':
				count_t[j]+=1
		for j in range(0,k):
			profile_a[j]=count_a[j]/(i-1+k)
			profile_c[j]=count_c[j]/(i-1+k)
			profile_g[j]=count_g[j]/(i-1+k)
			profile_t[j]=count_t[j]/(i-1+k)
		dict={'A':profile_a,'C':profile_c,'G':profile_g,'T':profile_t} ##计算更新最大可能motif后的profile
	count=[]
	for i in range(0,k):
		count+=[[0,0,0,0]]
	for motif in bestmotif:
		for i in range(0,k):
			if motif[i]=='A':
				count[i][0]+=1
			if motif[i]=='C':
				count[i][1]+=1
			if motif[i]=='G':
				count[i][2]+=1
			if motif[i]=='T':
				count[i][3]+=1		
	score_motif=k*t
	for i in count:
		score_motif-=max(i)   ##计算最优组合的得分
	if 	score_motif<score_best:
		score_best=score_motif
		bestmotif_final=list(bestmotif)  ##与最开始的集合进行比较，更新最最优组合及其得分

for item in bestmotif_final:
	print(item)