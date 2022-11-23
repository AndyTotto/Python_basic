import datetime
import time

# 時刻とUnixTimeの変換
# 時刻を入力
input_time = datetime.datetime(2020, 1, 10, 10, 20, 30)
# input_time = datetime.datetime(2020, 1, 10, 10, 20, 30, 123)

# 入力した時刻を出力
print("普通に取得：", end="")
print(input_time)

# UnixTimeに変換する
input_unix_time = (int)(time.mktime(input_time.timetuple()))
print("UnixTimeに変換： ", end="")
print(input_unix_time)