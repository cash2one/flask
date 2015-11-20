#-*-coding:utf-8-*-
from app import app
from flask import render_template,redirect,request,url_for
import anydbm
import time
import math
import checkAns
import parseBaidu
import glo
@app.route('/')
@app.route('/index')
def index():

	return render_template("page.html")


@app.route('/index',methods=['POST'])
def get_input_name():
	global input_name
	input_name=request.form["input_name"]
	print input_name
	#if glo.db.has_key(input_name.encode('utf-8')):
	#	query = '请换一个,这个测过啦！！！'
	#	return render_template("page.html",query=input_name)
	#else:
	#	
	return redirect('/result')


@app.route('/result')
def show_result():
	global out,out2
	query = input_name.encode('gbk')
	input_tag=input_name.encode('utf-8')
	out = []
	out2 = []
	out3 = []

	c = 0
	c2 = 0
	c3 = 0
	m1 = checkAns.search(input_tag)
	for i in m1:
		for j in i:
			c += 1
			out.append(j)

	m2 = parseBaidu.main_process(input_tag)
	for i in m2:
		c2+= 1
		out2.append(i)



	print len(out2)
	if len(out) == 0:out.append(['not found'])
	if len(out2) == 0: out2.append('not found')
	'''
	m3 = checkAns.qqsearch(input_tag)
	for i in m3:
		for j in i:
			c3+=1
			out3.append(j)	


	if len(out3) == 0:out3.append(['not found'])
	return render_template("result1.html",mat=out,mat2=out2,mat3=out3,query=query)
	'''
	return render_template("result.html",mat=out,mat2=out2,query=query)


@app.route('/result',methods=['POST'])
def get_dcg():
	glo.db[input_name.encode('utf-8')] = ''
	outfile_pr = open('record_pr.txt','a')
	outfile_baidu = open('record_baidu.txt','a')
	outfile_pr.write(input_name+'\n')
	outfile_baidu.write(input_name+'\n')
	for i in out:
		cg = request.form[i]
		outstr = str(cg)+'#'+i
		outfile_pr.write(outstr+'\n')
	outfile_pr.write('\n\n\n\n')
	for j in out2:
		cg = request.form[j]
		outstr = str(cg)+'#'+j
		outfile_baidu.write(outstr+'\n')
	outfile_baidu.write('\n\n\n\n')
	query = input_name+('	提交成功！！！').decode('utf-8').encode('gbk')

	return render_template("page.html",query=query)
	