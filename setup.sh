#!/bin/bash

echo "# >>>>>>>>>>>>> youdao_linux configuration >>>>>>>>>>>>>>>" >>~/.bashrc
echo "alias query='bash ~/youdao_linux/query.sh'" >> ~/.bashrc
echo "# >>>>>>>>>>>>> youdao_linux configuration >>>>>>>>>>>>>>>" >>~/.bashrc

# 复制到home
cp -r ./../../ ~

# 配置config.py
rm ~/youdao_linux/package/config.py
cd ~
home=$(pwd)
cd -
echo "DATABASE_URI = '$home/youdao_linux/data/data.db'" >> ~/youdao_linux/package/config.py
echo "DATABASE_SCHEMA = '$home/youdao_linux/data/schema.sql'" >> ~/youdao_linux/package/config.py
echo "#　默认英式读音，可以通过设置ＳＯＵＮＤ为'UK'来改成美式读音" >> ~/youdao_linux/package/config.py
echo "# 如果不想要读音，可以注释掉SOUND变量" >> ~/youdao_linux/package/config.py
echo "SOUND = 'UK'" >> ~/youdao_linux/package/config.py


echo "youdao_linux has been installed!"
source ~/.bashrc

