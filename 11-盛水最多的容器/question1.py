import time


def func1(arr: help("This is list")):
    arr1 = list()
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            arr1.append(arr[i] * (j - i)) if arr[i] < arr[j] else arr1.append(arr[j] * (j - i))
    arr1.sort(reverse=True)
    return arr1



if __name__ == '__main__':
    start = time.clock()

    arr = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print(func1(arr))

    stop = time.clock()
    print(stop - start)
