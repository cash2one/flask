

import math
def cal_dcg(scoremat):
	dcg = scoremat[0]
	d = 0
	for i in scoremat:
		d+=1
		if d==1:continue
		
		dcg += float(i)/math.log(d,2)

	return dcg
if __name__=='__main__':
	s1 = [1,1,0,1,1]
	s2 = [1,1,1,1,0]
	print cal_dcg(s1)/5,cal_dcg(s2)/5
	print cal_dcg(s1)/cal_dcg(s2)
