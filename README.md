# Terminal-Player
> 一个根据文件hash操作的,基于sox的终端播放器.

![演示](https://ghproxy.com/https://raw.githubusercontent.com/wzk0/photo/main/202206241928082.png)

## 用法

首先,clone此仓库:

```bash
git clone https://github.com/wzk0/terminal-player
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

> 英文版本可输入`python3 en_main.py`运行.

> 如果提示报错,可能是缺少依赖,请输入`pip install Pyyaml`.

之后按照序号提示进行即可.

## 特点

* 一次性可以播放单曲/多首音乐(临时歌单).

* 可以创建歌单(根据文件hash值).

* ...

  > 可能会添加**收藏**功能.

## 原理

根据每一个文件独一无二的hash值确定,所以即使添加新的音乐到目录也**没有问题**!

> 注释也挺清楚的..

播放器使用的是`sox`(这我肯定不会做啊).

## 尾声

感谢使用!O(∩_∩)O
