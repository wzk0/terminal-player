import yaml

def get_good_name(name):
	name=name.replace('(','\(')
	name=name.replace(')','\)')
	name=name.replace(' ','\ ')
	return name

##读取配置用
conf=yaml.load(open('data/conf.yaml'),Loader=yaml.FullLoader)
music_dir=conf['music_dir']
music_dir=get_good_name(music_dir)
list_dir=conf['list_dir']
list_dir=get_good_name(list_dir)