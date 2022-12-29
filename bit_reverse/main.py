test_state = 0b101
print((str(test_state) + " = " + str(bin(test_state))))

# 全反転
mask_state = 2**3 - 1
test_state_reverse = ~test_state & mask_state
print(bin(test_state_reverse))

# 特定のbitの反転
# 2番目だけ反転を考える
target_bit = 2
target_state = 2**(target_bit - 1)
test_state_part_reverse = test_state ^ target_state
print(bin(test_state_part_reverse))

