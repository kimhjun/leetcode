from typing import List
from collections import defaultdict

def oddCells(m: int, n: int, indices: List[List[int]]) -> int:
    row_crossed_cnt = defaultdict(int)
    col_crossed_cnt = defaultdict(int)

    for i in range(m):
        row_crossed_cnt[i] = 0
    for j in range(n):
        col_crossed_cnt[j] = 0

    for li in indices:
        row_crossed_cnt[li[0]] += 1
        col_crossed_cnt[li[1]] += 1

    counter = 0
    for _, i in row_crossed_cnt.items():
        for _, j in col_crossed_cnt.items():
            if (i + j) % 2 == 1:
                counter += 1
    return counter

if __name__ == "__main__":
    m = 28
    n = 38
    indices = [[17,16],[26,31],[19,12],[22,24],[17,28],[23,21],[27,32],[23,27],[23,33],[18,7],[4,20],[0,31],[25,33],[5,22]]
    result = oddCells(m, n, indices)
    print(result)