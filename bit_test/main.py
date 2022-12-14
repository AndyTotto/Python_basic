# bitをそのまま入れる
a0 = 0b00
a1 = 0b01
a2 = 0b10
a3 = 0b11

# 入れた変数をそのまま表示
print("入れた変数をそのまま表示")
print(a0)
print(a1)
print(a2)
print(a3)
print("----------")

# 変数をbitのまま表示
print("変数をbitのまま表示")
print(bin(a0))
print(bin(a1))
print(bin(a2))
print(bin(a3))

print("----------")

# シフト
test_shift = 1 #0b01
# 左に1bit分シフト
test_shift_l1 = test_shift << 1
print("左に1bitシフト")
print(test_shift_l1)
# 左に2bit分シフト
test_shift_l2 = test_shift << 2
print("左に2bitシフト")
print(test_shift_l2)

print("----------")

# 論理演算
test_110 = 6
test_100 = 4
print(bin(test_110) + "と" + bin(test_100) + "で演算する")

print("----------")

# 論理積
test_and_res = test_110 & test_100
print("論理積")
print(test_and_res)
print(bin(test_and_res))

print("----------")

# 論理和
test_or_res = test_110 | test_100
print("論理和")
print(test_or_res)
print(bin(test_or_res))

print("----------")

# 排他的論理和
test_xor_res = test_110 ^ test_100
print("排他的論理和")
print(test_xor_res)
print(bin(test_xor_res))

print("----------")

# 左から2番目のbitを取り出したい
test_pic_2 = 0b10

test_pic_2_res_110 = test_110 & test_pic_2
test_pic_2_res_110 = test_pic_2_res_110 >> 1
print(test_pic_2_res_110)

test_pic_2_res_100 = test_100 & test_pic_2
test_pic_2_res_100 = test_pic_2_res_100 >> 1
print(test_pic_2_res_100)
