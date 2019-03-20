# _*_ coding: UTF-8 _*_
"""希尔排序（shell sort）
gap = 是子序列的个数
时间复杂度：O（n**2）
"""

def shell_sort(alist):
    n = len(alist)

    # 初始步长
    gap = n//2
    while gap > 0:
        # 按步长进行插入排序
        for i in range(gap, n):
            #print("i:",i,alist[i])
            j = i
            # 插入排序
            while j >= gap and alist [j - gap] > alist[j]:
                #print("j",alist[j - gap], alist[j])
                alist[j - gap], alist[j] = alist[j], alist[j - gap]
                j -= gap

        # 得到新的步长
        gap = gap//2

alist = [54,26,93,17,77,31,44,55,20]
print("origin:",alist)
shell_sort(alist)
print("shell_sort:",alist)
