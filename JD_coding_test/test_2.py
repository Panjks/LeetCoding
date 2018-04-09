"""
1~n的最小公倍数
"""


# coding=utf-8
import sys


def zxgbs(answer, num):
    if answer >= num:
        temp = answer
    else:
        temp = num
    while True:
        if (temp % num == 0 and temp % answer == 0):
            return temp
        else:
            temp += 1


if __name__ == "__main__":
    # 读取第一行的num
    # n = int(sys.stdin.readline().strip())
    n = 5
    ans = 1
    for i in range(1, n + 1):
        ans = zxgbs(ans, i)
    print(ans)
