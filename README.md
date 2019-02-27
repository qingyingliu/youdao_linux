## 有道词典linux版

### 下载
`git clone https://github.com/Lewin671/youdao_linux.git`, 欢迎大家pull和star。

### 安装说明: 
1. 进入项目的文件夹，然后在终端下执行命令:`bash setup.sh` 或者`./setup.sh`。


### 环境

1. Anaconda最新版[Anaconda3-5.3.1-Linux-x86_64.sh](https://mirrors.tuna.tsinghua.edu.cn/anaconda/archive/Anaconda3-5.3.1-Linux-x86_64.sh)

2. 安装完anaconda后，将环境添加到`～/.bashrc`（anaconda的一个安装选项）。

3. 在命令行下安装`Scrapy`，`conda install scrapy`，并更新anaconda。

4. 音乐播放器: `pygame`．安装命令:`pip install pygame`．

5. sqlite3操作SQLITE数据库，一般`linux`系统自带．如果没有，使用`pip install sqlite3`安装．

6. scrapy运行js库：`scrapy_splash`.　安装方法：`pip install scrapy_splash`．
   
### 使用说明：

1. 默认查询命令是`query [单词或者短语]`。如果需要更改命令，请在`~/.bashrc`中更改别名(alias)。

2. 如果有例句有显示出来，最多显示三条。

3. 查看最常查询的词汇，使用参数`--analysis`: `query analysis`．

４. 默认发音为英式发音，可以在`package`的`config.py`更改`SOUND`变量．
   
### 效果

![example1](./pic/example1.png)
![example2](./pic/example2.png)

### 此次更新

1. 将用`csv`存储数据改为数据库存取，优化存取和查询效率．

2. 添加单词读音，可以在`package`包里面设置`config.py`的`SOUND`,如果不想发音可以注释掉`SOUND`变量．

3. 整体优化项目结构．

注意： 该项目仅仅供自己学习和分享给大家学习用途。如果有问题可以通过邮箱联系我：2596736318@qq.com
