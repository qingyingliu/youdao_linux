import pandas as pd 
import sys
from . import color
import os
import math
import datetime
from . import db
from . import config


def display_music(path):
    import pygame
    pygame.mixer.init()
    track = pygame.mixer.music.load(path)
    pygame.mixer.music.play()
    import time
    time.sleep(1.5)  # 播放10秒
    pygame.mixer.music.stop()  # 停止播放


def query(word):

    fmt = color.fmt

    result = db.select_word_by(word)

    if len(result) == 0:
        try:
            # print("scrapy crawl query -a word='"+word+"'")
            os.system("scrapy crawl query -a word='"+word+"' --nolog")

        except Exception as e:
            print("query error",e)

    # reload
    result = db.select_word_by(word)

    # rejudge
    if len(result) == 0:
        print(fmt(color.RED,"sorry, there are no this word!"))

    else:
        result = result[0]
        phonetic_symbol = result['phonetic_symbol']
        word_attr = list(str(result['word_attr']).split(','))
        meanings = str(result['meanings']).split(",")
        cn_sentence = list()
        en_sentence = list()
        cn_sentence.append(result['cn_sentence1'])
        cn_sentence.append(result['cn_sentence2'])
        cn_sentence.append(result['cn_sentence3'])
        en_sentence.append(result['en_sentence1'])
        en_sentence.append(result['en_sentence2'])
        en_sentence.append(result['en_sentence3'])

        # print result


        # 判断是否有这个单词
        if len(result) == 0:
            print(fmt(color.RED,'sorry, there are no this word.'))
            sys.exit(100)

        else:
            # 单词
            print(fmt(color.GREEN,word))
            # 音标
            print(fmt(color.YELLOW,phonetic_symbol))
            # 意思
            for i in range(len(word_attr)):
                print(fmt(color.CYAN,word_attr[i]),fmt(color.PURPLE,"".join(meanings[i])))

            # 例句
            for i in range(len(en_sentence)):
                if en_sentence[i] is None or en_sentence[i].strip()=="":
                    break
                print()
                print(i+1,".",fmt(color.YELLOW,en_sentence[i]))
                print(fmt(color.PURPLE, cn_sentence[i]))

            print()


            # 添加到统计count
            db.update_times(word)

            # 读音
            dir_path = os.path.join(os.path.abspath('data/sounds'), word[0])
            if config.SOUND == "UK":
                display_music(os.path.join(dir_path,word+"_uk.mp3"))
            elif config.SOUND == "US":
                display_music(os.path.join(dir_path, word + "_us.mp3"))

