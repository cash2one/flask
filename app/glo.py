import anydbm
global PR,name2uri,uri2name,song2artist,song2album,artist2song,db
PR=anydbm.open('E:\\sam_work\\2014\\pagerank\\qqmusic\\db0\\uriToPR.db','r')
name2uri=anydbm.open('E:\\sam_work\\2014\\pagerank\\qqmusic\\db0\\NameToUri.db','r')
uri2name=anydbm.open('E:\\sam_work\\2014\\pagerank\\qqmusic\\db0\\uriToName.db','r')
song2artist = anydbm.open('E:\\sam_work\\2014\\pagerank\\qqmusic\\db0\\song2artist.db','r')
song2album = anydbm.open('E:\\sam_work\\2014\\pagerank\\qqmusic\\db0\\song2album.db','r')
artist2song = anydbm.open('E:\\sam_work\\2014\\pagerank\\qqmusic\\db0\\artist2song.db','r')
uri2hot = anydbm.open('E:\\sam_work\\2014\\pagerank\\qqmusic\\db0\\UriToHot.db','r')
db = anydbm.open('query.db','c')