# _*_ coding: UTF-8 _*_
import time

# 如果 a+b+c=1000，且 a^2+b^2=c^2（a,b,c 为自然数），如何求出所有a、b、c可能的组合?

# 第一次尝试
start_time = time.time()
for a in range(1001):
    for b in range(1001):
        c = 1000 - a - b
        if a**2 + b**2 == c**2:
            print("a:%d, b:%d, c:%d " %(a,b,c))
end_time = time.time()
print("time:%f" %(end_time-start_time))  # 1.31

print("*"*30)
# 第二次尝试
start_time = time.time()
for a in range(1001):
    for b in range(1001-a):
        c = 1000 - a - b
        if a**2 + b**2 == c**2:
            print("a:%d, b:%d, c:%d " %(a,b,c))
end_time = time.time()
print("time:%f" %(end_time-start_time))  # 0.69

# 时间复杂度： T(n) = O(n*n*(1+1)) = O(n*n) = O(n2)