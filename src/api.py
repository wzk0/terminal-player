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

##美化输出序号和列表内容
def show_ls(names):
	lenth=len(names)-1
	zero=0
	while zero<=lenth:
		print('\033[1;35;44m'+str(zero)+'.\033[0m | \033[0m\033[1;36m'+str(names[zero])+'\033[0m')
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
def play(thing,act):
	if thing=='a':
		os.system(act+read.music_dir+'*')
	else:
		for name in thing:
			name=read.get_good_name(name)
			os.system(act+read.music_dir+name)

##写入hash到文件
def write_into(ipt,list_name):
	hash_list=make_list(ipt)
	with open(read.list_dir+list_name,'w')as f:
		f.write('\n'.join(hash_list)+'\n')

##通过hash播放歌曲
def play_hash(hsh):
	songs_list=dict(zip(list(get_dirhash().values()),list(get_dirhash().keys())))
	name=songs_list[hsh]
	name=read.get_good_name(name)
	os.system('play '+read.music_dir+name)

##通过输入序号返回歌单的hash列表
def back_hash(ipt):
	ls=os.listdir(read.list_dir)
	lenth=len(ls)
	list_list=dict(zip(range(0,lenth),ls))
	with open(read.list_dir+list_list[int(ipt)])as f:
		f=f.read()
	f=f.split('\n')
	return f[:-1]

##根据输入序号获取歌单路径
def get_path(ipt):
	ls=os.listdir(read.list_dir)
	lenth=len(ls)
	list_list=dict(zip(range(0,lenth),ls))
	return read.list_dir+list_list[int(ipt)]

##删除歌单文件
def rm_ls(ipt):
	list_list=get_path(ipt)
	os.system('rm -rf '+list_list)

##收藏音乐
def like(ipt):
	hash_list=make_list(ipt)
	with open(read.list_dir+'我的收藏','a')as f:
		f.write('\n'.join(hash_list)+'\n')

##删除所有
def dl_all_file():
	os.system('rm -rf '+read.list_dir+'*')

##清空所有
def clear_all():
	ls=os.listdir(read.list_dir)
	os.system('rm -rf '+read.list_dir+'*')
	for l in ls:
		os.system('touch '+read.list_dir+l)

##获取补集
def get_b(ipt,hsh):
	if ipt=='a':
		os.system('rm -rf '+path)
		os.system('touch '+path)
	else:
		ls=ipt.split(' ')
		wd=[]
		for i in ls:
			wd.append(hsh[int(i)])
		b=list(set(hsh)-(set(wd)))
		return b

##删除歌单内音乐
def rm_ls_inside(b,path):
	os.system('rm -rf '+path)
	with open(path,'w')as f:
		f.write('\n'.join(b)+'\n')

##新旧歌单作比较
def compare(b):
	nms=back_name(b)
	print('\n')
	show_ls(nms)