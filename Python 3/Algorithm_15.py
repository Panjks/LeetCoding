"""
Problem: 3SUM


Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0?
Find all unique triplets in the array which gives the sum of zero.

For example, given array S = [-1, 0, 1, 2, -1, -4],
A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""


class SolutionFailedTimeOut:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        for i in range(0, len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                for k in range(j + 1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        temp = [nums[i], nums[j], nums[k]]
                        result.append(temp)
        # 除重算法
        temp = []
        for i in result:
            i.sort()
            if i not in temp:
                temp.append(i)
        result = temp
        return result


class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        result = []
        i = 0
        while i < len(nums) - 2:
            j = i + 1
            k = len(nums) - 1
            while j < k:
                if nums[j] + nums[k] + nums[i] == 0:
                    temp = [nums[i], nums[j], nums[k]]
                    result.append(temp)
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
                elif nums[j] + nums[k] + nums[i] < 0:
                    j += 1
                else:
                    k -= 1
            i = i + 1
            while i < len(nums) - 2 and nums[i] == nums[i - 1]:
                i += 1
        return result

    """
    求一个列表中所有和为零的二元组的一种思路是先把列表排序，再用两个指针从两头向中间移动。
    如果前后两个数的和小于0，则左指针右移；如果和大于0，则右指针左移。
    求三元组时可以参考这种做法，第一个数a确定后，可以理解为求列表中和为-a的二元组。
    由于不要考虑重复的元组，遇到重复的数可以直接跳过。
    """


if __name__ == "__main__":
    sln = Solution()
    test_nums = [-1, 0, 1, 2, -1, -4]
    print(sln.threeSum(test_nums))
    # Finished
