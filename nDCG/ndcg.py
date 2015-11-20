#!/usr/bin/python
#-*-coding:utf-8-*-
import re
import string
import anydbm
import math

data = open('record_baidu.txt','r')
mat_baidu = []
tempmat = []
for i in data:
	i = i.strip('\n')
	if len(i) == 0:continue
	if not re.search(r'\d#',i):
		if len(tempmat) > 8:
			mat_baidu.append(tempmat)
		tempmat = []
		tempmat.append(i)
		continue
	tempmat.append(i)
data.close()


hash_baidu = {}
for mat in mat_baidu:
	query = mat[0]
	c = 0
	tempmat = []
	for i in mat:
		c += 1
		if c == 1:continue
		
		mat2 = re.compile('#').split(i)
		score = float(mat2[0])
		tempmat.append(score)
	hash_baidu[query] = tempmat







data = open('record_migu.txt','r')
mat_migu = []
tempmat = []
for i in data:
	i = i.strip('\n')
	if len(i) == 0:continue
	if not re.search(r'\d#',i):
		if len(tempmat) > 4:
			mat_migu.append(tempmat)
		tempmat = []
		tempmat.append(i)
		continue
	tempmat.append(i)
data.close()

hash_migu = {}
for mat in mat_migu:
	query = mat[0]
	c = 0
	tempmat = []
	for i in mat:
		c += 1
		if c == 1:continue
		
		mat2 = re.compile('#').split(i)
		score = float(mat2[0])
		tempmat.append(score)
	hash_migu[query] = tempmat




data = open('record_pr.txt','r')
mat_pr = []
tempmat = []
for i in data:
	i = i.strip('\n')
	if len(i) == 0:continue
	if not re.search(r'\d#',i):
		if len(tempmat) > 8:
			mat_pr.append(tempmat)
		tempmat = []
		tempmat.append(i)
		continue
	tempmat.append(i)
data.close()



hash_pr = {}
for mat in mat_pr:
	query = mat[0]
	c = 0
	tempmat = []
	for i in mat:
		c += 1
		if c == 1:continue
		
		mat2 = re.compile('#').split(i)
		score = float(mat2[0])
		
		tempmat.append(score)
	hash_pr[query] = tempmat



def cal_dcg(scoremat):
	dcg = scoremat[0]
	d = 0
	for i in scoremat:
		d+=1
		if d==1:continue

		dcg += i/math.log(d,2)
	return dcg
outhash = {}
baidu_ave = 0
pr_ave = 0
mg_ave = 0
mat1 = []
mat2 = []
for query in hash_pr:

	try:
		mat_b = hash_baidu[query]
		mat_p = hash_pr[query]
		#mat_m = hash_migu[query]
	except:
		continue

	#mat_b_ideal = sorted(mat_b,reverse=True)
	#mat_p_ideal = sorted(mat_p,reverse=True)

	#ndcg_b = cal_dcg(mat_b)/cal_dcg(mat_b_ideal)
	
	ndcg_b = cal_dcg(mat_b)
	mat1.append(ndcg_b)
	baidu_ave += ndcg_b
	

	#ndcg_p = cal_dcg(mat_p)/cal_dcg(mat_p_ideal)
	ndcg_p = cal_dcg(mat_p)
	mat2.append(ndcg_p)
	pr_ave += ndcg_p
	

	#ndcg_m = cal_dcg(mat_m)
	#mg_ave += ndcg_m


	outhash[query] = query+'	'+str(ndcg_b)+'	'+str(ndcg_p)

for i in outhash:
	print outhash[i]


print 'baidu average:',baidu_ave/len(outhash)
print 'baidu max,min:',max(mat1),min(mat1)
print 'pagerank max,min:',max(mat2),min(mat2)
print 'pagerank average:',pr_ave/len(outhash)
#print 'migu average:',mg_ave/len(outhash)

