# Best Time to Buy and Sell Stock II


def maxProfit(prices):
    return sum(
        (prices[idx + 1] - prices[idx])
        for idx in range(len(prices) - 1)
        if prices[idx] < prices[idx + 1]
    )


if __name__ == "__main__":
    for q, a in [[[7, 1, 5, 3, 6, 4], 7], [[1, 2, 3, 4, 5], 4], [[7, 6, 4, 3, 1], 0]]:
        print(maxProfit(q) == a)
