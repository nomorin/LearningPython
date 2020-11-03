# モジュールの利用.
import math

cal_res = 10 * 20 * math.sin(math.radians(45)) / 2
print(cal_res)

# importはブロックの中でも行える.
# その場合はブロック内のスコープでのみ利用可能になる.

# fromの場合はモジュール名を指定せずに利用可能
# 読み込む時にモジュール名を指定するため
from math import sin, radians
cal_res_2 = 10 * 20 * sin(radians(45)) / 2
print(cal_res_2)

import sys
# モジュールの場所を表示する.
print(sys.path)

# import時に as [name] で別名としてモジュールを利用できる.
# .py スクリプトファイルをモジュールとして利用できる.


