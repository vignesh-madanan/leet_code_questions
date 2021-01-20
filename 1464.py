# 1464. Maximum Product of Two Elements in an Array
import heapq


def run(nums):
    heapq.heapify(nums)

    if nums[0] < 0 and nums[1] < 0:
        return (nums[0] - 1) * (nums[0] - 1)

    x, y = heapq.nlargest(2, nums)

    return (x - 1) * (y - 1)


if __name__ == "__main__":
    nums = [1, 5, 4, 5]

    print(run(nums))