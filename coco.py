
import requests
import jieba
from bs4 import BeautifulSoup
from pyecharts.charts import WordCloud

# 请求链接并获取响应数据
url = "https://nocturne-spider.baicizhan.com/2020/09/02/coco/"
headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"}
response = requests.get(url,headers=headers)
html = response.text
soup = BeautifulSoup(html,"lxml")
content_all = soup.find_all(name="em")
# print(content_all)

# 解析数据并将内容存在列表中
wordList = []
for content in content_all:
    contentString = content.string
    # 列表转化成字符串并分词
    words = jieba.lcut(contentString)
    wordList = wordList + words

# 利用字典进行词频统计
wordDict = {}
for word in wordList:
    if len(word)>1:
        if word not in wordDict:
            wordDict[word] = 1
        else:
            wordDict[word] += 1

# 按照要求生成词云图
wordCloud = WordCloud()
wordCloud.add(series_name = "",data_pair=wordDict.items(),width=800,height=500,word_size_range=[30,70])
wordCloud.render("dream.html")
print("success")
