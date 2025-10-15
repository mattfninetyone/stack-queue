from typing import Protocol, TypeVar, Optional, Generic
import numpy as np


T = TypeVar("T")

# PROTOCOLS
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

# ----- STACK IMPLEMENTATIONS ----- #

class MattStackArrAll(Generic[T]):

    _EMPTY = object()

    def __init__(self) -> None:
        self._items = np.empty(2, dtype=object)
        self._items[:] = self._EMPTY

    def push(self, item: T) -> None:
        if not self.is_empty() and type(self.peek()) != type(item):
            raise ValueError("Too Many Types")

        open_pos = np.where(self._items == self._EMPTY)[0]
        for obj in self._items:
            open_pos = np.where(self._items == self._EMPTY)[0]
            if obj != self._EMPTY and open_pos.size == 0:
                close_pos = np.where(self._items != self._EMPTY)[0]
                scale = close_pos.size
                self._items = np.append(self._items, np.full(scale, self._EMPTY, dtype=object))
        if open_pos.size > 0:
            self._items[open_pos[0]] = item
        
    def pop(self) -> Optional[T]:
        if self.is_empty():
            raise ValueError("Empty")
        no_zero = np.where(self._items != self._EMPTY)[0]
        top = no_zero[-1]
        popped_value = self._items[top]
        self._items[top] = self._EMPTY

        open_pos_after = np.where(self._items == self._EMPTY)[0]
        no_zero = np.where(self._items != self._EMPTY)[0]

        if open_pos_after.size >= no_zero.size and self._items.size > 2:
            self._items = np.delete(self._items, open_pos_after)

        return popped_value

    def peek(self) -> Optional[T]:
        if self.is_empty():
            raise ValueError("Empty")
        no_zero = np.where(self._items != self._EMPTY)[0]
        top = no_zero[-1]
        return self._items[top]
    
    def is_empty(self) -> bool:
        return np.all(self._items == self._EMPTY)

# ----- QUEUE AND NODE IMPLEMENTATIONS ------ #
# LINKED LIST NODE
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# LINKED LIST
class MattQueueLink(Generic[T]):

    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def enqueue(self, item: T) -> None:
        if not self.is_empty() and type(self.peek()) != type(item):
            raise ValueError("Too Many Types")

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

# DBL LINKED LIST NODE
class NodeX2:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

# DBL LINKED LIST
class MattQueueLinkX2(Generic[T]):

    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def enqueue(self, item: T) -> None:
        if not self.is_empty() and type(self.peek()) != type(item):
            raise ValueError("Too Many Types")

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


