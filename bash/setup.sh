#!/bin/bash

echo "# >>>>>>>>>>>>> youdao_linux configuration >>>>>>>>>>>>>>>" >>~/.bashrc
echo "alias query='bash ~/youdao_linux/bash/query.sh'" >> ~/.bashrc
echo "# >>>>>>>>>>>>> youdao_linux configuration >>>>>>>>>>>>>>>" >>~/.bashrc
cp -r ./../../ ~
echo "youdao_linux has been installed!"
source ~/.bashrc
