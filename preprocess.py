import jieba
import os


# 载入停用词表
def stopwordslist(filepath):
    stopwords = [line.strip() for line in open(filepath, 'r', encoding='utf-8').readlines()]
    return stopwords


# 主要思想是分词过后，遍历一下停用词表，去掉停用词。
# 对句子进行分词
def seg_sentence(sentence):
    sentence_seged = jieba.cut(sentence.strip())
    st_path=os.getcwd()+'\\Stopwords\\1893（utf8）.txt'
    stopwords = stopwordslist(st_path)  # 这里加载停用词的路径
    outstr = ''
    for word in sentence_seged:
        if word not in stopwords:
            if word != '\t':
                outstr += word
                outstr += " "
    return outstr


# 输入的文档应该放在input文件夹下
input_path=os.getcwd()+'\\input\\source1.txt'
inputs = open(input_path, 'r', encoding='utf-8')
output_path=os.getcwd()+'\\output\\output1.txt'
outputs = open(output_path, 'w',encoding='utf-8')
for line in inputs:
    line_seg = seg_sentence(line)  # 这里的返回值是字符串
    outputs.write(line_seg + '\n')
outputs.close()
inputs.close()