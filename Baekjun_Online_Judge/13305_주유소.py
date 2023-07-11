import sys
read = sys.stdin.readline


def main():
    n = int(read())
    distance = list(map(int, read().split()))
    price = list(map(int, read().split()))

    answer = 0
    min_cost = price[0]
    for i in range(n-1):
        if i == 0:
            answer += price[i] * distance[i]
            continue
        if price[i] < min_cost:
            # price[i:] = [price[i-1] for _ in range(len(price[i:]))]
            min_cost = price[i]
        answer += min_cost * distance[i]

    print(answer)



# def find_cost_until_min_price(distance, price):
#     # print("지금 거리, 가격", distance, price)
#     if len(distance) == 0:
#         return 0
#     if len(distance) == 1:
#         return price[0] * distance[0]
#
#     min_price_idx = 0
#     for i in range(len(price[:-1])):
#         if price[i] < price[min_price_idx]:
#             min_price_idx = i
#
#     # print(find_cost_until_min_price(distance[:min_price_idx], price[:min_price_idx+1]),  price[min_price_idx] * sum(price[min_price_idx:]))
#     return (find_cost_until_min_price(distance[:min_price_idx], price[:min_price_idx+1]) +
#             price[min_price_idx] * sum(distance[min_price_idx:]))

main()