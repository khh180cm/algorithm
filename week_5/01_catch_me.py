from collections import deque

c = 11
b = 2


def catch_me(cony_loc, brown_loc):
    while True:
        tik_tok = 1
        if 0 <= cony_loc <= 200000 and 0 <= brown_loc <= 200000:
            cony_s = tik_tok ** 2 / 2 + tik_tok / 2.0 + cony_loc
            brown_s = brown_loc * 2
            tik_tok += 1
            print(cony_loc, brown_loc)
            if brown_loc >= cony_loc:
                break
    return tik_tok


print(catch_me(c, b))  # 5가 나와야 합니다!