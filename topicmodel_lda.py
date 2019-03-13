import codecs
import os
from gensim import corpora
from gensim.models import LdaModel

train = []
text_path=os.getcwd()+'\\output\\output1.txt'
# 对比open()方法，codecs.open()用于读写unicode编码方式的文档
fp = codecs.open(text_path,'r',encoding='utf8')
for line in fp:
    line = line.split()
    train.append([w for w in line])

dictionary = corpora.Dictionary(train)  # 创建语料的字典
corpus = [dictionary.doc2bow(text) for text in train]  # 将文本转换为词袋向量
lda = LdaModel(corpus=corpus, id2word=dictionary, num_topics=20)  # 训练lda模型

for topic in lda.print_topics(num_words=10):
    termNumber = topic[0]
    print(topic[0], ':', sep='')
    listOfTerms = topic[1].split('+')
    for term in listOfTerms:
        listItems = term.split('*')
        print('  ', listItems[1], '(', listItems[0], ')', sep='')

