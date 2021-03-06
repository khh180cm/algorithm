"""
최대 할인 가격을 구하기
"""

shop_prices = [30000, 2000, 1500000]
user_coupons = [20, 40]


class Node:
    def __init__(self, price, coupon):
        self.total_price = price * (1 - coupon / 100)
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, price, discount):
        new_node = Node(price, discount)
        # 비어 있으면
        if self.is_empty():
            self.head = new_node
            return
        # 비어있지 않으면
        cur_node = self.head
        while cur_node.next:
            cur_node = cur_node.next
        cur_node.next = new_node

    def is_empty(self):
        return self.head is None

    def pop(self):
        if self.is_empty():
            return False
        deleted_node = self.head
        self.head = self.head.next
        return deleted_node.total_price


# 방법 1 - 오름차순 정렬 후 링크드 리스트 활용
def get_max_discounted_price(prices, coupons):
    total_price = 0
    linked_list = LinkedList()

    # 오름차순 정렬
    prices.sort()
    coupons.sort()
    while prices and coupons:
        price = prices.pop()
        coupon = coupons.pop()
        linked_list.append(price, coupon)
    while True:
        cur_price = linked_list.pop()
        if cur_price is False:
            break
        total_price += cur_price

    for no_dc_price in prices:
        total_price += no_dc_price
    return int(total_price)


print(get_max_discounted_price(shop_prices, user_coupons))


# 방법 2 - 리스트 활용
def get_max_discounted_price_2(prices, coupons):
    total_price = 0
    while coupons:
        # 최대 할인 쿠폰
        max_dc_coupon = max(coupons)
        coupons.remove(max_dc_coupon)
        # 가격 비싼 제품
        max_price = max(prices)
        prices.remove(max_price)
        # 총합 누적
        total_price += (max_price * (1 - max_dc_coupon/100))
    # 할인 미적용 제품들
    for no_dc_price in prices:
        total_price += no_dc_price
    return int(total_price)


shop_prices = [30000, 2000, 1500000]
user_coupons = [20, 40]

print(get_max_discounted_price_2(shop_prices, user_coupons))
