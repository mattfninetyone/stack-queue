# Implementation of Stack and Queue Data Structures.

### Overview 
- This project provides implementations of stack and queue data structures using various underlying data structures such as a numpy based array for a stack, and singly and doubly linked lists for queues.
- The implementations are designed to be generic, allowing them to store any data type.
- The code includes protocols to define the expected behavior of stacks and queues, ensuring that any implementation adheres to a consistent interface.

### Features
- **Stack Implementation**: A stack data structure using a numpy array, supporting standard operations like push, pop, and checking if the stack is empty. The assumption of using an array includes resizing when the stack is full (expected array behaviour).
- **Queue Implementations**: Two queue implementations:
  - A queue using a singly linked list.
  - A queue using a doubly linked list.
  - Both queue implementations support standard operations like enqueue, dequeue, and checking if the queue is empty.
  - Both are built using a separate ode class to assign values and pointers.
- **Type Safety**: Utilises Python's typing module to ensure type safety and clarity in the code.
- **Protocols**: Defines protocols for stacks and queues to enforce a consistent interface across different implementations.

### Testing
- The project includes a suite of tests using pytest to validate the functionality of the stack and queue implementations.
- The complete list of tests covered is as follows:
    1. **Stack Tests**:
        - Base Stack Tests:
            - Test that push adds an item to the stack.
            - Test that pop removes and returns the last item added to the stack.
            - Test that you can look at the top item of the stack without removing it.
            - Test that is_empty returns True when the stack is empty and False otherwise.
        - Additional Stack Tests:
            - Test that adding multiple items works correctly.
            - Tests that the array resizes correctly when the stack exceeds its initial capacity.
            - Test that popping or peeking at an empty stack raises an ValueError.
            - Test that the stack can store different data types (e.g., integers, strings).
            - Tests that the stack cannot store a mix of data types.
            - Test that peek maintains idempotency (multiple calls return the same result without modifying the stack).

    2. **Queue Tests**:
        - Base Queue Tests:
            - Test that enqueue adds an item to the end of the queue.
            - Test that dequeue removes and returns the item at the front of the queue.
            - Test that you can look at the front item of the queue without removing it.
            - Test that is_empty returns True when the queue is empty and False otherwise.
        - Additional Queue Tests:
            - Test that adding multiple items works correctly.
            - Test that dequeuing or peeking at an empty queue raises a ValueError.
            - Test that the queue can store different data types (e.g., integers, strings).
            - Test that the queue cannot store a mix of data types.
            - Test that head and tail return None when empty.
            - Test that for doubly linked list, the next and prev pointers are correctly assigned, and head.prev results to None after a dequeue (expected doubly linked list behaviour).


- To run the tests, use the command:
  ```bash
  pytest
  ```

### Requirements
- Python 3.8 or higher
- numpy
- pytest (for running tests)




