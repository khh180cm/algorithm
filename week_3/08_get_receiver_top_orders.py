"""
[6 <- 9 <- 5 <- 7 <- 4]
[0, 0, 2, 2, 4] 가 반환되어야 한다!
"""
top_heights = [6, 9, 5, 7, 4]


def get_receiver_top_orders(heights):
    answer = [0] * len(heights)
    while heights:
        top = heights.pop()
        for idx in range(len(heights)-1, 0, -1):
            if heights[idx] > top:
                answer[len(heights)] = idx + 1
                break
    return answer


print(get_receiver_top_orders(top_heights))