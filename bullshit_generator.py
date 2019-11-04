import os
import re
import random
import readJSON


data = readJSON.read_json("data.json")
idiom = data["famous"]  # a 代表前面垫话，b代表后面垫话
before = data["before"]  # 在名人名言前面弄点废话
after = data['after']  # 在名人名言后面弄点废话
shit_start = data['bosh_start']
shit = data['bosh']  # 代表文章主要废话来源

title = "來點廢話"

repeat = 2


def random_loop(l):
    global repeat
    pool = list(l) * repeat
    while True:
        random.shuffle(pool)
        for i in pool:
            yield i

            
next_shit = random_loop(shit)
next_idiom = random_loop(idiom)
next_shit_start = random_loop(shit_start)


def add_idiom():
    global next_idiom
    xx = next(next_idiom)
    xx = xx.replace("a", random.choice(before))
    xx = xx.replace("b", random.choice(after))
    return xx


def another_paragraph():
    xx = ""
    xx += "\r\n"
    xx += "    "
    return xx


if __name__ == "__main__":
    xx = input("请输入文章主题: ")
    length = int(input("字數: "))
    total = 0
    tmp = str('    ')
    while (len(tmp) < length):
        conditiion = random.randint(0, 100)
        conditiion1 = random.randint(0, 100)
        if conditiion < 5:
            tmp += another_paragraph()
        elif conditiion < 20:
            if conditiion1 < 40:
                tmp += next(next_shit_start)
            tmp += add_idiom()
        else:
            if conditiion1 < 40:
                tmp += next(next_shit_start)
            tmp += next(next_shit)
    tmp = tmp.replace("x", xx)
    total += len(tmp)
    print(tmp)
