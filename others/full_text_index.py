import jieba
import collections
"""

一个关于 全文检索的 python demo

"""


articles = (
    (1, '今生今世 永不再将你想起 除了 除了在有些个 因落泪而湿润的夜里 如果 如果你愿意'),
    (2, '有一天路标迁了希望你能从容有一天桥墩断了希望你能渡越有一天栋梁倒了希望你能坚强有一天期待蔫了希望你能理解'),
    (3, '你 一会看我一会看云我觉得你看我时很远你看云时很近'),
    (4, '你站在桥上看风景 看风景人在楼上看你 明月装饰了你的窗子 你装饰了别人的梦'),
    (5, '我向你倾吐思念 你如石像 沉默不应 如果沉默是你的悲抑 你知道这悲抑最伤我心')
)

text_index = {}


def gen_index():

    for article in articles:
        index, text = article
        words = jieba.lcut_for_search(text)
        # 这里只对单词长度大于一的词语做分词，顺便剔除空格符
        words = [wd for wd in words if len(wd) > 1]

        # print(collections.Counter(words))

        for word, count in collections.Counter(words).items():
            index_count = text_index.get(word)
            if index_count is None:
                text_index[word] = [0] * len(articles)
                text_index[word][index-1] = count
            else:
                index_count[index-1] = count


def search(word: str):
    text_index_get = text_index.get(word)
    if text_index_get is None:
        print('没有文章满足')
    else:
        [print("文章为：" + dict(articles).get(index+1) + "  得分：" + str(count))
         for index, count in enumerate(text_index_get) if count > 0]


def main():
    gen_index()
    search("如果")


if __name__ == "__main__":
    main()
