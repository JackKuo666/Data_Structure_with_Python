"""归并排序
归并排序是采用分治法的一个非常典型的应用。归并排序的思想就是先递归分解数组，再合并数组。
将数组分解最小之后，然后合并两个有序数组，基本思路是比较两个数组的最前面的数，谁小就先取谁，取了后相应的指针就往后移一位。然后再比较，直至一个数组为空，最后把另一个数组的剩余部分复制过来即可。
时间复杂度：O(nlogn)
稳定性：稳定
"""

def merge_sort(alist):
    if len(alist) <= 1:
        return alist
    # 二次分解
    mid = len(alist)//2
    left = merge_sort(alist[:mid])
    right = merge_sort(alist[mid:])
    # 合并
    return merge(left, right)

def merge(left, right):
    """合并操作，将两个有序数组left[]和right[]合并成一个大的有序数组"""
    # left 与 right 的下标指针
    l, r = 0, 0
    result = []
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
    result += left[l:]
    result += right[r:]
    return result

alist = [54,26,93,17,77,31,44,55,20]
print("origin:", alist)
print("merge_sort:",merge_sort(alist))
