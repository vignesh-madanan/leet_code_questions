# 1299. Replace Elements with Greatest Element on Right Side
# Input: arr = [17,18,5,4,6,1]
# Output: [18,6,6,6,1,-1]


def solution(arr):
    final = [-1]
    final.extend(max(arr[-1 - i :]) for i in range(len(arr) - 1))
    return final[::-1]


if __name__ == "__main__":
    print(
        list(
            map(
                solution,
                [
                    [17, 18, 5, 4, 6, 1],
                    [400],
                    [-1, -4, -8.0, -8.0, -6, 4],
                    [
                        5,
                        5,
                        5,
                        5,
                    ],
                ],
            )
        )
    )
