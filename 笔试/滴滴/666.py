
class Solution:

    def question(self, arr, num):
        res = 0
        temp_arr = arr.copy()
        temp_arr.sort(reverse=True)


        # for i in range(len(arr)):



        print(temp_arr)

        pass


    def average(self, arr):
        return sum(arr) / len(arr)



if __name__ == '__main__':

    in1 = input().split(" ")
    in1 = [int(i) for i in in1]

    in2 = input().split(" ")
    in2 = [int(i) for i in in2]

    a = Solution().question(in2, in1[1])


