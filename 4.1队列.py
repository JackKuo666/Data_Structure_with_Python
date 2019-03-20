# _*_ coding: UTF-8  _*_


"""
# 队列 (queue): 只允许在一端进行插入操作，而在另一端进行删除操作的线性表。
先进先出
"""

class Queue(object):
    """队列"""
    def __init__(self):
        self.items = []

    def is_empty(self):
        """判断队列是否为空"""
        return self.items == []

    def enqueue(self, item):
        """进队列"""
        return self.items.insert(0, item)

    def dequeue(self):
        """出队列"""
        return self.items.pop()

    def size(self):
        """返回队列大小"""
        return len(self.items)


if __name__ == "__main__":
    q = Queue()
    q.enqueue("hello")
    q.enqueue("world")
    q.enqueue("itcast")
    print(q.size())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
