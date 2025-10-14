from typing import Protocol, TypeVar, Optional, Generic
import numpy as np

T = TypeVar("T")

class Stack(Protocol[T]):
    """Protocol for a stack data structure."""

    def push(self, item: T) -> None:
        """Add an item to the top of the stack."""
        ...

    def pop(self) -> Optional[T]:
        """Remove and return the top item from the stack."""
        ...

    def peek(self) -> Optional[T]:
        """Return the top item without removing it."""
        ...

    def is_empty(self) -> bool:
        """Return True if the stack is empty."""
        ...

class Queue(Protocol[T]):
    """Protocol for a queue data structure."""

    def enqueue(self, item: T) -> None:
        """Add an item to the end of the queue."""
        ...

    def dequeue(self) -> Optional[T]:
        """Remove and return the item at the front of the queue."""
        ...

    def peek(self) -> Optional[T]:
        """Return the front item without removing it."""
        ...

    def is_empty(self) -> bool:
        """Return True if the queue is empty."""
        ...

# STACK IMPLEMENTATIONS #
class MattStackArr(Generic[T]):

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

class MattStackArrAll(Generic[T]):
    """IGNORE THIS: PLACEHOLDER FOR GENERALISED STACK IMPLEMENTATION"""
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

# QUEUE AND NODE IMPLEMENTATIONS #
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class MattQueueLink(Generic[T]):

    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def enqueue(self, item: T) -> None:
        new_node = Node(item)
        if self.tail is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def dequeue(self) -> Optional[T]:
        if self.head is None:
            raise ValueError("Empty")
        value = self.head.value
        self.head = self.head.next
        if self.head is None:  
            self.tail = None
        return value
    
    def peek(self) -> Optional[T]:
        if self.head is None:
            raise ValueError("Empty")
        return self.head.value

    def is_empty(self) -> bool:
        return self.head is None

class NodeX2:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class MattQueueLinkX2(Generic[T]):

    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def enqueue(self, item: T) -> None:
        new_node = NodeX2(item)
        if self.tail is None:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def dequeue(self) -> Optional[T]:
        if self.head is None:
            raise ValueError("Empty")
        value = self.head.value
        self.head = self.head.next
        if self.head is None:  
            self.tail = None
        else:
            self.head.prev = None
        return value

    def peek(self) -> Optional[T]:
        if self.head is None:
            raise ValueError("Empty")
        return self.head.value

    def is_empty(self) -> bool:
        return self.head is None

# def temp_func(num):
#     matt = MattStackArr()
#     for i in range(num):
#         matt.push(1)
#     # matt.push(2)
#     #print(matt._items)
#     print(matt.is_empty())
#     print(matt._items)
# temp_func(0)

import time
q = MattQueueLink()

start = time.time()
for i in range(10000000):
    q.enqueue(i)
end = time.time() - start
print(f'{end:.5f}s')

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