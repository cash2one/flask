#!/usr/bin/python
#-*-coding:utf-8-*-

import re
import anydbm
import sys
import glo

def checkmat(mat):
	c = 0
	for i in mat:
		for j in i:
			c += 1
	return c



def qqsearch(name):
	outmat = []
	if not glo.name2uri.has_key(name):
		return outmat
	uris = re.compile(r'\|').split(glo.name2uri[name])
	prhash = {}
	for i in uris:
		try:
			p = float(glo.uri2hot[i])
		except:
			p = 0
		prhash[i] = p
	keys = sorted(prhash.iteritems(),key=lambda prhash:prhash[1],reverse=True)	
	l = 0
	tempsingerhash = {}
	for i in keys:
		tempmat = []	
		if re.search('artist',i[0]):
			try:
				songs = re.compile(r'\|').split(glo.artist2song[i[0]])
				temphash = {}
				for k in songs:
					try:
						p = glo.uri2hot[k]
					except:
						p = 0
					temphash[k] = float(p)
				ikeys = sorted(temphash.iteritems(),key=lambda temphash:temphash[1],reverse=True)
				count = 0
				tempsonghash = {}
				for m in ikeys:
					
					if count >=10 :break
					try:
						
						songname = glo.uri2name[m[0]]
						if tempsonghash.has_key(songname):continue
						tempsonghash[songname] = ''
					except:
						songname = ''
					try:
						album =  glo.uri2name[glo.song2album[m[0]]]
					except:
						album = ''
					#print 'song:',songname,'	album:',album,'	score:',m[1]
					l += 1
					count += 1
					outstr = 'song:'+songname+'	artist:'+name+'	album:'+album
					tempmat.append(outstr.decode('utf-8').encode('gbk'))
			except:
				continue
		if re.search('song',i[0]):
			
			try:
				singer = glo.uri2name[glo.song2artist[i[0]]]
				if tempsingerhash.has_key(singer):continue
				tempsingerhash[singer] = ''
			except:
				singer = ''
			try:
				album = glo.uri2name[glo.song2album[i[0]]]
			except:
				album = ''	
			l+=1
			outstr ='song:'+name+'	artist:'+singer+'	album:'+album
			tempmat.append(outstr.decode('utf-8').encode('gbk'))
		outmat.append(tempmat)
		if checkmat(outmat) >=10:break
	return outmat	



def search(name):
	outmat = []
	if not glo.name2uri.has_key(name):
		return outmat
	uris = re.compile(r'\|').split(glo.name2uri[name])
	prhash = {}
	for i in uris:
		try:
			p = float(glo.PR[i])
		except:
			p = 0
		prhash[i] = p
	keys = sorted(prhash.iteritems(),key=lambda prhash:prhash[1],reverse=True)
	l = 0
	tempsingerhash = {}
	for i in keys:
		tempmat = []	
		if re.search('artist',i[0]):
			try:
				songs = re.compile(r'\|').split(glo.artist2song[i[0]])
				temphash = {}
				for k in songs:
					try:
						p = glo.PR[k]
					except:
						p = 0
					temphash[k] = float(p)
				ikeys = sorted(temphash.iteritems(),key=lambda temphash:temphash[1],reverse=True)
				count = 0
				tempsonghash = {}
				for m in ikeys:
					
					if count >=10 :break
					try:
						
						songname = glo.uri2name[m[0]]
						if tempsonghash.has_key(songname):continue
						tempsonghash[songname] = ''
					except:
						songname = ''
					try:
						album =  glo.uri2name[glo.song2album[m[0]]]
					except:
						album = ''
					#print 'song:',songname,'	album:',album,'	score:',m[1]
					l += 1
					count += 1
					outstr = 'song:'+songname+'	artist:'+name+'	album:'+album
					tempmat.append(outstr.decode('utf-8').encode('gbk'))
			except:
				continue
		if re.search('song',i[0]):
			
			try:
				singer = glo.uri2name[glo.song2artist[i[0]]]
				if tempsingerhash.has_key(singer):continue
				tempsingerhash[singer] = ''
			except:
				singer = ''
			try:
				album = glo.uri2name[glo.song2album[i[0]]]
			except:
				album = ''	
			l+=1
			outstr ='song:'+name+'	artist:'+singer+'	album:'+album
			tempmat.append(outstr.decode('utf-8').encode('gbk'))
		outmat.append(tempmat)
		if checkmat(outmat) >=10:break
	return outmat
if __name__=='__main__':
	outmat = qqsearch('刘德华')		
	for mat in outmat:
		for j in mat:
			print j