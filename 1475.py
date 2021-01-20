# 1475. Final Prices With a Special Discount in a Shop
# Input: prices = [8,4,6,2,3]
# Output: [4,2,4,2,3]


def final_price(prices):
    for i in range(0, len(prices) - 1):
        if prices[i] >= prices[i + 1]:
            prices[i] -= prices[i + 1]
    return prices


if __name__ == "__main__":
    all_ques = [
        ([8, 4, 6, 2, 3], [4, 2, 4, 2, 3]),
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
        ([10, 1, 1, 6], [9, 0, 1, 6]),
    ]
    print([ques[1] == final_price(ques[0]) for ques in all_ques])
