# 1323. Maximum 69 Number


def run(num):
    all_res = []
    for i in range(4):
        res = num + 3 * (10 ** i)
        if res == 9999:
            return 9999
        elif res > 9999:
            continue
        all_res.append(res)
    return max(all_res)


if __name__ == "__main__":
    num = 9996
    print(run(num))