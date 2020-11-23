def is_chinese(word):
    for w in word:
        if u'\u4e00' <= w <= u'\u9fff':
            return True
        return False
