case = [6988,6982,6658,6045,6387,7654,7097,8868,9180,9353,9105,8574,11079,11618,13215,12541,12528,10710]
def SelectionSort(case):
    for i in range(len(case)):
        min = i
        for j in range( i+1,len(case)):
            if case[min] > case[j]:
                min = j
            case[i], case[min] = case[min], case[i]
    return case
print("排序前的数组：", case)
print("排序后的数组：", SelectionSort(case))
print("最大值：", case[-1], "\n最小值：", case[0])
