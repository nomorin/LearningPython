#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 組込型を継承する.
# 辞書型の継承.

class StrDictionary(dict):
    def __init__(self):
        pass

    def __setitem__(self, key, value):
        """
        特殊メソッドをオーバーライドする.
        keyが文字列型以外なら例外を発生させる.
        :param key:
        :param value:
        :return:
        """

        if not isinstance(key, str):
            # isinstance はtypeofと同じように型の判定を行う.

            # キーが文字列ではない場合には例外を発生.
            # raise で例外を送出する.(javaのthrowと同じ)
            raise ValueError("Key must be str or unicode.")

        dict.__setitem__(self, key, value)


d = StrDictionary()
d["spam"] = 1
print(d["spam"])

# これは登録されていないのでエラーになる.
# d[1] = 1

print(d.keys())
