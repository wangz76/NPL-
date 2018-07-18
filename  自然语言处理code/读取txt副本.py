# -*- coding:utf-8 -*-


from snownlp import SnowNLP
import pandas as pd
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


f = open("/Users/wangzhe/PycharmProjects/first/search-result-hainan.txt")


text1=[i.decode('utf-8') for i in f]
data = text1

print data
print('读入成功')

print('本电脑正在尽全力运算，别催！')
sentences = []
senti_score = []
for i in data:
    a1 = SnowNLP(i)
    a2 = a1.sentiments
    sentences.append(i)  # 语序...
    senti_score.append(a2)
print '快算完了！！！'
count = 0
for i in senti_score:
    if i > 0.6:
        count += 1

b = len(senti_score)

a = (count/float(b))
print '计算结果如下'
print '\n' + "关于浙江最多跑一次的微博总条数为" +" "+ str(len(senti_score)) + "条"
print '\n' + "积极微博条数为" +" " + str(count) + "条"
print '\n' + "积极微博占比为" + " " + str(a)