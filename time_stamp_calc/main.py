import datetime
import time

# 現在時刻を取得
start = datetime.datetime.now()

time.sleep(15)

# 現在時刻を取得
end = datetime.datetime.now()

# 実行時刻計算
do_time = end - start
print("実行時間：")
print(do_time)