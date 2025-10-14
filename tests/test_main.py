from main import Stack, Queue, MattStackArr, MattQueueLink, T
import pytest

@pytest.fixture
def stack() -> Stack:
    # create and return a new queue implementation
    return MattStackArr()

@pytest.fixture
def queue() -> Queue:
    # create and return a new queue implementation
    return MattQueueLink()

# ----- STACK TESTS ----- #

def test_stack_push(stack):
    # Arrange
    item = 12
    # Act
    stack.push(item)

    # Assert
    assert not stack.is_empty()
    assert stack.peek() == item


def test_stack_pop(stack):
    # Arrange
    item = 12
    # Act
    stack.push(item)
    popped_item = stack.pop()

    # Assert
    assert popped_item == item
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
    for i in reversed(items):  
        assert stack.pop() == i

def test_stack_none(stack):
    # Arrange
    
    # Act
    
    # Assert
    with pytest.raises(ValueError) as e1:
        stack.pop()
    with pytest.raises(ValueError) as e2:
        stack.peek()

    assert str(e1.value) == "Empty"
    assert str(e2.value) == "Empty"

def test_stack_multi_op(stack):
    for i in range(1,10):
        stack.push(i)
    for i in reversed(range(1,10)):
        assert stack.pop() == i

def test_stack_zero_as_input(stack):
    item = 0

    stack.push(item)

    assert not stack.is_empty()
    assert stack.peek() == item

def test_stack_str_as_input(stack):
    item = "matt"

    stack.push(item)

    assert not stack.is_empty()
    assert stack.peek() == item

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
    assert queue.is_empty()

def test_queue_multi_push(queue):
    # Arrange
    items = [1, 2, 3, 4, 5]
    # Act
    for item in items:
        queue.enqueue(item)
    # Assert
    assert not queue.is_empty()
    for i in items:  
        assert queue.dequeue() == i

def test_queue_none(queue):
    with pytest.raises(ValueError) as e1:
        queue.dequeue()
    with pytest.raises(ValueError) as e2:
        queue.peek()

    assert str(e1.value) == "Empty"
    assert str(e2.value) == "Empty"

def test_queue_multi_op(queue):
    for i in range(10):
        queue.enqueue(i)
    for i in range(10):
        assert queue.dequeue() == i














