# _*_ coding: UTF-8 _*_
"""选择排序（Selection sort）
升序：每次从 未排序区域中选出最大的 与 在未排序区域的第一个位置的数 交换
时间复杂度：O（n**2）
稳定性：不稳定
"""

def selection_sort(alist):
    # 需要进行n-1次选择操作
    for i in range(len(alist) - 1):
        # 记录最小位置
        min_index = i
        for j in range(i + 1, len(alist)):
            if alist[j] < alist[min_index]:
                min_index = j
        # 如果选择出的数据不在正确的位置，进行交换
        if min_index != i:
            alist[i], alist[min_index] = alist[min_index], alist[i]

alist = [54,226,93,17,77,31,44,55,20]
print("origin alist:",alist)
selection_sort(alist)
print("selection_sort:",alist)
