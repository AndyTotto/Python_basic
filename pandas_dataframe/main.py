import pandas as pd
import warnings

# warningが邪魔だったので設定
warnings.simplefilter('ignore')

# 空のDataFrameを作成
df = pd.DataFrame(columns=["Name", "Score"])
# 結果の確認
print("空のDataFrameを作成")
print(df)
print("----------")

# 列"Name"に値を入れる
df["Name"] = ["Andy", "たろう"]
# 結果の確認
print("列Nameに値を入れる")
print(df)
print("----------")

# Name"Andy"のScore列に数字を設定
df.loc[df["Name"] == "Andy", "Score"] = 60
# Name"たろう"のScore列に数字を設定
df.loc[df["Name"] == "たろう", "Score"] = 70
# 結果の確認
print("Andyとたろうにscoreを設定")
print(df)
print("----------")

# 一行 Name, Scoreのセットを加える
df_temp = pd.DataFrame({"Name":["ななし"], "Score":[100]})
df = df.append(df_temp)
print("Name,Scoreのセットを加える")
print(df)


