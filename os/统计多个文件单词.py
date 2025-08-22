import 统计文件单词
import os


def count_word(dir,set_count={}):

    while True:
        lst = os.listdir(dir)
        for i in range(len(lst)):
            pull_path = os.path.join(dir,lst[i])
            if os.path.isfile(pull_path):
                set_count = 统计文件单词.is_word(pull_path,set_count)
            else:
                count_word(pull_path)
        break
    return set_count
# print(count_word("D:/桌面/afsd"))

dit = {"a":"apple","at":"apple"}

def add_dict(set_count,dit):
    word = {}
    for i in set_count:
        if i in dit:
            i = dit[i]
        word[i] = word.get(i,0)+set_count.get(i,0)+1
    return word
set_kjkj = count_word("D:/桌面/afsd")
word = add_dict(set_kjkj,dit)
# word = sorted(word)

print(word)



            

