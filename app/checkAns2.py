#!/usr/bin/python
#-*-coding:utf-8-*-

import re
import anydbm
import sys

def main_song(name):
	#name=name.strip('\n|\r').encode('utf-8')
	PR=anydbm.open('E:\\sam_work\\pagerank\\qqmusic\\db\\uriToPR.db','r')
	name2uri=anydbm.open('E:\\sam_work\\pagerank\\qqmusic\\db\\NameToUri.db','r')
	uri2name=anydbm.open('E:\\sam_work\\pagerank\\qqmusic\\db\\uriToName.db','r')
	song2artist = anydbm.open('E:\\sam_work\\pagerank\\qqmusic\\db\\song2artist.db','r')
	song2album = anydbm.open('E:\\sam_work\\pagerank\\qqmusic\\db\\song2album.db','r')
	outmat = []
	if not name2uri.has_key(name):
		return outmat
	uris = re.compile(r'\|').split(name2uri[name])
	myhash = {}
	for i in uris:
		if re.search('song',i):
			try:
				p = PR[i]
			except:
				p = 0
			myhash[i] = p
	keys = sorted(myhash.iteritems(),key=lambda myhash:myhash[1],reverse=True)
	#print 'search query:',name

	for i in keys:
		try:
			singer = uri2name[song2artist[i[0]]]
		except:
			singer = ''
		try:
			album = uri2name[song2album[i[0]]]
		except:
			album = ''
		#print 'singer:',singer,'	album:',album,'	score:',i[1]
		outstr = 'singer:'+singer+'	album:'+album+'	score:'+i[1]
		outmat.append(outstr)
	return outmat


def main_artist(name):
	db = anydbm.open('E:\\sam_work\\pagerank\\qqmusic\\db\\artist2song.db','r')
	PR=anydbm.open('E:\\sam_work\\pagerank\\qqmusic\\db\\uriToPR.db','r')
	name2uri=anydbm.open('E:\\sam_work\\pagerank\\qqmusic\\db\\NameToUri.db','r')
	uri2name=anydbm.open('E:\\sam_work\\pagerank\\qqmusic\\db\\uriToName.db','r')
	song2album = anydbm.open('E:\\sam_work\\pagerank\\qqmusic\\db\\song2album.db','r')
	outmat = []
	print 'search singer:',name
	try:
		uris = re.compile(r'\|').split(name2uri[name])
		for j in uris:
			if re.search('artist',j):
				try:
					songs = re.compile(r'\|').split(db[j])
					temphash = {}
					for k in songs:
						try:
							p = PR[k]
						except:
							p = 0
						temphash[k] = float(p)
					keys = sorted(temphash.iteritems(),key=lambda temphash:temphash[1],reverse=True)
					count = 0
					outmat.append('singer:'+name)
				
					for m in keys:
						count += 1
						if count >10 :break
						try:
							songname = uri2name[m[0]]
						except:
							songname = ''
						try:
							album = uri2name[song2album[m[0]]]
						except:
							album = ''
						#print 'song:',songname,'	album:',album,'	score:',m[1]
						outstr = 'song:'+songname+'	album:'+album+'	score:'+m[1]
						outmat.append(outstr)
				except:
					continue
		return outmat
	except:
		




def pre():
	data = open('..\\data\\artist2song.txt','r')
	db = anydbm.open('..\\db\\song2artist.db','n')
	db_1 = anydbm.open('..\\db\\artist2song.db','n')
	for i in data:
		mat = re.compile('	').split(i.strip('\n'))
		db['song'+str(mat[1])] = 'artist'+str(mat[0])
		if db_1.has_key('artist'+str(mat[0])):
			db_1['artist'+str(mat[0])] += '|song'+str(mat[1])
		else:
			db_1['artist'+str(mat[0])] = 'song'+str(mat[1])
	data.close()
	data = open('..\\data\\album2song.txt','r')
	db2 = anydbm.open('..\\db\\song2album.db','n')
	db_2 = anydbm.open('..\\db\\album2song.db','n')
	for i in data:
		mat = re.compile('	').split(i.strip('\n'))
		db2['song'+str(mat[1])] = 'album'+str(mat[0])
		if db_2.has_key('album'+str(mat[0])):
			db_2['album'+str(mat[0])] += '|song'+str(mat[1])
		else:
			db_2['album'+str(mat[0])] = 'song'+str(mat[1])
	data.close()

if __name__=='__main__':
	main_song('老男孩')
	#main_artist('筷子兄弟')