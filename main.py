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

    def __init__(self) -> None:...

    def push(self, item: T) -> None:...

    def pop(self) -> Optional[T]:...

    def peek(self) -> Optional[T]:...

    def is_empty(self) -> bool:...

class MattQueue(Generic[T]):

    def __init__(self) -> None:...

    def enqueue(self, item: T) -> None:...

    def dequeue(self) -> Optional[T]:...

    def peek(self) -> Optional[T]:...

    def is_empty(self) -> bool:...


