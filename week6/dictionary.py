words = set()


def load(dictionary):
    # open()の使用感はC言語と同じ
    # どちらかというとwithでfile openするのが通例かも(closeし忘れ防止)
    file = open(dictionary, "r")
    for line in file:
        # line.rstrip()で改行の削除ができる
        words.add(line.rstrip())
    file.close()
    return True


def check(word):
    # lowerで小文字にできる。便利。
    if word.lower() in words:
        return True
    else:
        return False


def size():
    # set型は当然長さの情報を持っているのでlen()で長さが確認できる
    return len(words)


# ポインタ、アドレスについて考える必要がないのでunloadの実装は必要ない
def unload():
    return True
