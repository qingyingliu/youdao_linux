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
    cd ~/youdao_linux/
	python3 ~/youdao_linux/analysis.py
    cd - > /dev/null
	exit 0
fi

cd ~/youdao_linux
# 查询
python3 query.py "$*" #2> /dev/null
cd - > /dev/null
