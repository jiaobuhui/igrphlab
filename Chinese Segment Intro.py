# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <headingcell level=1>

# 中文分词工具

# <headingcell level=3>

# 以结巴分词为例</br>
# >安装 pip install jieba  或者 easy_install jieba </br>
# >官方文档 ：https://github.com/fxsjy/jieba

# <codecell>

import jieba
import jieba.posseg as posg
import jieba.analyse

# <headingcell level=3>

# 基本分词

# <codecell>

s = "你看不到我的内心，我忽略你的情绪。争吵暴露更多，一个人内心根深蒂固的思想不会在热恋中，而只能在争吵中集中凸显出来。接受一个人就是接受他成长过程中所有的热情和顾虑，冷淡和挫折，过往和现在，然后承诺给出自己的未来"
s1 = "有人说，燃油税即使提高，也比欧洲一些国家低。这些所谓的专家真可谓无知。欧洲的99%高速路之所以不收费，就是因为收了燃油税。高速公路的收费体现在燃油税里。没有任何一个国家，一方面，征收昂贵的高速费，同时，还征税超过高昂的燃油税的。如果二者相加，中国又一个全球第一"
result = jieba.cut(s1)
for word in result:
    print word

# <headingcell level=3>

# 词频统计

# <codecell>

freq = {}
for word in result:
    freq[word] = freq.get(word,0)+1
for k in freq:
    print k,freq[k]

# <headingcell level=3>

# 输出词性 & 按词性筛选

# <codecell>

result_pos = posg.cut(s)
for word in result_pos:
    if word.flag in ["n","v","adj"]: #按词性提取
        print word.word,word.flag

# <headingcell level=3>

# 提取关键词

# <codecell>

keywords = jieba.analyse.extract_tags(s1,10,True)

# <codecell>

for kw in keywords:
    print kw[0],kw[1]

# <headingcell level=3>

# 生成语义网络

# <codecell>

word_list = []
for word in result:
    word_list.append(word)
length = len(word_list)
for i in range(0,length-1):
    print word_list[i],word_list[i+1]

# <headingcell level=3>

# 文件分词

# <codecell>

text = open("c:/users/tanhe/desktop/test.txt","r").readlines()
#text_seg = jieba.cut(text)
#for word in text_seg:
    #print word
for line in text:
    print line.strip().decode("gbk")  #需确定文件编码

# <codecell>

wordlist = []
out_file = open("c:/users/tanhe/desktop/output.txt","w")
for line in text:
    parag = "\n".join(jieba.cut(line.strip()))
    out_file.write(parag)
out_file.close()

# <codecell>

print wordlist

# <codecell>


for word in result:
    out_file.write("")

