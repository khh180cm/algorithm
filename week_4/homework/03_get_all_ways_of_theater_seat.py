seat_count = 9
vip_seat_array = [4, 7]



count = 0


def get_all_ways_of_theater_seat(total_count, fixed_seat_array):
    memory = {}
    for i in fixed_seat_array:
        memory.setdefault(i, i)
    while True:
        for i in range(0, total_count):
            if len(memory) == 9:
                print("called")
                global count
                count += 1

            if i not in memory:
                memory.setdefault(i, i)
                print(memory)
            elif i+1 not in memory:
                memory.setdefault(i+1, i)
                print(memory)
            elif i-1 not in memory:
                memory.setdefault(i-1, i)
            else:
                get_all_ways_of_theater_seat(total_count, fixed_seat_array)
                return
# 12가 출력되어야 합니다!
print(get_all_ways_of_theater_seat(seat_count, vip_seat_array))
