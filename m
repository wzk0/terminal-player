#!/usr/bin/python3

import os
import json
from colorama import Fore, Back, Style

now_path=os.popen('pwd').read().replace('\n','')
you=os.getlogin()
file_name=['mp3','MP3','flac','FLAC','wav','WAV','m4a','M4A','ogg','OGG','3ga','669','a52','acc','ac3','adt','adts','aif','aiff','amr','aob','ape','awb','caf','dts','it','kar','m4b','m4p','m5p','mid','mka','mlp','mod','mpa','mp1','mp2','mpc','mpga','mus','oga','oma','opus','qcp','ra','rmi','s3m','sid','spx','thd','tta','voc','vqf','w64','wma','wv','xa','xm']

def get_music(ls):
	result=[]
	for l in ls:
		if l.split('.')[-1] not in file_name:
			pass
		else:
			result.append(l)
	return result

def write_json(dic,name):
	if not os.path.exists('/home/'+you+'/.songs_list.json'):
		with open('/home/'+you+'/.songs_list.json','w')as f:
			f.write(json.dumps([dic],ensure_ascii=False))
	else:
		with open('/home/'+you+'/.songs_list.json','r')as f:
			f=json.loads(f.read())
		f.append(dic)
		with open('/home/'+you+'/.songs_list.json','w')as ff:
			ff.write(json.dumps(f,ensure_ascii=False))

def add_json(string,name=''):
	ls=get_music(os.listdir(now_path))
	if not os.path.exists('/home/'+you+'/.songs_list.json'):
		name=input('\n请输入新建歌单名:')
	else:
		if name:
			name=name
		else:
			with open('/home/'+you+'/.songs_list.json','r')as f:
				f=json.loads(f.read())
			os.system('clear')
			name_list=[]
			for l in f:
				name_list.append(l['name'])
			print('已有的歌单名: '+Fore.BLUE+'<%s>'%'>, <'.join(name_list)+Style.RESET_ALL)
			name=input('\n请输入新建歌单名:')
	songs=[]
	for s in string.split(' '):
		songs.append(ls[int(s)])
	dic={}
	dic['name']=name
	dic['path']=now_path
	dic['songs']=songs
	write_json(dic,name)

def show_json(simple=''):
	if simple:
		if not os.path.exists('/home/'+you+'/.songs_list.json'):
			pass
		else:
			with open('/home/'+you+'/.songs_list.json','r')as f:
				f=json.loads(f.read())
			name_list=[]
			for l in f:
				name_list.append(l['name'])
			print('已有的歌单名: '+Fore.BLUE+Style.BRIGHT+'<%s>'%'>, <'.join(name_list)+Style.RESET_ALL)
	else:
		with open('/home/'+you+'/.songs_list.json','r')as f:
			f=json.loads(f.read())
		for l in f:
			print(str(f.index(l))+'. 歌单名称: '+Fore.BLUE+Style.BRIGHT+l['name']+Style.RESET_ALL+'\n歌曲数量: '+Fore.GREEN+Style.BRIGHT+str(len(l['songs']))+Style.RESET_ALL+'\n歌曲路径: '+Fore.CYAN+Style.BRIGHT+l['path']+Style.RESET_ALL+'\n')

def play():
	ls=get_music(os.listdir(now_path))
	for l in ls:
		print(Fore.BLUE+Style.BRIGHT+str(ls.index(l))+Fore.CYAN+'. %s'%''.join(l.split('.')[:-1])+Style.RESET_ALL)
	string=input('\n请输入序号(多个序号间用空格分开):')
	for s in string.split(' '):
		os.system('clear')
		print(Fore.GREEN+Style.BRIGHT+'\033[5m<== NOW PLAYING ==> \n\033[0m'+Style.BRIGHT+Fore.CYAN+'%s\n'%''.join(ls[int(s)].split('.')[:-1])+Style.RESET_ALL)
		os.system("cvlc --play-and-exit '%s'"%ls[int(s)])
	show_json(simple=True)
	choose=input('\n若要将刚播放的音乐添加至新歌单, 请直接输入新歌单名称(否则请回车):')
	if choose !='':
		add_json(string,name=choose)

