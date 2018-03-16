"""
Problem: Hamming Distance\


The Hamming distance between two integers is the number of positions at which the corresponding bits are different.
Given two integers x and y, calculate the Hamming distance.

Example:

    Input: x = 1, y = 4
    Output: 2
    Explanation:
    1   (0 0 0 1)
    4   (0 1 0 0)
           ↑   ↑
    The above arrows point to positions where the corresponding bits are different.
"""


class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        return bin(x ^ y).count('1')

    """
    Python的表达式写法与C/C++类似。只是在某些写法有所差别。
    主要的算术运算符与C/C++类似。+, -, *, /, //, **, ~, %分别表示加法或者取正、减法或者取负、乘法、除法、整除、乘方、取补、取模。
    >>, <<表示右移和左移。&, |, ^表示二进制的AND, OR, XOR运算。
    >, <, ==, !=, <=, >=用于比较两个表达式的值，分别表示大于、小于、等于、不等于、小于等于、大于等于。
    在这些运算符里面，~, |, ^, &, <<, >>必须应用于整数。
    Python使用and, or, not表示逻辑运算。
    
    Python count() 方法用于统计字符串里某个字符出现的次数。可选参数为在字符串搜索的开始与结束位置。
    """


if __name__ == "__main__":
    sln = Solution()
    test_x = 1
    test_y = 4
    print(sln.hammingDistance(test_x, test_y))
    # Finished.
