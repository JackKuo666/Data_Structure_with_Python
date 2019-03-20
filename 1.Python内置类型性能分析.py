# _*_ conding: UTF-8 _*_
from timeit import Timer

def test1():
    l = []
    for i in range(1000):
        l = l + [i]

def test2():
    l = []
    for i in range(1000):
        l.append(i)

def test3():
    l = [i for i in range(1000)]

def test4():
    l = list(range(1000))

t1 = Timer("test1()", "from __main__ import test1")
print("concat ", t1.timeit(number=1000), "seconds")

t2 = Timer("test2()", "from __main__ import test2")
print("append ", t2.timeit(number=1000), "seconds")

t3 = Timer("test3()", "from __main__ import test3")
print("comprehension ", t3.timeit(number=1000), "seconds")

t4 = Timer("test4()", "from __main__ import test4")
print("list range ", t4.timeit(number=1000), "seconds")


"""结果：
concat  1.421693535000486 seconds
append  0.1010527379994528 seconds
comprehension  0.036659903999861854 seconds
list range  0.018424673000481562 seconds
"""

print("*"*30)
# pop 测试
x = [i for i in range(2000000)]
pop_zero = Timer("x.pop(0)", "from __main__ import x")
print("pop_zero ", pop_zero.timeit(number=1000), "seconds")

pop_end = Timer("x.pop()", "from __main__ import x")
print("pop_end ", pop_end.timeit(number=1000), "seconds")

list_append = Timer("x.append(1)", "from __main__ import x")
print("list_append(从后边插入) ", list_append.timeit(number=1000), "seconds")

list_insert = Timer("x.insert(0,1)", "from __main__ import x")
print("list_insert(从前边插入) ", list_insert.timeit(number=1000), "seconds")

"""
pop_zero  3.0994806850003442 seconds
pop_end  0.0001244389995918027 seconds
list_append(从后边插入)  9.197799954563379e-05 seconds
list_insert(从前边插入)  3.44098534800014 seconds
"""