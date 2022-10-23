import datetime
import time

# 時刻とUnixTimeの変換
## 時刻を入力
input_time = datetime.datetime(2020, 1, 10, 10, 20, 30, 123)
print("普通に取得：", end="")
print(input_time)
print("マイクロ秒： ", end="")
print(input_time.microsecond)
print("UnixTimeに変換： ", end="")
print(int(time.mktime(input_time.timetuple())))
print("UnixTime(ミリ秒)に変換： ", end="")
print(int(time.mktime(input_time.timetuple())) + input_time.microsecond/1000)

print("-------------------")
# 現在時刻の取得
now = datetime.datetime.now()
print("現在時刻を取得：", end="")
print(now)


print("-------------------")
# 文字列を読み込んで日時に変換
# 日付の文字列から時刻へ
str_time = "2020/01/02 16:09:24"
input_time2 = datetime.datetime.strptime(str_time, "%Y/%m/%d %H:%M:%S")
print("文字列から変換： ", end="")
print(input_time2)
