from typing import Generic, Optional, Protocol, Type, TypeVar

import numpy as np

T = TypeVar("T")


# PROTOCOLS
class Stack(Protocol[T]):
    """Protocol for a stack data structure."""

    def push(self, item: T) -> None:
        """Add an item to the top of the stack."""
        ...

    def pop(self) -> T:
        """Remove and return the top item from the stack."""
        ...

    def peek(self) -> T:
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
    def __init__(self, dtype: Type[T] | None = None) -> None:
        self._dtype = dtype or object
        self._items = np.empty(2, dtype=self._dtype)
        self._EMPTY = self._dtype()
        self._items[:] = self._EMPTY
        self._length = 0

    def push(self, item: T) -> None:
        """Adds an item to the top of the stack."""

        if not isinstance(item, self._dtype):
            raise TypeError("item should be of type " + str(self._dtype))

        if self._length == len(self._items):
            self._expand()

        self._items[self._length] = item

        self._length += 1

    def _expand(self) -> None:
        """Doubles the size of the internal array."""

        old_items = self._items
        old_size = self._length
        new_size = old_size * 2
        new_items = [self._EMPTY] * new_size
        new_items[:old_size] = old_items
        self._items = new_items

    def pop(self) -> T:
        """Removes and returns the top item from the stack."""

        if self.is_empty():
            raise ValueError("Stack is empty")

        idx = self._length - 1
        popped_value = self._items[idx]
        self._items[idx] = self._EMPTY
        self._length -= 1
        return popped_value

    def peek(self) -> T:
        """Returns the top item without removing it."""

        if self.is_empty():
            raise ValueError("Stack is empty")

        return self._items[self._length - 1]

    def is_empty(self) -> bool:
        return self._length == 0

    def __len__(self) -> int:
        return self._length


# ----- QUEUE IMPLEMENTATIONS ----- #
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
