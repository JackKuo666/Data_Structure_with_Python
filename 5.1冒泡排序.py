# _*_ coding: UTF-8 _*_
"""冒泡排序
时间复杂度：O（n**2）
升序：每次只比较左右两个，大的放右边
稳定性：稳定
"""

def bubble_sort(alist):
    for j in range(len(alist) - 1, 0, -1):
        # j表示每次遍历需要比较的次数，是逐渐减小的
        for i in range(j):
            if alist[i] > alist[i+1]:
                alist[i], alist[i+1] = alist[i+1], alist[i]


li = [54,26,93,17,77,31,44,55,20]
bubble_sort(li)
print(li)
