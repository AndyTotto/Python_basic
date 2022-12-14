import datetime

# 文字列を読み込んで日時に変換

# 文字列で時刻の設定
str_time = "2020/01/02 16:09:24"

# 文字列を日時に変換
input_time = datetime.datetime.strptime(str_time, "%Y/%m/%d %H:%M:%S")

print("文字列から変換：")
print(input_time)