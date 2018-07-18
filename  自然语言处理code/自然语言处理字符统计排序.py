# coding: utf-8

import nltk
import sys
reload(sys)
sys.setdefaultencoding('utf8')

fr = open('search-result-guangdong1.txt','r')
charactor = []
stat = {}

for line in fr:
    line = line.strip()

    if len(line) ==0:
        continue

    line = unicode(line)
    for x in xrange(0,len(line)):
        if line[x] in [' ','a','"', 'd','c','s','0','e','1','2','3','4','5','6','7','8','9','i','n','l','=','b','f','g','h','i']:
            continue

        if not line[x] in charactor:
            charactor.append((line[x]))
        if not stat.has_key(line[x]):
            stat[line[x]] = 0
        stat[line[x]] += 1

print len(charactor)
#print charactor
#for key,value in stat.items():
#    print key,value
stat = sorted(stat.iteritems(),key = lambda d:d[1], reverse=True)
for x in xrange(0,20):
    print charactor[x]

print '*'*20

for x in xrange(0,20):
    print stat[x][0],stat[x][1]

fw = open('result.csv', 'w')
for item in stat:
    fw.write(item[0]+','+str(item[1])+'\n')
fw.close()

fr.close()