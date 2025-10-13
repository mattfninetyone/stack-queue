from main import Stack, Queue, MattStack, MattQueue, T
import pytest

@pytest.fixture
def stack() -> Stack:
    # create and return a new queue implementation
    return MattStack()

@pytest.fixture
def queue() -> Queue:
    # create and return a new queue implementation
    return MattQueue()

# ----- STACK TESTS ----- #

def test_stack_push(stack):
    # Arrange
    item = 12
    # Act
    stack.push(item)

    # Assert
    assert not stack.is_empty()
    assert stack.peek() is item


def test_stack_pop(stack):
    # Arrange
    item = 12
    # Act
    stack.push(item)
    popped_item = stack.pop()

    # Assert
    assert popped_item is item
    assert stack.is_empty()

def test_stack_peek(stack):
    # Arrange
    item = 12
    # Act
    stack.push(item)
    top_item = stack.peek()

    # Assert
    assert top_item == item
    assert not stack.is_empty()

def test_stack_is_empty(stack):
    # Arrange

    # Act

    # Assert
    assert stack.is_empty()

def test_stack_multi_push(stack):
    # Arrange
    items = [1, 2, 3, 4, 5]
    # Act
    for item in items:
        stack.push(item)
    # Assert
    assert not stack.is_empty()
    assert stack.peek() is items[-1]

def test_stack_none(stack):
    # Arrange
    
    # Act
    
    # Assert
    assert stack.pop() is None
    assert stack.peek() is None

def test_stack_multi_op(stack):
    item_1 = 1
    item_2 = 2
    stack.push(item_1)
    assert stack.peek() is 1
    assert stack.pop() is 1
    stack.push(item_1)
    stack.push(item_2)
    assert stack.pop() is 2
    assert queue.pop() is 1

# ----- QUEUE TESTS ----- #

def test_queue_enqueue(queue):
    # Arrange
    item = 12
    # Act
    queue.enqueue(item)
    # Assert
    assert not queue.is_empty()
    assert queue.peek() is item

def test_queue_dequeue(queue):
    # Arrange
    item = 12
    # Act
    queue.enqueue(item)
    dequeued_item = queue.dequeue()

    # Assert
    assert dequeued_item is item
    assert queue.is_empty()

def test_queue_peek(queue):
    # Arrange
    item = 12
    # Act
    queue.enqueue(item)
    front_item = queue.peek()

    # Assert
    assert front_item is item
    assert not queue.is_empty()

def test_queue_is_empty(queue):
    # Arrange

    # Act

    # Assert
    assert queue.is_empty()

def test_queue_multi_push(queue):
    # Arrange
    items = [1, 2, 3, 4, 5]
    # Act
    for item in items:
        queue.enqueue(item)
    # Assert
    assert not queue.is_empty()
    assert queue.peek() is items[-1]

def test_queue_none(queue):
    # Arrange

    # Act
    
    # Assert
    assert queue.dequeue() is None
    assert queue.peek() is None

def test_queue_multi_op(queue):
    item_1 = 1
    item_2 = 2
    queue.enqueue(item_1)
    assert queue.peek() is 1
    assert queue.dequeue() is 1
    queue.enqueue(item_1)
    queue.enqueue(item_2)
    assert queue.dequeue() is 1
    assert queue.dequeue() is 2














