#!/bin/bash

if [ $# -eq 0 ]
then
    echo "you didn't input a word"
    exit 1
fi

cd ~/youdao_linux/bash

# 统计查询信息
echo "$1,$(date)" >> ./../data/count.csv

# 查询
python3 ../python/combined_query.py "$*" #2> /dev/null
cd - > /dev/null
