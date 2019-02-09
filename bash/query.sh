#!/bin/bash

if [ $# -eq 0 ] || test "$1" == "--help"
then
	echo "<<<<<<<<< youdao_linux <<<<<<<<<<<<<<<"
	echo ""
    echo "Usage: query [option] [word or phrase]"
    echo "option are as follows: "
    echo "--help: show the manual of youdao_linux."
    echo "--analysis: show the frequency words that you have queried."
    echo ""
    echo "<<<<<<<<< youdao_linux <<<<<<<<<<<<<<<"
    exit 0
fi

if [ "$1" == "--analysis" ]
then
    cd ~/youdao_linux/python
	python3 ~/youdao_linux/python/analysis.py
    cd -
	exit 0
fi

cd ~/youdao_linux/bash

# 查询
python3 ../python/combined_query.py "$*" #2> /dev/null

cd - > /dev/null