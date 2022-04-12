import time


def func(arr: list):
    arr.sort()
    l = len(arr)
    resArr = list()
    i = 0
    while i < (l - 2):
        left = i + 1
        right = l - 1
        if arr[i] >= 0:
            break
        while left < right:
            if (arr[i] + arr[left] + arr[right]) > 0:
                right -= 1
            elif (arr[i] + arr[left] + arr[right]) < 0:
                left += 1
            if (arr[i] + arr[left] + arr[right]) == 0 and left != right:
                resArr.append([arr[i], arr[left], arr[right]])
                left += 1
        if arr[i] != arr[i + 1]:
            i += 1
        else:
            i += 2
    return resArr


if __name__ == '__main__':
    start = time.clock()
    nums = [-1, 0, 1, 2, -1, -4]
    print(func(nums))
    stop = time.clock()
    print(f"用时:", stop - start)
