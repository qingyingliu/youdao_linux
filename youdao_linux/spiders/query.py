import scrapy
from bs4 import BeautifulSoup

class QuerySpider(scrapy.Spider):
    # usage: scrapy crawl query -a word=good --nolog
    name = "query"

    def __init__(self, word=None,crawl=None, *args, **kwargs):
        super(QuerySpider, self).__init__(*args, **kwargs)
        if crawl != None:
            self.flag = False
            file = open("data/word.txt")
            self.start_urls = []
            for line in file.readlines():
                wd = line.split(" ")[1].strip()
                self.start_urls.append('http://www.iciba.com/%s' % wd)
        elif word != None:
            self.start_urls = ['http://www.iciba.com/%s' % word]
        
    def start_requests(self):
        for url in self.start_urls:
            yield self.make_requests_from_url(url)

    def parse(self,response):
        # 音标
        phonetic_symbol = response.css('.base-speak').xpath('./span/span/text()').extract()

        # 词性
        word_attr = response.css('.clearfix').xpath('./span/text()').extract()

        # 单词意思
        meanings = list()
        for meaning in response.css('.clearfix').xpath('./p'):
            meanings.append("".join(meaning.xpath('./span/text()').extract()))

        # 例句
        en_sentence = list()
        cn_sentence = list()
        soup = BeautifulSoup(response.text,'html.parser')
        cnt = 1
        example = soup.select('.prep-order > .text-sentence p')
        for item in example:
            if cnt > 6:
                break
            if cnt % 2 == 0:
                cn_sentence.append(item.text.strip())
            else:
                en_sentence.append(item.text.strip())
            cnt+=1
            #print(item)

        word = response.url[21:].strip()
        if phonetic_symbol != None :
            yield{
                # 防止错误编码
                'word': word.replace('%20',' '),
                'phonetic_symbol': phonetic_symbol,
                'word_attr': word_attr,
                'meanings': meanings,
                'en_sentence1': en_sentence[0],
                'cn_sentence1': cn_sentence[0],
                'en_sentence2': en_sentence[1],
                'cn_sentence2': cn_sentence[1],
                'en_sentence3': en_sentence[2],
                'cn_sentence3': cn_sentence[2],
            }

