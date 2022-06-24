import yaml

##读取配置用
conf=yaml.load(open('data/conf.yaml'),Loader=yaml.FullLoader)
music_dir=conf['music_dir']
list_dir=conf['list_dir']