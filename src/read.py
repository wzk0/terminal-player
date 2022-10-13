import yaml

def get_good_name(name):
	name=name.replace('(','\(')
	name=name.replace(')','\)')
	name=name.replace(' ','\ ')
	return name

##读取配置用
conf=yaml.load(open('data/conf.yaml'),Loader=yaml.FullLoader)
music_dir=conf['music_dir']
list_dir=conf['list_dir']
player_core=conf['player_core']
lrc_path=conf['lrc_path']
rainbow=conf['rainbow']
pure_color=conf['pure_color']
sleep_time=conf['sleep_time']
preview=conf['preview']
analysis=conf['analysis']
music_dir=get_good_name(music_dir)
list_dir=get_good_name(list_dir)
if player_core=='cvlc ':
	player_core='cvlc --play-and-exit '