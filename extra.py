from typing import Protocol, TypeVar, Optional, Generic
import numpy as np
import pytest
from main import Queue, MattQueueLink, MattQueueLinkX2

T = TypeVar("T")

class MattStackArrInt(Generic[T]):

    def __init__(self) -> None:
        self._items = np.zeros(2, dtype=int)

    def push(self, item: T) -> None:
        open_pos = np.where(self._items == 0)[0]
        for obj in self._items:
            open_pos = np.where(self._items == 0)[0]
            if obj != 0 and open_pos.size == 0:
                close_pos = np.where(self._items != 0)[0]
                scale = close_pos.size
                self._items = np.append(self._items, np.zeros(scale, dtype=int))
        if open_pos.size > 0:
            self._items[open_pos[0]] = item
        
    def pop(self) -> Optional[T]:
        if self.is_empty():
            raise ValueError("Empty")
        no_zero = np.where(self._items != 0)[0]
        top = no_zero[-1]
        popped_value = self._items[top]
        self._items[top] = 0

        open_pos_after = np.where(self._items == 0)[0]
        no_zero = np.where(self._items != 0)[0]

        if open_pos_after.size >= no_zero.size and self._items.size > 2:
            self._items = np.delete(self._items, open_pos_after)

        return popped_value

    def peek(self) -> Optional[T]:
        if self.is_empty():
            raise ValueError("Empty")
        no_zero = np.where(self._items != 0)[0]
        top = no_zero[-1]
        return self._items[top]
    
    def is_empty(self) -> bool:
        return np.all(self._items == 0)
    

@pytest.fixture
def queue() -> Queue:
    return MattQueueLink()

@pytest.fixture
def queue_v2() -> Queue:
    return MattQueueLinkX2()




# def temp_func(num):
#     matt = MattStackArr()
#     for i in range(num):
#         matt.push(1)
#     # matt.push(2)
#     #print(matt._items)
#     print(matt.is_empty())
#     print(matt._items)
# temp_func(0)

# import time
# q = MattQueueLink()

# start = time.time()
# for i in range(10000000):
#     q.enqueue(i)
# end = time.time() - start
# print(f'{end:.5f}s')

# q = MattQueueLinkX2()
# start = time.time()
# for i in range(10000000):
#     q.enqueue(i)
# end = time.time() - start
# print(f'{end:.5f}s')




# q.enqueue(10)
# q.enqueue(20)
# q.enqueue(30)

# print(q.dequeue())  
# print(q.peek())     
# print(q.is_empty()) 

# ms = MattStackArrAll()
# for i in range(9):
#     ms.push(1)
# print(ms._items)

# ms = MattStackArrAll()
# ms.push(1)
# ms.push("matt")





# import time

# ms = MattStackArrAll()
# start = time.time()
# last = start  # last checkpoint
# for i in range(10000):
#     ms.push(1)
#     if i % 1000 == 0:
#         now = time.time()
#         interval = now - last
#         print(f'{interval:.3f}')
#         last = now  # update the checkpoint

# end = time.time() - start
# print(f'Total time: {end:.3f}')

# start = time.time()
# ms.push(1)
# end = time.time() - start
# print(f'{end:.3f}')