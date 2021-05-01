current_r, current_c, current_d = 7, 4, 0
current_room_map = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]


def get_count_of_departments_cleaned_by_robot_vacuum(r, c, d, room_map):
    cur_pos_state = room_map[r][c]
    cur_pos_state = 1

    search_area_dict = {
        0: room_map[r][:c],
        1: room_map[c][:],
        2: room_map[r][:][c+1:],
        3: room_map[c][r:],

    }
    search_area = search_area_dict[d]
    need_left_cleaning = 0 in search_area

    while True:
        if need_left_cleaning:
            d = 3
            c -= 1
            get_count_of_departments_cleaned_by_robot_vacuum(r, c, d, room_map)
        else:
            d = (d+4) % 4
            # 후진해서 다시 탐색
            r += 1
            get_count_of_departments_cleaned_by_robot_vacuum(r, c, d, room_map)
    return


print(get_count_of_departments_cleaned_by_robot_vacuum(current_r, current_c, current_d, current_room_map))
