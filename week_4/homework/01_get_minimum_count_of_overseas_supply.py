"""
최소 납품 횟수 구하기
"""

import heapq

ramen_stock = 4
supply_dates = [4, 10, 15]
supply_supplies = [20, 5, 10]
supply_recover_k = 30


def get_minimum_count_of_overseas_supply(stock, dates, supplies, k):
    # 공급받은 횟수
    supplied_count = 0
    cur_day_idx = 0
    heap = []
    for i in range(len(dates)):
        heapq.heappush(heap, -1 * supplies[i])
    # 현재 공장 재고
    cur_stock = stock

    # 기존 납품업체 수리 기간 동안
    while k >= 0:
        # 현재 공장 재고가 0이면
        if cur_stock == 0:
            cur_stock += -heapq.heappop(heap)
            supplied_count += 1
        k -= 1
        cur_stock -= 1
    return supplied_count


print(get_minimum_count_of_overseas_supply(ramen_stock, supply_dates, supply_supplies, supply_recover_k))
