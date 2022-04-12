def fun(fir, sec):


    print("sum")


if __name__ == '__main__':
    fir_list = input().split(" ")
    sec_list = []
    for i in range(int(fir_list[0])):
        sec_list.append(input().split(" "))
    print("fir_list:", fir_list)
    print("sec_list:", sec_list)
    fun(fir_list, sec_list)
