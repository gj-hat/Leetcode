class Solution:
    def question(self, num, nums):
        if num < 3:
            return 0
        count = 0
        for i in range(0, num):
            for j in range(i + 1, num):
                if k - i <= 1:
                    continue
                for k in range(j + 1, num):
                    if nums[k] == (3 * nums[j] - nums[i]):
                        count += 1
        return count


if __name__ == '__main__':
    num = int(input())
    nums = input().split()
    nums = [int(i) for i in nums]
    s = Solution().question(num, nums)
    print(s)
