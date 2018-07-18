# coding: utf-8
import sys
import urllib
import urllib2
from BeautifulSoup import BeautifulSoup

question_word = "浙江最多跑一次"

url = "http://www.baidu.com/s?wd=" + urllib.quote(question_word.decode(sys.stdin.encoding).encode('gbk'))

def title_get(url):
    htmlpage = urllib2.urlopen(url).read()
    soup = BeautifulSoup(htmlpage)
    # print len(soup.findAll("h3", {"class":"t"}))
    name = []
    for result_table in soup.findAll("div", {"class": "result c-container "}):
        a_click = result_table.find("div")
        title = a_click.renderContents()  # 标题
        title = title.replace("<em>", "").replace("</em>", "").replace('<span class=" newTimeFactor_before_abs m">',"").replace('&nbsp;-&nbsp;</span>',"")
        # print title
        name.append(title)
    return name

def item_get(url):
    htmlpage = urllib2.urlopen(url).read()
    soup = BeautifulSoup(htmlpage)
    item = []
    for href_table in soup.findAll("div", {"id": "page"}):
        href_click = href_table.findAll("a")
        for i in href_click:
            href = i.get("href")
            item.append(href)
    return item


def url_new(item):#page_url
    url_item = []
    for s in range(len(item)):
        url = "http://www.baidu.com/s?wd=" + item[s]
        url_item.append(url)
    return url_item

a = title_get(url)
b = item_get(url)
c = url_new(b)

content = []
for s in range(len(c)):
    e = title_get(c[s])
    content.append(e)


with open("search-result-guangdong1.txt","w") as f:
    for i in content:
        for j in i:
            f.write("\n"+ str(j))
    f.close()

