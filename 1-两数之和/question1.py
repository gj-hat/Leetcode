def main_body(nums, target):
    """
    暴力穷举
    :param nums:
    :param target:
    :return:
    """
    results = []
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            if target == nums[i] + nums[j]:
                results.append(i)
                results.append(j)
                break
    return results


def main_body_with_hashmap(nums, target):
    """
    穷举 + 遍历hashmap
    :param nums:
    :param target:
    :return:
    """
    results = []
    store_nums = dict()
    for i in range(len(nums)):
        another = target - nums[i]
        another_index = store_nums.get(another)
        if another_index is not None:
            results.append(i)
            results.append(another_index)
        else:
            store_nums[nums[i]] = i

    return results


if __name__ == '__main__':
    nums = [3, 2, 4]
    target = 6
    results = main_body_with_hashmap(nums, target)
    print(results)
