#!/usr/bin/python
#-*-coding:utf-8-*-

import re
import anydbm
import urllib2
import urllib

def main_process(songname):


	url='http://music.baidu.com/search/song?key=%s&s=1'%songname
	f=urllib.urlopen(url)
	data=re.sub('\n|\r','',f.read())
	f.close()
	mat=re.compile(r'<span class=\"index-num index-hook\"(.*?)<input type=\"checkbox\"   class=\"checkbox-item-hook\"').findall(data)
	

	outmat=[]
	c = 0
	for i in mat:
		song=''
		singer=''
		album=''
		songmat=re.compile(r'<span class=\"song-title\".*?title=\"(.*?)\">').findall(i)
		if len(songmat)>0:
			if re.search('审批',songmat[0]):
				song_temp=re.compile('审批').split(songmat[0])
				song=song_temp[0]
			else:
				song=songmat[0]
		singermat=re.compile(r'<span class=\"singer.*?title=\"(.*?)\">').findall(i)
		if len(singermat)>0:singer=singermat[0]
		albummat=re.compile(r'<span class=\"album-title\".*?title=\"(.*?)\">.*?<span class="music-icon-hook"').findall(i)
		if len(albummat)>0:
			if not re.search('href',albummat[0]):
				album=albummat[0]
		c += 1
		outstr='song:'+song+'	singer:%s'%singer+'	album:%s'%album
		outmat.append(outstr.decode('utf-8').encode('gbk'))
		if c == 10:break
	return outmat

if __name__=='__main__':
	song='邓丽君'
	out = main_process(song)
	for i in out:
		print i


