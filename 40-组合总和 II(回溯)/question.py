"""
 @author：     JiaGuo
 @emil：       1520047927@qq.com
 @date：       Created in 2022/4/15 09:25
 @description：40-组合总和 II(回溯)
 @modified By：
 @version:     1.0
"""
import collections
from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        sum = 0
        candidates_len = len(candidates)
        # pos 下标   rest 还需要一个多大的数
        def dfs(pos: int, rest: int):

            missNum = rest
             # candidates_len
             # sequence
            # 递归退出条件
            if rest == 0:
                ans.append(sequence)
                return

            # 下标等于 freq的长度(即所有数字都遍历完了)   或者 还需要的数 比 下一个数还大  则不需要继续了
            if pos == len(freq) or rest < freq[pos]:
                return

            # dfs(pos + 1, rest)
            #
            # # most = min(rest // freq[pos], freq[pos][1])
            #
            # for i in range(1, most + 1):
            #     sequence.append(freq[pos][0])
            #     dfs(pos + 1, rest - i * freq[pos][0])

            for i in range(pos, candidates_len):
                sequence.append(freq[pos])
                dfs(pos+1, target - freq[pos])
                sequence.pop()


        # 统计每个数字出现的次数
        # freq = sorted(collections.Counter(candidates).items())
        freq = sorted(candidates)
        ans = []
        sequence = []
        dfs(0, target)


        return ans


if __name__ == '__main__':
    # 1  1  2  5  6  7  10
    candidates = [10, 1, 2, 7, 6, 1, 5]
    target = 8
    a = Solution().combinationSum2(candidates, target)
    print(a)
