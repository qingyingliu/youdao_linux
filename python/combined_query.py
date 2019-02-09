import pandas as pd 
import sys
from color import *
import os
import math
import datetime

if __name__ == "__main__":
        
    word = " ".join(sys.argv[1:])
    path = "~/youdao_linux/data/word.csv"
    data = pd.read_csv(path,encoding='utf8')
    data = data.set_index('word')
    
    if word not in data.index:
        os.system("scrapy crawl query -a word='"+word+"' -o ~/youdao_linux/data/word.csv --nolog -s FEED_EXPORT_ENCODING=UTF-8")

    # reload
    data = pd.read_csv(path,encoding='utf8')
    data = data.set_index('word')
    
    if word not in data.index:
        print(fmt(color.RED,"sorry, there are no this word!"))
        
    else:
        line = data.loc[word]
        # get data from csv
        phonetic_symbol = line['phonetic_symbol']
        word_attr = list(str(line['word_attr']).split(','))
        meanings = str(line['meanings']).split(",")
        cn_sentence = list()
        en_sentence = list()
        cn_sentence.append(line['cn_sentence1'])
        cn_sentence.append(line['cn_sentence2'])
        cn_sentence.append(line['cn_sentence3'])
        en_sentence.append(line['en_sentence1'])
        en_sentence.append(line['en_sentence2'])
        en_sentence.append(line['en_sentence3'])

        # print result


        # 判断是否有这个单词
        if(len(meanings)==0):
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
                if type(en_sentence[i]) is float and math.isnan(en_sentence[i]):
                    break
                print()
                print(i+1,".",fmt(color.YELLOW,en_sentence[i]))
                print(fmt(color.PURPLE, cn_sentence[i]))

            print()

            # 添加到统计csv
            d = datetime.datetime.now()
            df1 = pd.DataFrame({
                'word':[word],
                'date': ["%s-%s-%s %s:%s:%s" % (d.year,d.month,d.day,d.hour,d.minute,d.second)]
            })
            df1.to_csv('~/youdao_linux/data/count.csv', mode='a', header=False,index=False)
