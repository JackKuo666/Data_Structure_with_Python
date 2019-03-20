# _*_ coding: UTF-8 _*_
"""插入排序（Insertion Sort）
升序：通过构建有序序列，将未排序数据，在已排序数据中从后向前扫描，找到相应位置并插入
时间复杂度：O（n）
稳定性：稳定
"""

def insert_sort(alist):
    # 从第二个位置起，即下标为1的元素开始向前插入
    for i in range(1, len(alist)):
        # 从第i个元素开始向前比较，如果小于前一个元素，交换位置
        for j in range(i, 0, -1):
            if alist[j] < alist[j-1]:
                alist[j], alist[j-1] = alist[j-1], alist[j]
alist = [54,26,93,17,77,31,44,55,20]
print("origin:",alist)
insert_sort(alist)
print("insert_sort:",alist)