def add():
	ls=get_music(os.listdir(now_path))
	for l in ls:
		print(Fore.BLUE+Style.BRIGHT+str(ls.index(l))+Fore.CYAN+'. %s'%''.join(l.split('.')[:-1])+Style.RESET_ALL)
	string=input('\n请输入序号(多个序号间用空格分开):')
	add_json(string)

def play_list():
	show_json()
	with open('/home/'+you+'/.songs_list.json','r')as f:
		f=json.loads(f.read())
	string=input('请输入歌单序号(多个序号间用空格分开):')
	for s in string.split(' '):
		l=f[int(s)]
		for song in l['songs']:
			os.system('clear')
			print(Fore.GREEN+Style.BRIGHT+'\033[5m<== NOW PLAYING ==> \n\033[0m'+Style.BRIGHT+Fore.CYAN+'%s\n'%''.join(song.split('.')[:-1])+Style.RESET_ALL)
			os.system("cvlc --play-and-exit '%s'"%(l['path']+'/'+song))

def remove():
	print('0. 移除歌单\n1. 移除指定歌单中的歌曲')
	choose=input('\n请输入序号:')
	os.system('clear')
	if choose=='0':
		show_json()
		with open('/home/'+you+'/.songs_list.json','r')as f:
			f=json.loads(f.read())
		string=input('请输入要移除的歌单序号(多个序号间用空格分开):')
		rm_ls=[]
		for s in string.split(' '):
			rm_ls.append(f[int(s)])
		for r in rm_ls:
			f.remove(r)
		with open('/home/'+you+'/.songs_list.json','w')as ff:
			ff.write(json.dumps(f,ensure_ascii=False))
		os.system('clear')
		print('完成! 现有的歌单:\n')
		show_json()
	elif choose=='1':
		show_json()
		with open('/home/'+you+'/.songs_list.json','r')as f:
			f=json.loads(f.read())
		string=input('请输入要进行操作的歌单序号:')
		songs_data=f[int(string)]
		del f[int(string)]
		ls=songs_data['songs']
		for l in ls:
			print(Fore.BLUE+Style.BRIGHT+str(ls.index(l))+Fore.CYAN+'. %s'%''.join(l.split('.')[:-1])+Style.RESET_ALL)
		strin=input('\n请输入要移除的歌曲序号(多个序号间用空格分开):')
		rm_ls=[]
		for s in strin.split(' '):
			rm_ls.append(ls[int(s)])
		ls=list(set(ls)-(set(rm_ls)))
		dic={}
		dic['name']=songs_data['name']
		dic['path']=songs_data['path']
		dic['songs']=ls
		f.append(dic)
		with open('/home/'+you+'/.songs_list.json','r')as ff:
			ff=json.loads(ff.read())
		with open('/home/'+you+'/.songs_list.json','w')as file:
			file.write(json.dumps(f,ensure_ascii=False))
		os.system('clear')
		print('完成! 现在的歌单内容:\n')
		for l in ls:
			print(Fore.BLUE+Style.BRIGHT+str(ls.index(l))+Fore.CYAN+'. %s'%''.join(l.split('.')[:-1])+Style.RESET_ALL)

def board():
	os.system('clear')
	print('0. 播放此目录中的歌曲\n1. 新建基于此目录的歌单\n2. 播放已有歌单\n3. 移除\n')
	choose=input('请输入序号:')
	os.system('clear')
	if choose=='0':
		play()
	elif choose=='1':
		add()
	elif choose=='2':
		play_list()
	elif choose=='3':
		remove()

try:
	board()
except:
	os.system('clear')
	print('出错了...!')