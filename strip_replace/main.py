# 基本的には同じ結果になる
str1 = "Hello World!"
print(str1 + "の場合")
print("stripの結果 → " + str1.strip("World!"))
print("replaceの結果 → " + str1.replace("World!", ""))

print("----------")

# 一部のケースで意図しない文字がstripでは消える
str2 = "id=dummy"
print(str2 + "の場合")
print("stripの結果 → " + str2.strip("id="))
print("replaceの結果 → " + str2.replace("id=", ""))
