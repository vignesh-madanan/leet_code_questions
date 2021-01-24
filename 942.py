# Given a string S that only contains "I" (increase) or "D" (decrease), let N = S.length.

# Return any permutation A of [0, 1, ..., N] such that for all i = 0, ..., N-1:

# If S[i] == "I", then A[i] < A[i+1]
# If S[i] == "D", then A[i] > A[i+1]


def solution(strx):
    all_n = list(range(0, len(strx) + 1))
    result = []
    for alphabet in strx:
        if alphabet == "D":
            result.append(all_n.pop())
        else:
            result.append(all_n.pop(0))
    result.append(all_n.pop())
    return result


if __name__ == "__main__":
    for q, sol in [
        ["IDID", [0, 4, 1, 3, 2]],
        ["III", [0, 1, 2, 3]],
        ["DDI", [3, 2, 0, 1]],
    ]:
        print(sol == solution(q))