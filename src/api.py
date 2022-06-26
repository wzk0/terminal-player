import hashlib
import os
from . import read

##获取文件hash
def get_hash(path):
	h=hashlib.sha1()
	zero=0
	with open(path,'rb')as f:
		while zero!=b'':
			zero=f.read(1024)
			h.update(zero)
	return h.hexdigest()

##获取hash与文件名对照的字典
def get_dirhash():
	songs=os.listdir(read.music_dir)
	songs_name=[]
	songs_hash=[]
	for song in songs:
		songs_hash.append(get_hash(read.music_dir+song))
		songs_name.append(song)
	songs_list=dict(zip(songs_name,songs_hash))
	return songs_list

##美化输出序号和对照的歌名
def show_list():
	songs_name=list(get_dirhash().keys())
	lenth=len(songs_name)-1
	zero=0
	while zero<=lenth:
		print(str(zero)+'. | '+str(songs_name[zero]))
		zero+=1

##通过输入序号生成歌曲的hash列表
def make_list(ipt):
	ids=ipt.split(' ')
	songs_name=get_dirhash()
	lenth=len(songs_name)
	ids_list=dict(zip(range(0,lenth),songs_name))
	name_list=[]
	for i in ids:
		name=ids_list[int(i)]
		name_list.append(name)
	hash_list=[]
	for name in name_list:
		hsh=songs_name[name]
		hash_list.append(hsh)
	return hash_list

##通过hash列表返回歌曲名
def back_name(hash_list):
	songs_list=dict(zip(list(get_dirhash().values()),list(get_dirhash().keys())))
	name_list=[]
	for hsh in hash_list:
		name_list.append(songs_list[hsh])
	return name_list

##通过列表播放歌曲
def play(thing):
	for name in thing:
		name=name.replace('(','\(')
		name=name.replace(')','\)')
		name=name.replace(' ','\ ')
		os.system('play '+read.music_dir+name)

##写入hash到文件
def write_into(ipt,list_name):
	hash_list=make_list(ipt)
	with open(read.list_dir+list_name,'w')as f:
		f.write('\n'.join(hash_list)+'\n')

##通过hash播放歌曲
def play_hash(hsh):
	songs_list=dict(zip(list(get_dirhash().values()),list(get_dirhash().keys())))
	name=songs_list[hsh]
	name=name.replace('(','\(')
	name=name.replace(')','\)')
	name=name.replace(' ','\ ')
	os.system('play '+read.music_dir+name)

##美化输出序号和对照的歌单
def show_songsls():
	ls=os.listdir(read.list_dir)
	lenth=len(ls)-1
	zero=0
	while zero<=lenth:
		print(str(zero)+'. | '+str(ls[zero]))
		zero+=1

##通过输入序号返回歌单的hash列表
def back_hash(ipt):
	ls=os.listdir(read.list_dir)
	lenth=len(ls)
	list_list=dict(zip(range(0,lenth),ls))
	with open(read.list_dir+list_list[int(ipt)])as f:
		f=f.read()
	f=f.split('\n')
	return f[:-1]

def like(ipt):
	hash_list=make_list(ipt)
	with open(read.list_dir+'我的收藏','a')as f:
		f.write('\n'.join(hash_list)+'\n')