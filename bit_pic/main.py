for state in range(2**2):
    init_state = state
    print("init_state = " + str(bin(init_state)))

    temp_bit = [0, 0]
    for s_i in range(2):
        # 取り出したいbitだけ立てる
        temp_bit[s_i] = init_state & 2**s_i
        # 0 or 1にする
        temp_bit[s_i] = temp_bit[s_i] >> s_i

    print("取り出したbit = " + str(temp_bit))
