from typing import Protocol, TypeVar, Optional, Generic

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

class MattStack(Generic[T]):

    def __init__(self) -> None:
        self._items: list[T] = []

    def push(self, item: T) -> None:
        self._items.append(item)

    def pop(self) -> Optional[T]:
        if self.is_empty():
            return None
        return self._items.pop()

    def peek(self) -> Optional[T]:
        if self.is_empty():
            return None
        return self._items[-1]

    def is_empty(self) -> bool:
        return len(self._items) == 0

class MattQueue(Generic[T]):

    def __init__(self) -> None:
        self._items: list[T] = []

    def enqueue(self, item: T) -> None:
        self._items.append(item)

    def dequeue(self) -> Optional[T]:
        if self.is_empty():
            return None
        return self._items.pop(0)

    def peek(self) -> Optional[T]:
        if self.is_empty():
            return None
        return self._items[0]

    def is_empty(self) -> bool:
        return len(self._items) == 0

# matts = MattStack()
# matts.push(12)
# matts.push(13)
# matts.push(90)
# print(matts.is_empty())
