# Terminal-Player

![演示](https://ghproxy.com/https://raw.githubusercontent.com/wzk0/photo/main/202210022149432.png)

![演示](https://ghproxy.com/https://raw.githubusercontent.com/wzk0/photo/main/202210022152595.png)

![演示](https://raw.githubusercontent.com/wzk0/photo/main/%E6%88%AA%E5%9B%BE%202022-07-30%2016-04-27.png)

## 介绍

这是一个根据文件hash操作的,基于`sox`或者`cvlc`的终端播放器.

> `cvlc`是`vlc`的终端版本.

你可以指定一个塞满音频文件的目录为音乐夹,进行`创建并且播放歌单`,`收藏并且播放单曲`,`删除或清理歌单`等操作.

## 特点

* 一次性可以播放单曲/多首音乐(临时歌单).

* 可以创建歌单(根据文件hash值).

* 界面颜色丰富(挺好看的).

* 支持终端实时歌词显示,桌面歌词不同皮肤设置.

* ...

> ~~可能会添加**收藏**功能~~. 已完成

> 可能会添加`读取多个音乐目录`功能.

## 用法

首先,clone此仓库:

```bash
git clone https://github.com/wzk0/terminal-player
```

安装`sox`或`vlc`:

```
sudo apt install sox -y
或
sudo apt install vlc -y
```

随后,在所在文件夹打开终端,输入:

```bash
nano data/conf.yaml
```

编辑**配置文件**.

接着输入:

```bash
python3 main.py
```

运行**主程序**.

> 如果提示报错,可能是缺少依赖,请输入`pip install pyyaml`.

之后按照序号提示进行即可.

## 注意

* 由于`pyyaml`读取配置文件的特性,请不要指定路径中`有空格的目录`为音乐目录.

* 填写配置文件时,需要注意最后面有没有`/`,没有请务必加上.

## 原理

根据每一个文件独一无二的hash值确定,所以即使添加新的音乐到目录也**没有问题**!

> 注释也挺清楚的..

播放器核心使用的是`sox`或`cvlc`(这我肯定不会做啊).

## 尾声

感谢使用!O(∩_∩)O

## 相关

终端歌词显示:

[通过sleep实现的终端lrc歌词文件解析和实时展示.](https://github.com/wzk0/lrc-timely)