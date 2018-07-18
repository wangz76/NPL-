#!/usr/bin/python
# -*- coding:utf-8 -*-
import pandas as pd
import jieba.analyse


inputfile = r'/Users/wangzhe/PycharmProjects/zj_runone_content.xlsx'

data = pd.read_excel(inputfile)
data = data[u'微博内容']


#第一步：分词，这里使用结巴分词全模式

fenci_text = jieba.cut(str(data))
#print("/ ".join(fenci_text))
#第二步：去停用词
#这里是有一个文件存放要改的文章，一个文件存放停用表，然后和停用表里的词比较，一样的就删掉，最后把结果存放在一个文件中
try:
    stopwords = {}.fromkeys([ line.rstrip() for line in open('/Users/wangzhe/PycharmProjects/stopword.txt') ])
    final = ""
    for word in fenci_text:
      if word not in stopwords:
        if (word != "。" and word != "，") :
          final = final + " " + word

    a=jieba.analyse.extract_tags(final, topK = 80, withWeight = True, allowPOS = ())
    for v,n in a:
        print v + '\t' + str(int(n * 10000))

finally:
    print "结束"

