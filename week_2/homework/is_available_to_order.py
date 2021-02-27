"""
이진 탐색을 통한 주문 가능 여부 판별하기
"""


shop_menus = ["만두", "떡볶이", "오뎅", "사이다", "콜라"]
shop_orders = ["오뎅", "콜라", "만두"]


def is_available_to_order(menus, orders):
    menus.sort()
    for order in orders:
        left = 0
        right = len(menus) - 1
        middle = (left + right) // 2
        while left <= right:
            if order == menus[middle]:
                # 주문 가능 메뉴이면 그 다음 메뉴 검증
                break
            elif menus[middle] > order:
                right = middle - 1
            else:
                left = middle + 1
            middle = (left + right) // 2
        else:
            # 주문 불가능 메뉴 존재
            return False
    # 모두 주문 가능
    return True


result = is_available_to_order(shop_menus, shop_orders)
print(result)
