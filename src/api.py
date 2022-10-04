import hashlib
import os
from . import read
from threading import Thread
import time
import random

def lrc_play(player,lrc_name,lrc_path,music_path,sleep_time):
	def get_good_name(name):
		name=name.replace('(','\(')
		name=name.replace(')','\)')
		name=name.replace(' ','\ ')
		return name
		
	def find(name,lrc_path,music_path):
		lrc=os.listdir(lrc_path)
		music=os.listdir(music_path)
		ls=[]
		for l in lrc:
			if name in l:
				if name==l.split('.')[0]:
					print('\n\033[1;36m已找到同名的歌词文件!\n\033[0m')
					ls.append(l)
				else:
					print('\n\033[1;36m未找到同名的歌词文件,但找到可能相关的歌词文件!名称为: \033[1;32m'+str(l)+'\033[0m\033[1;36m 将使用该歌词文件!\n\033[0m')
					ls.append(l)
		for m in music:
			mm=m.split('.')[0]
			if name==mm:
				ls.append(m)
		ls.append(len(ls))
		return ls

	def red(name):
		with open(name,'r')as f:
			return list(f.read().split('\n'))

	def get(tm):
		t=tm.split(':')
		if t==['']:
			pass
		else:
			return 60*int(t[0])+float(t[1])

	def begin(name,w):
		data=red(name)
		ls=[]
		for i in data:
			tm=i.replace('[','').split(']')
			ls.append(tm)
		def do(ls,sleep_time):
			for t in ls:
				tm=t[0]
				me=ls.index(t)
				if me==0:
					if read.rainbow:
						i=random.randint(30,37)
						z=random.randint(40,47)
						print('\033[1;'+str(i)+';'+str(z)+'m'+t[1]+'\033[0m')
					else:
						if read.pure_color!=False:
							print('\033[1;'+read.pure_color+t[1]+'\033[0m')
						else:
							print(t[1])
				else:
					now=ls[me][0]
					pre=ls[me-1][0]
					if now=='':
						pass
					else:
						time.sleep(get(now)-get(pre)-sleep_time)
						if read.rainbow:
							i=random.randint(30,37)
							z=random.randint(40,47)
							print('\033[1;'+str(i)+';'+str(z)+'m'+t[1]+'\033[0m')
						else:
							if read.pure_color!=False:
								print('\033[1;'+read.pure_color+t[1]+'\033[0m')
							else:
								print(t[1])
		if '00:00.00' in ls[0][0]:
			ls=ls
		else:
			ls.insert(0,['00:00.000','\n不规范的歌词文件,已自动修复!'])
		do(ls,sleep_time)

	def pla(player,file):
		os.system(player+' '+file)

	result=find(lrc_name,lrc_path,music_path)
	if result[-1]==0:
		return False
	if result[-1]==1:
		music_name=result[0]
		print('\n\033[1;36m没有找到歌词!\n\033[0m')
		pla(player,music_path+get_good_name(music_name))
	if result[-1]==2:
		music_name=result[1]
		lrc_name=result[0]
		t1=Thread(target=begin,args=(lrc_path+lrc_name,''))
		t2=Thread(target=pla,args=(player,music_path+get_good_name(music_name)))
		t1.daemon = True
		t2.daemon = True
		t1.start()
		t2.start()
		t2.join()
		if t2.is_alive()!=True:
			if t1.is_alive():
				try:
					t1._stop()
				except:
					print('\n\033[1;36m由于不规范的歌词或手动中断了歌曲,已中途退出!\n\033[0m')
			else:
				pass

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
		for name in os.listdir(read.music_dir):
			n=name.split('.')[0].split('/')[-1]
			if read.rainbow:
				i=random.randint(30,37)
				z=random.randint(40,47)
				print('\033[1;'+str(i)+';'+str(z)+'m\n本首歌是:\n\n'+n+'\033[0m')
			else:
				if read.pure_color!=False:
					print('\033[1;'+read.pure_color+'\n本首歌是:\n\n'+n+'\033[0m')
				else:
					print('\n本首歌是:\n\n'+n)
			lrc_play(act,n,read.lrc_path,read.music_dir,read.sleep_time)
	else:
		for name in thing:
			n=name.split('.')
			if read.rainbow:
				i=random.randint(30,37)
				z=random.randint(40,47)
				print('\033[1;'+str(i)+';'+str(z)+'m\n本首歌是:\n\n'+n[0]+'\033[0m')
			else:
				if read.pure_color!=False:
					print('\033[1;'+read.pure_color+'\n本首歌是:\n\n'+n[0]+'\033[0m')
				else:
					print('\n本首歌是:\n\n'+n[0])
			lrc_play(act,n[0],read.lrc_path,read.music_dir,read.sleep_time)

##写入hash到文件
def write_into(ipt,list_name):
	hash_list=make_list(ipt)
	with open(read.list_dir+list_name,'w')as f:
		f.write('\n'.join(hash_list)+'\n')

##通过hash播放歌曲
def play_hash(hsh):
	songs_list=dict(zip(list(get_dirhash().values()),list(get_dirhash().keys())))
	name=songs_list[hsh]
	n=name.split('.')
	if read.rainbow:
		i=random.randint(30,37)
		z=random.randint(40,47)
		print('\033[1;'+str(i)+';'+str(z)+'m\n本首歌是:\n\n'+n[0]+'\033[0m')
	else:
		if read.pure_color!=False:
			print('\033[1;'+read.pure_color+'\n本首歌是:\n\n'+n[0]+'\033[0m')
		else:
			print('\n本首歌是:\n\n'+n[0])
	lrc_play(read.player_core,n[0],read.lrc_path,read.music_dir,read.sleep_time)

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
def get_b(ipt,hsh,path):
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
	os.system('clear')
	show_ls(nms)