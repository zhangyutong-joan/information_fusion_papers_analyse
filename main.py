from collections import Counter
import re


def getText(filename):
    txt = open(filename,"r").read()
    # 变成小写
    txt = txt.lower()
    # 处理特殊符号
    for ch in '''!"$%&()*+,-./;:<=>?@[\\]^_{|}~''\n\t ''':
          txt = txt.replace(ch," ")
    return txt

def tongji(text, words_dict_file):
    with open(text, 'r', encoding='utf-8') as file:
        txt= file.read().lower()  # 将文本内容转换为小写以便进行匹配
        # 处理特殊符号
        for ch in '''!"$%&()*+,-./;:<=>?@[\\]^_{|}~''\n\t ''':
            content = txt.replace(ch," ")

    with open(words_dict_file, 'r', encoding='utf-8') as dict_file:
        words_dict = set(dict_file.read().lower().split())  # 读取关键词字典并转换为小写后放入集合中

    words = content.split()  # 切分文本内容为单词列表

    # 统计文本中每个词组（根据字典划分）的出现次数
    word_counts = Counter([word for word in words if word in words_dict])

    # 计算总词数
    total_words = sum(word_counts.values())

    # 计算每个词组的词频
    word_frequencies = {word: count / total_words for word, count in word_counts.items()}

    # 按词频排序
    sorted_word_frequencies = dict(sorted(word_frequencies.items(), key=lambda item: item[1], reverse=True))

    # 获取词频最高的前20%词组
    num_top_words = int(0.2 * len(sorted_word_frequencies))
    top_words_and_frequencies = {k: sorted_word_frequencies[k] for k in list(sorted_word_frequencies)[:num_top_words]}

    return top_words_and_frequencies



if __name__ == '__main__':
    result = tongji('最新-正在.txt', 'fusion关键词库.txt')
    print(result)
