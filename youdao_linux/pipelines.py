# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exceptions import DropItem

class YoudaoLinuxPipeline(object):
    def process_item(self, item, spider):
        # print("go to process_item ")

        from package.db import get_db,select_word_by
        try:
            if(item['meanings'] != ""):
                db = get_db()
                cursor = db.cursor()
                cursor.execute(("insert into word(word,phonetic_symbol,word_attr,meanings,en_sentence1,"
                                "cn_sentence1,en_sentence2,cn_sentence2,en_sentence3,cn_sentence3) values (?,?,?,?,?,?,?,?,?,?)"),
                               (str(item['word']),item['phonetic_symbol'],item['word_attr'],item['meanings'],item['en_sentence1'],
                                item['cn_sentence1'],item['en_sentence2'],item['cn_sentence2'],item['en_sentence3'],
                                item['cn_sentence3']))
                db.commit()
                db.close()

        except Exception as e:
            print(e)
            raise DropItem()


        #下载音频到本地
        #print(item['sounds'])
        sounds = item['sounds'].split(',')

        if sounds[0]!="":
            import urllib
            import os
            word = item['word']

            dir_path = os.path.join(os.path.abspath('data/sounds'),word[0])
            if not os.path.exists(dir_path):
                os.makedirs(dir_path)

            sound_path = os.path.join(dir_path,word+"_uk.mp3")
            urllib.request.urlretrieve(sounds[0],sound_path)

            sound_path = os.path.join(dir_path,word+"_us.mp3")
            urllib.request.urlretrieve(sounds[0],sound_path)

        else:
            print("no sounds")

        return item

