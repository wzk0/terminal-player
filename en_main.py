from src import api
import os

os.system('clear')
dsktp=['0. Play A Song or Songs','1. Play Songs_List','2. Make A Songs_List','3. Setting','4. Exit']
for s in dsktp:
	print(s,end='\n============\n\n')
ipt=input('Pls tell me what you want to do next :')
os.system('clear')

if ipt=='0':
	print('Your Music is Loading...\n')
	api.show_list()
	print('\nDone!\n')
	ipt=input('Pls input the ID before the name of song ( you can split the IDs with " " then you can play more than 1 song ) :')
	name=api.back_name(api.make_list(ipt))
	api.play(name)
	print('Do you want to write the songs into a list ?')
	chs=input('y / n :')
	if chs=='y':
		list_name=input('Pls name you list for these songs :')
		api.write_into(ipt,list_name)
		print('\nDone!\n')
	else:
		pass

if ipt=='1':
	print('Your Music is Loading...\n')
	api.show_songsls()
	print('\nDone!\n')
	ipt=input('Pls input the ID before the list to play it :')
	for hsh in api.back_hash(ipt):
		api.play_hash(hsh)

if ipt=='2':
	print('Your Music is Loading...\n')
	api.show_list()
	print('\nDone!\n')
	ipt=input('Pls input the ID before the name of song , you can split the IDs with " " :')
	name=api.back_name(api.make_list(ipt))
	list_name=input('Pls name you list for these songs :')
	api.write_into(ipt,list_name)
	print('\nDone!\n')

if ipt=='3':
	os.system('nano data/conf.yaml')

if ipt=='4':
	print('Bye~~ O(∩_∩)O~~')
	pass