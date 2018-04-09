"""
任意删除字符形成回文的个数
"""


# coding=utf-8
import sys
import random


def test_huiwen(huiwen_str):
    temp = reversed(list(huiwen_str))
    if list(temp) == list(huiwen_str):
        return 1
    else:
        return 0


def cut(s: str):
    results = []
    temp = list(s)
    for i in range(len(s)):
        slice = random.sample(list, i)
        print(slice)
    return results


if __name__ == "__main__":
    # 读取第一行的num
    # n = int(sys.stdin.readline().strip())
    n = "ABA"
    ans = 0
    temps = cut(n)
    print(temps)
    for temp in temps:
        if test_huiwen(temp):
            ans += 1

    print(ans)
