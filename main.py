from src import api
import os
import sys

os.system('clear')
dsktp=['0. 播放音乐','1. 播放歌单','2. 制作歌单','3. 收藏','4. 设置','5. 退出']
for s in dsktp:
	print(s,end='\n============\n\n')
ipt=input('请输入序号:')
os.system('clear')

if ipt=='0':
	print('音乐正在加载中...\n')
	api.show_list()
	print('\n完成!\n')
	ipt=input('请输入歌曲前的序号以播放(可以用空格分隔开多个序号):')
	name=api.back_name(api.make_list(ipt))
	api.play(name)
	print('是/否(y/n)把刚刚播放的音乐添加入歌单?')
	chs=input('y / n :')
	if chs=='y':
		list_name=input('请为这张歌单命名:')
		api.write_into(ipt,list_name)
		print('\n完成!\n')
		sys.exit()
	else:
		sys.exit()

if ipt=='1':
	print('歌单正在加载中...\n')
	api.show_songsls()
	print('\n完成!\n')
	ipt=input('请输入歌单前的序号以播放:')
	for hsh in api.back_hash(ipt):
		api.play_hash(hsh)
	sys.exit()

if ipt=='2':
	print('音乐正在加载中...\n')
	api.show_list()
	print('\n完成!\n')
	ipt=input('请输入歌曲前的序号,每个序号间用空格分隔开:')
	name=api.back_name(api.make_list(ipt))
	list_name=input('请为这张歌单命名:')
	api.write_into(ipt,list_name)
	print('\n完成!\n')
	sys.exit()

if ipt=='3':
	print('音乐正在加载中...\n')
	api.show_list()
	print('\n完成!\n')
	ipt=input('请输入歌曲前的序号,每个序号间用空格分隔开:')
	api.like(ipt)
	print('\n完成!\n')
	sys.exit()

if ipt=='4':
	os.system('nano data/conf.yaml')
	sys.exit()

if ipt=='5':
	print('Bye~~ O(∩_∩)O~~')
	sys.exit()